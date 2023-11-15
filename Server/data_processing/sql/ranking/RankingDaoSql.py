from data_processing.sql.ranking.IRankingDaoSql import IRankingDaoSql
from data_processing.api.startgg.tournament.TournamentDaoApi import TournamentDaoApi
from data_processing.api.startgg.event.EventDaoApi import EventDaoApi
from data_processing.sql.video_game.VideoGameSql import VideoGameDaoSql
from data_processing.api.startgg.player.PlayerDaoApi import PlayerDaoApi
from data_processing.sql.elo.EloDaoSql import EloDaoSql
from model.ranking import Ranking
from data_processing.sql.dao import Dao
from typing import Dict
import datetime

class RankingDaoSql(IRankingDaoSql, Dao):

    def __init__(self):
        super().__init__()

    def update_ranking(self, date : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Met à jour le classement

        Args:
            date (int): date
            videogame_id (int): videogame's id
            coordonnees (str): coordinates
            distance (str): distance

        Returns:
            dict[int, str]: in key the player's id and in value the player himself

        Raises:
            HTTPError: Si la requête échoue.
        """
        # Initialise les DAO
        tournament_dao = TournamentDaoApi()
        event_dao = EventDaoApi()
        videogame_dao = VideoGameDaoSql()
        player_dao = PlayerDaoApi()
        elo_dao = EloDaoSql()

        # Récupère le jeu vidéo
        videogame = videogame_dao.get_video_game_by_id(videogame_id)

        # Envoyer la requête
        result = tournament_dao.get_tournaments_by_location(date, videogame, coordonnees, distance)

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
            res = event_dao.get_event_by_id(event.Id, page_courante)
            complete_events.append(res)
            print(page_courante)
            while len(res.Sets) > 0:
                for set in res.Sets:
                    set.EventNbEntrants = event.NumEntrants
                    sets.append(set)
                page_courante += 1
                res = event_dao.get_event_by_id(event.Id, page_courante)
                if page_courante == 0:
                    complete_events.append(res)
                print(page_courante)

        # Met à jour le classement
        players = player_dao.get_all_players()
        ranking = Ranking(players.values())
        ranking.update_ranking(sets, videogame) 

        # Récupère le classement
        player_ranking = ranking.Players

        # Met à jour le nombre de tournois joués par chaque joueur
        for event in complete_events:
            for player in event.Players:
                if (player.Id in player_ranking):
                    player_ranking[player.Id].NbTournaments += 1

        # Met à jour le nombre de sets joués par chaque joueur
        # Players
        player_dao.remove_all_players()
        player_dao.add_players(player_ranking.values())

        # Elos
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        elo_dao.add_elos(player_ranking, videogame_id, date)

        # Video games
        videogame_dao.delete_audited_game(videogame)
        videogame_dao.add_audited_game(videogame)

        return player_ranking