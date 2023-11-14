from model.player import Player
from model.set import Set
from model.elo import Elo
import functools
from constants import LOSER_RUN_FACTOR
from model.videogame import Videogame
from manager.elo_manager import EloManager

class Ranking():
    """
    Permet de gérer le classement des joueurs
    """

    def __init__(self, players : [Player] = None):
        self.__players : [Player] = {}
        self.__elo_manager = EloManager()
        for player in players:
            self.__players[player.Id] = player

    # region Properties

    @property
    def Players(self) -> [Player]:
        """
        Getter de la liste des joueurs avec en clé leur id

        Returns:
            [Player]: Liste des joueurs avec en clé leur id
        """
        return self.__players
    
    @Players.setter
    def Players(self, players : [Player]) -> None:
        """
        Setter de la liste des joueurs avec en clé leur id

        Args:
            players ([Player]): Nouvelle liste des joueurs avec en clé leur id
        """
        self.__players = players

    # endregion

    # region Operations

    def init_players(self, player : Player, videogame : Videogame) -> Player:
        """
        Initialise les joueurs

        Si le joueur n'a pas encore joué, on lui attribue un elo de 1000

        Args:
            player (Player): Joueur
            videogame (Videogame): Jeu vidéo à initialiser

        Returns:
            Player: Joueur initialisé
        """
        #Création du joueur s'il n'est pas encore dans le dictionnaire des joueurs
        if player.Id not in self.Players:
            default_elo = self.__elo_manager.get_default_elo(player.Id, videogame.Id)
            data_elo = {"score" : default_elo}
            elo = Elo()
            elo.hydrate(data_elo)
            elo.Videogame = videogame
            player.Elos[videogame.Id] = elo
            self.Players[player.Id] = player
        #Récupération du joueur s'il est déjà dans le dictionnaire des joueurs
        else:
            player = self.Players[player.Id]
        return player

    def get_expected_score(self, player : Player, opponent : Player, videogameId : int) -> float:
        """
        Calcule pour connaitre la chance de gagner d'un joueur contre un autre en fonction de leur elo

        Args:
            player (Player): Joueur
            opponent (Player): Adversaire
            videogameId (int): Id du jeu vidéo concerné par le calcul de l'élo

        Returns:
            float: Chance de gagner du joueur
        """
        return 1 / (1 + 10 ** ((opponent.Elos[videogameId].Score - player.Elos[videogameId].Score) / 400))
    
    def get_new_elo(self, winner : Player, looser : Player, set : Set, videogameId : int) -> (float, float):
        """
        Calcule le nouvel elo d'un joueur

        Args:
            winner (Player): Joueur gagnant
            looser (Player): Joueur perdant
            set (Set): Set concerné
            videogameId (int): Id du jeu vidéo concerné par le calcul de l'élo

        Returns:
            (float, float): Nouvel elo du gagnant puis du perdant
        """
        #Initialisation des variables pour le calcul de l'élo
        expected_a = self.get_expected_score(winner, looser, videogameId)
        expected_b = self.get_expected_score(looser, winner, videogameId)
        facteur_round = 1
        facteur_k = set.EventNbEntrants
        if set.Round <0:
            facteur_round = LOSER_RUN_FACTOR
        #Calcul de l'élo
        return winner.Elos[videogameId].Score + (facteur_k * (1 - expected_a))*facteur_round, looser.Elos[videogameId].Score + (facteur_k * (0 - expected_b))*facteur_round

    def update_ranking(self, sets : [Set], videogame : Videogame) -> None:
        """
        Met à jour le classement des joueurs

        Args:
            sets ([Set]): Liste des sets joués
            videogame (Videogame): Jeu vidéo concerné
        """
        reverse_sets = sets[::-1]
        for set in reverse_sets:
            #Verification qu'aucun des joueurs n'est disqualifié
            if (set.Players[0].IsDisqualified == None and set.Players[1].IsDisqualified == None):
                #Initialisation de l'élo des joueurs si ils n'ont pas encore joué
                player_a = set.Players[0]
                player_b = set.Players[1]
                player_a = self.init_players(player_a, videogame)
                player_b = self.init_players(player_b, videogame)

                winner, looser = set.get_winner_looser(player_a, player_b)

                #Calcul de l'élo
                winner.Elos[videogame.Id].Score, looser.Elos[videogame.Id].Score = self.get_new_elo(winner, looser, set, videogame.Id)

                #Ajout des joueurs dans le dictionnaire
                self.Players[winner.Id] = winner
                self.Players[looser.Id] = looser

        #Tri des joueurs en fonction de leur élo
        custom_sort = functools.partial(lambda item, param: item[1].Elos[param].Score, param=videogame.Id)
        self.Players = dict(sorted(self.Players.items(), key=custom_sort, reverse=True))

    # endregion
