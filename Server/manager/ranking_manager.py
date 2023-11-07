from model.ranking import Ranking
from manager.manager import Manager
from manager.tournament_manager import TournamentManager
from manager.event_manager import EventManager
from manager.video_game_manager import VideoGameManager
from manager.player_manager import PlayerManager
from manager.elo_manager import EloManager
import datetime

class RankingManager(Manager):
    """
    Classe permettant de gérer le ranking
    """

    def __init__(self):
        super().__init__()

    # region Operations

    def update_ranking(self, date : int, videogame_id : int, coordonnees : str, distance : str) -> dict[int, str]:
        """
        Met à jour le ranking

        Args:
            date (int): la date à partir de laquelle on veut récupérer les tournois
            videogame_id (int): l'id du jeu-vidéo
            coordonnees (str): les coordonnées de la ville
            distance (str): la distance autour de la ville

        Returns:
            dict[int, str]: en clé l'id du joueur et en valeur le joueur en lui-même
        """
        #Initialisation des variables
        tournament_manager = TournamentManager()
        event_manager = EventManager()
        videogame_manager = VideoGameManager()
        player_manager = PlayerManager()
        elo_manager = EloManager()

        #Récupération du jeu-vidéo selectionné
        videogame = videogame_manager.get_video_game_by_id(videogame_id)

        #Envoi de la requête pour obtenir les tournois en fonction de la date et du jeu
        result = tournament_manager.get_tournaments_by_location(date, videogame, coordonnees, distance)

        #Tri des tournois événements des tournois pour obtenir que les brackets principaux
        events = []
        for tournament in result:
            current_event_max_entrant = tournament.Events[0]
            for event in tournament.Events:
                if (event.NumEntrants > current_event_max_entrant.NumEntrants):
                    current_event_max_entrant = event
            events.append(current_event_max_entrant)

        #Récupération des sets de chaque tournoi pour les inverser et obtenir les sets dans l'ordre joué
        complete_events = []
        sets = []
        for event in events:
            page_courante = 0
            res = event_manager.get_event_by_id(event.Id, page_courante)
            complete_events.append(res)
            print(page_courante)
            while len(res.Sets) > 0:
                for set in res.Sets:
                    set.EventNbEntrants = event.NumEntrants
                    sets.append(set)
                page_courante += 1
                res = event_manager.get_event_by_id(event.Id, page_courante)
                if page_courante == 0:
                    complete_events.append(res)
                print(page_courante)

        #Mise à jour de l'élo en fonction des sets récupérés
        players = player_manager.get_all_players()
        ranking = Ranking(players.values())
        ranking.update_ranking(sets, videogame) 

        #Récupération des élos des joueurs
        player_ranking = ranking.Players

        #Mise à jour du nombre de tournois joués par les joueurs
        for event in complete_events:
            for player in event.Players:
                if (player.Id in player_ranking):
                    player_ranking[player.Id].NbTournaments += 1

        #Mise à jour de la base de données en fonction des résultats
        #Joueurs
        player_manager.remove_all_players()
        player_manager.add_players(player_ranking.values())

        #Elos
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        elo_manager.add_elos(player_ranking, videogame_id, date)

        #Jeu-vidéo
        videogame_manager.delete_audited_game(videogame)
        videogame_manager.add_audited_game(videogame)

        return player_ranking

    #endregion