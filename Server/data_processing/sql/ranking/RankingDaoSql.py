from data_processing.sql.ranking.IRankingDaoSql import IRankingDaoSql
from data_processing.api.startgg.tournament.TournamentDaoApi import TournamentDaoApi
from data_processing.api.startgg.event.EventDaoApi import EventDaoApi
from data_processing.api.startgg.video_game.VideoGameDaoApi import VideoGameDaoApi
from data_processing.sql.video_game.VideoGameSql import VideoGameDaoSql
from data_processing.sql.player.PlayerDaoSql import PlayerDaoSql
from data_processing.sql.elo.EloDaoSql import EloDaoSql
from data_processing.sql.season.SeasonDaoSql import SeasonDaoSql
from model.ranking import Ranking
from data_processing.sql.dao import Dao
from typing import Dict

class RankingDaoSql(IRankingDaoSql, Dao):

    def __init__(self):
        super().__init__()

    def update_ranking(self, afterDate : int, beforeDate : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Met à jour le classement

        Args:
            afterDate (int): date depuis laquelle on veut récupérer les tournois
            beforeDate (int): date jusqu'à laquelle on veut récupérer les tournois
            videogame_id (int): id du jeu vidéo à mettre à jour
            coordonnees (str): coordonnees de la localisation des tournois à récupérer
            distance (str): distance de la localisation des tournois à récupérer

        Returns:
            dict[int, str]: en clé l'id du joueur et en valeur le rang du joueur

        Raises:
            HTTPError: Si la requête échoue.
        """
        # Initialise les DAO
        tournament_dao_api = TournamentDaoApi()
        event_dao_api = EventDaoApi()
        videogame_dao_api = VideoGameDaoApi()
        videogame_dao_sql = VideoGameDaoSql()
        season_dao_sql = SeasonDaoSql()
        player_dao_sql = PlayerDaoSql()
        elo_dao_sql = EloDaoSql()

        # Récupère le jeu vidéo
        videogame = videogame_dao_api.get_video_game_by_id(videogame_id)

        #Récupère la saison
        current_season = season_dao_sql.get_current_season()

        # Envoyer la requête
        result = tournament_dao_api.get_tournaments_by_location(afterDate, beforeDate, videogame, coordonnees, distance)

        # Récupère les événements de chaque tournoi
        events = []
        for tournament in result:
            current_event_max_entrant = tournament.Events[0]
            for event in tournament.Events:
                if (event.NumEntrants > current_event_max_entrant.NumEntrants):
                    current_event_max_entrant = event
            events.append(current_event_max_entrant)

        # Récupère les sets de chaque événement
        complete_events = []
        sets = []
        for event in events:
            page_courante = 0
            res = event_dao_api.get_event_by_id(event.Id, page_courante)
            complete_events.append(res)
            print(page_courante)
            while len(res.Sets) > 0:
                for set in res.Sets:
                    set.EventNbEntrants = event.NumEntrants
                    sets.append(set)
                page_courante += 1
                res = event_dao_api.get_event_by_id(event.Id, page_courante)
                if page_courante == 0:
                    complete_events.append(res)
                print(page_courante)

        # Met à jour le classement
        players = player_dao_sql.get_all_players()
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
        player_dao_sql.remove_all_players()
        player_dao_sql.add_players(player_ranking.values())

        # Elos        
        elo_dao_sql.add_elos(player_ranking, videogame_id, beforeDate)

        # Video games
        videogame_dao_sql.delete_audited_game(videogame)
        videogame_dao_sql.add_audited_game(videogame)

        return player_ranking