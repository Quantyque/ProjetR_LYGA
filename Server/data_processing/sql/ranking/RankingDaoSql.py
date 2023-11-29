from data_processing.sql.ranking.IRankingDaoSql import IRankingDaoSql
from data_processing.api.startgg.tournament.ITournamentDaoApi import ITournamentDaoApi
from data_processing.api.startgg.tournament.TournamentDaoApi import TournamentDaoApi
from data_processing.api.startgg.event.IEventDaoApi import IEventDaoApi
from data_processing.api.startgg.event.EventDaoApi import EventDaoApi
from data_processing.api.startgg.video_game.IVideoGameDaoApi import IVideoGameDaoApi
from data_processing.api.startgg.video_game.VideoGameDaoApi import VideoGameDaoApi
from data_processing.sql.player.IPlayerDaoSql import IPlayerDaoSql
from data_processing.sql.player.PlayerDaoSql import PlayerDaoSql
from data_processing.sql.elo.IEloDaoSql import IEloDaoSql
from data_processing.sql.elo.EloDaoSql import EloDaoSql
from data_processing.sql.season.ISeasonDaoSql import ISeasonDaoSql
from data_processing.sql.season.SeasonDaoSql import SeasonDaoSql
from model.ranking import Ranking
from model.tournament import Tournament
from model.event import Event
from model.set import Set
from data_processing.sql.dao import Dao
from typing import Dict

class RankingDaoSql(IRankingDaoSql, Dao):

    def __init__(self):
        super().__init__()
        # Initialise les DAO
        self.__tournament_dao_api: ITournamentDaoApi = TournamentDaoApi()
        self.__videogame_dao_api: IVideoGameDaoApi = VideoGameDaoApi()
        self.__season_dao_sql: ISeasonDaoSql = SeasonDaoSql()
        self.__player_dao_sql: IPlayerDaoSql = PlayerDaoSql()
        self.__elo_dao_sql: IEloDaoSql = EloDaoSql()
        self.__event_dao_api: IEventDaoApi = EventDaoApi()

    def update_ranking(self, afterDate : int, beforeDate : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Met à jour le classement

        Args:
            afterDate (int): La date unix a partir de laquelle rechercher les tournois.
            beforeDate (int): La date unix jusqu'à laquelle rechercher les tournois.
            videogame_id (int): id du jeu vidéo à mettre à jour
            coordonnees (str): coordonnees de la localisation des tournois à récupérer
            distance (str): distance de la localisation des tournois à récupérer

        Returns:
            dict[int, str]: en clé l'id du joueur et en valeur le rang du joueur

        Raises:
            HTTPError: Si la requête échoue.
        """
        # Récupère le jeu vidéo
        videogame = self.__videogame_dao_api.get_video_game_by_id(videogame_id)

        #Récupère la saison
        current_season = self.__season_dao_sql.get_current_season()

        # Envoyer la requête
        result = self.__tournament_dao_api.get_tournaments_by_location(afterDate, beforeDate, videogame, coordonnees, distance)

        # Récupère les événements de chaque tournoi
        events = self.__get_events(result)

        # Récupère les sets de chaque événement
        sets, complete_events = self.__get_sets_and_complete_events(events)

        # Met à jour le classement
        players = self.__player_dao_sql.get_all_players()
        ranking = Ranking(players.values())
        ranking.update_ranking(sets, videogame, current_season) 

        # Récupère le classement
        player_ranking = ranking.Players

        # Met à jour le nombre de tournois joués par chaque joueur
        for event in complete_events:
            for player in event.Players:
                if (player.Id in player_ranking):
                    player_ranking[player.Id].NbTournaments += 1

        # Met à jour le nombre de sets joués par chaque joueur
        # Players
        self.__player_dao_sql.remove_all_players()
        self.__player_dao_sql.add_players(player_ranking.values())

        # Elos        
        self.__elo_dao_sql.add_elos(player_ranking, videogame_id, beforeDate)

        return player_ranking
    
    def __get_events(self, tournaments : [Tournament]) -> [Event]:
        """
        Récupère les événements de chaque tournoi

        Args:
            tournaments ([Tournament]): Liste des tournois

        Returns:
            [Event]: Liste des événements
        """
        #Initialisation de la liste à renvoyer
        events = []
        for tournament in tournaments:
            #Récupère l'événement avec le plus d'entrants
            current_event_max_entrant = tournament.Events[0]
            for event in tournament.Events:
                if (event.NumEntrants > current_event_max_entrant.NumEntrants):
                    current_event_max_entrant = event
            #Ajoute l'événement à la liste
            events.append(current_event_max_entrant)
        return events
    
    def __get_sets_and_complete_events(self, events : [Event]) -> ([Set], [Event]):
        """
        Récupère les sets de chaque événement

        Args:
            events ([Event]): Liste des événements

        Returns:
            ([Set], [Event]): Liste des sets et liste des événements
        """
        #Initialisation des variables à renvoyer
        complete_events = []
        sets = []

        for event in events:
            page_courante = 0
            # Récupère les sets de l'événement
            res = self.__event_dao_api.get_event_by_id(event.Id, page_courante)
            complete_events.append(res)
            print(page_courante)

            while len(res.Sets) > 0:
                #Ajout des sets à la liste
                for set in res.Sets:
                    set.EventNbEntrants = event.NumEntrants
                    sets.append(set)

                #Récupération de la page suivante des sets de l'événement
                page_courante += 1
                res = self.__event_dao_api.get_event_by_id(event.Id, page_courante)

                #Ajout des événements complets à la liste
                if page_courante == 0:
                    complete_events.append(res)
                print(page_courante)
        return sets, complete_events