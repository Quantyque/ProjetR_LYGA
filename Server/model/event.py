from model.entity import Entity
from model.set import Set
from model.player import Player
from model.videogame import Videogame

class Event(Entity):
    """
    Représente un événement d'un tournoi
    """

    def __init__(self):
        self.__id : int = None
        self.__name : str = None
        self.__num_entrants : int = None
        self.__players : [Player] = []
        self.__sets : [Set] = []
        self.__videogame : Videogame = None

    # region Properties
    @property
    def Id(self) -> int:
        """
        Id de l'événement
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Name(self) -> str:
        """
        Nom de l'événement
        """
        return self.__name
    
    @Name.setter
    def Name(self, name : str) -> None:
        self.__name = name

    @property
    def NumEntrants(self) -> int:
        """
        Nombre d'entrants à l'événement
        """
        return self.__num_entrants
    
    @NumEntrants.setter
    def NumEntrants(self, num_entrants : int) -> None:
        self.__num_entrants = num_entrants

    @property
    def Sets(self) -> [Set]:
        """
        Liste des sets de l'événement
        """
        return self.__sets
    
    @Sets.setter
    def Sets(self, sets : [Set]) -> None:
        self.__sets = sets

    @property
    def Videogame(self):
        """
        Jeu vidéo lié à l'événement
        """
        return self.__videogame
    
    @Videogame.setter
    def Videogame(self, videogame):
        self.__videogame = videogame

    @property
    def Players(self) -> [Player]:
        """
        Liste des joueurs de l'événement
        """
        return self.__players
    
    @Players.setter
    def Players(self, players : [Player]) -> None:
        self.__players = players

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "name" in data:
            self.Name = data["name"]
        if "numEntrants" in data:
            self.NumEntrants = data["numEntrants"]
        if "sets" in data:
            for data_set in data["sets"]["nodes"]:
                set = Set()
                set.hydrate(data_set)
                self.Sets.append(set)
        if "videogame" in data:
            videogame = Videogame()
            videogame.hydrate(data["videogame"])
            self.Videogame = videogame
        if "entrants" in data:
            for entrant in data["entrants"]["nodes"]:
                player = Player()
                player.hydrate(entrant["standing"]["player"])
                self.Players.append(player)

    def toJSON(self):
        json = {
            "id": self.Id,
            "name": self.Name,
            "numEntrants": self.NumEntrants,
            "sets": [
                set.toJSON() for set in self.Sets
            ],
            "videogame": self.Videogame.toJSON() if self.Videogame is not None else ""
        }
        return json

    # endregion