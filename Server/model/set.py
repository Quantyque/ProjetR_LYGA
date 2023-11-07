from model.entity import Entity
from model.player import Player
from model.game import Game
from model.videogame import Videogame

class Set(Entity):
    """
    Represente un set
    """

    def __init__(self):
        self.__id : int = None
        self.__round : int = None
        self.__winner_id : int = None
        self.__players : [Player] = []
        self.__event_nb_entrants : int = None
        self.__date : int = None
        self.__games : [Game] = []
        self.__videogame : Videogame = None

    # region Properties

    @property
    def Id(self) -> int:
        """
        Id du set
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Round(self) -> int:
        """
        Round du set dans le tournoi (négatif si le set est en loser bracket)
        """
        return self.__round
    
    @Round.setter
    def Round(self, round : int) -> None:
        self.__round = round

    @property
    def WinnerId(self) -> int:
        """
        Id du gagnant du set
        """
        return self.__winner_id
    
    @WinnerId.setter
    def WinnerId(self, winner_id : int) -> None:
        self.__winner_id = winner_id

    @property
    def Players(self) -> [Player]:
        """
        Liste des joueurs ayant participé au set
        """
        return self.__players
    
    @Players.setter
    def Players(self, players : [Player]) -> None:
        self.__players = players

    @property
    def EventNbEntrants(self) -> int:
        """
        Nombre d'entrants à l'événement auquel appartient le set
        """
        return self.__event_nb_entrants
    
    @EventNbEntrants.setter
    def EventNbEntrants(self, event_nb_entrants : int) -> None:
        self.__event_nb_entrants = event_nb_entrants

    @property
    def Date(self) -> int:
        """
        Date du set
        """
        return self.__date
    
    @Date.setter
    def Date(self, date : int) -> None:
        self.__date = date

    @property
    def Games(self) -> [Game]:
        """
        Liste des matchs du set
        """
        return self.__games
    
    @Games.setter
    def Games(self, games : [Game]) -> None:
        self.__games = games

    @property
    def Videogame(self) -> Videogame:
        """
        Jeu-vidéo du set
        """
        return self.__videogame
    
    @Videogame.setter
    def Videogame(self, videogame : Videogame) -> None:
        self.__videogame = videogame

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "round" in data:
            self.Round = data["round"]
        if "slots" in data:
            for slot in data["slots"]:
                isDisqualified = slot["entrant"]["isDisqualified"]
                dataplayer = slot["entrant"]["standing"]["player"]
                dataplayer["isDisqualified"] = isDisqualified
                if (slot["entrant"]["id"] == data["winnerId"]):
                    self.WinnerId = dataplayer["id"]
                player = Player()
                player.hydrate(dataplayer)
                self.Players.append(player)
        if "completedAt" in data:
            self.Date = data["completedAt"]
        if "games" in data:
            if data["games"] != None:
                for datagame in data["games"]:
                    game = Game()
                    game.hydrate(datagame)
                    self.Games.append(game)
        if "completedAt" in data:
            self.Date = data["completedAt"]
        if "event" in data:
            if data["event"] != None:
                if "videogame" in data["event"]:
                    if data["event"]["videogame"] != None:
                        videogame = Videogame()
                        videogame.hydrate(data["event"]["videogame"])
                        self.Videogame = videogame

    def get_winner_looser(self, player1 : Player, player2 : Player) : #(Player, Player):
        """
        Renvoie le gagnant et le perdant du set

        Args:
            player1 (Player): le premier joueur
            player2 (Player): le second joueur

        Returns:
            Player, Player: le gagnant et le perdant
        """
        if player1.Id == self.WinnerId:
            return player1, player2
        else:
            return player2, player1
        
    def toJSON(self):
        json = {
            "id": self.Id,
            "round": self.Round,
            "winner_id": self.WinnerId,
            "players": [
                player.toJSON() for player in self.Players
            ],
            "event_nb_entrants": self.EventNbEntrants,
            "games": [
                game.toJSON() for game in self.Games
            ], 
            "date": self.Date,
            "videogame": self.Videogame.toJSON() if self.Videogame != None else None
        }
        return json

    # endregion
