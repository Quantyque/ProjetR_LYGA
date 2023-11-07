from model.entity import Entity
from model.videogame import Videogame
from model.character import Character
from model.elo import Elo

class Player(Entity):
    """
    Represente un joueur
    """

    def __init__(self):
        self.__id : int = None
        self.__name : str = None
        self.__prefix : str = None
        self.__characters : [Character] = []
        self.__elos : dict[int, Elo] = {}
        self.__images : dict(str, str)= {
            "profile" : "",
            "banner" : ""
        }
        self.__external_urls : [str] = []
        self.__isDisqualified : bool = False
        self.__bio : str = None
        self.__nb_tournaments : int = 0

    # region Properties

    @property
    def Id(self) -> int:
        """
        Id du joueur
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Name(self) -> str:
        """
        Nom du joueur
        """
        return self.__name
    
    @Name.setter
    def Name(self, name : str) -> None:
        self.__name = name

    @property
    def Prefix(self) -> str:
        """
        Nom d'équipe du joueur
        """
        return self.__prefix
    
    @Prefix.setter
    def Prefix(self, prefix : str) -> None:
        self.__prefix = prefix

    @property
    def Characters(self) -> [Character]:
        """
        Liste des personnages joués par le joueur dans les derniers matchs
        """
        return self.__characters
    
    @Characters.setter
    def Characters(self, characters : [Character]) -> None:
        self.__characters = characters

    @property
    def Elos(self) -> dict[int, Elo]:
        """
        Liste des elos du joueur en fonction des jeux
        """
        return self.__elos
    
    @Elos.setter
    def Elos(self, elos : dict[int, Elo]) -> None:
        self.__elos = elos

    @property
    def Images(self) -> [str]:
        """
        Liste des images représentant le joueur
        """
        return self.__images
    
    @Images.setter
    def Images(self, images : [str]) -> None:
        self.__images = images

    @property
    def ExternalUrls(self) -> [str]:
        """
        Liste des urls des réseaux sociaux du joueur
        """
        return self.__external_urls
    
    @ExternalUrls.setter
    def ExternalUrls(self, external_urls : [str]) -> None:
        self.__external_urls = external_urls

    @property
    def IsDisqualified(self) -> bool:
        """
        Si le joueur est disqualifié ou non du tournoi
        """
        return self.__isDisqualified
    
    @IsDisqualified.setter
    def IsDisqualified(self, isDisqualified : bool) -> None:
        self.__isDisqualified = isDisqualified

    @property
    def Bio(self) -> str:
        """
        Biographie du joueur
        """
        return self.__bio
    
    @Bio.setter
    def Bio(self, bio : str) -> None:
        self.__bio = bio

    @property
    def NbTournaments(self) -> int:
        """
        Nombre de tournois auquel le joueur a participé
        """
        return self.__nb_tournaments
    
    @NbTournaments.setter
    def NbTournaments(self, nb_tournaments : int) -> None:
        self.__nb_tournaments = nb_tournaments

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "gamerTag" in data:
            self.Name = data["gamerTag"]
        if "prefix" in data:
            self.Prefix = data["prefix"]
        if "sets" in data: 
            for games in data["sets"]["nodes"]:
                if games["games"] != None:
                    videogame_data = games["event"]["videogame"]
                    videogame = Videogame()
                    videogame.hydrate(videogame_data)
                    for game in games["games"]:
                        for selection in game["selections"]:
                            if selection["entrant"]["standing"]["player"]["id"] == data["id"]:
                                chara_data = selection["character"]
                                chara_data["videogame"] = videogame
                                character = Character()
                                character.hydrate(chara_data)
                                self.Characters.append(character)
        if "user" in data:
            if data["user"] != None:
                if "authorizations" in data["user"]:
                    if data["user"]["authorizations"] != None:
                        for dataExternal in data["user"]["authorizations"]:
                            self.ExternalUrls.append(dataExternal["url"])
                if "images" in data["user"]:
                    if data["user"]["images"] != None:
                        for dataImages in data["user"]["images"]:
                            self.Images[dataImages["type"]] = dataImages["url"]
                if "bio" in data["user"]:
                    self.Bio = data["user"]["bio"]

        if "isDisqualified" in data:
            self.IsDisqualified = data["isDisqualified"]
        if "nbTournaments" in data:
            self.NbTournaments = data["nbTournaments"]


    def toJSON(self):
        elos = {}
        for elo in self.Elos:
            elos[elo] = self.Elos[elo].toJSON()
        json = {
            "id": self.Id,
            "name": self.Name,
            "prefix": self.Prefix,
            "elos": elos,
            "images": self.Images,
            "external_urls": [
                external_url for external_url in self.ExternalUrls
            ],
            "bio": self.Bio,
            "nb_tournaments": self.NbTournaments,
        }
        return json

    # endregion