from model.entity import Entity
from model.videogame import Videogame

class Elo(Entity):
    """
    Represente l'elo d'un joueur dans un jeu
    """

    def __init__(self):
        self.__id : int = None
        self.__score : int = None
        self.__videogame : Videogame = None
        self.__date : int = None

    # region Properties

    @property
    def Id(self) -> int:
        """
        Id de l'elo
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Score(self) -> int:
        """
        Score de l'élo
        """
        return self.__score
    
    @Score.setter
    def Score(self, score : int) -> None:
        self.__score = score

    @property
    def Videogame(self):
        """
        Jeu vidéo lié à l'élo
        """
        return self.__videogame
    
    @Videogame.setter
    def Videogame(self, videogame) -> None:
        self.__videogame = videogame

    @property
    def Date(self):
        """
        Date de l'élo
        """
        return self.__date
    
    @Date.setter
    def Date(self, date) -> None:
        self.__date = date

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "score" in data:
            self.Score = data["score"]
        if "videogame" in data:
            videogame = Videogame()
            videogame.hydrate(data["videogame"])
            self.Videogame = videogame
        if "date" in data:
            self.Date = data["date"]

    def toJSON(self):
        json = {
            "id": self.Id,
            "score": self.Score,
            "videogame": self.Videogame.toJSON() if self.Videogame is not None else "",
            "date" : self.Date
        }
        return json

    # endregion
