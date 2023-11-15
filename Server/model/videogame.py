from model.entity import Entity
from model.character import Character

class Videogame(Entity):
    """
    Représente un jeu vidéo
    """

    def __init__(self):
        self.__id : int = None
        self.__name : str = None
        self.__characters : [Character] = []
        self.__images : [str] = []

    # region Properties
    @property
    def Id(self) -> int:
        """
        Récupère l'id du jeu vidéo

        Returns:
            int: Id du jeu vidéo
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        """
        Setter de l'id du jeu vidéo

        Args:
            id (int): Nouvel id du jeu vidéo
        """
        self.__id = id

    @property
    def Name(self) -> str:
        """
        Getter du nom du jeu vidéo

        Returns:
            str: Nom du jeu vidéo
        """
        return self.__name
    
    @Name.setter
    def Name(self, name : str) -> None:
        """
        Setter du nom du jeu vidéo

        Args:
            name (str): Nouveau nom du jeu vidéo
        """
        self.__name = name

    @property
    def Characters(self) -> [Character]:
        """
        Getter de la liste des personnages jouables dans le jeu

        Returns:
            [Character]: Liste des personnages jouables dans le jeu
        """
        return self.__characters
    
    @Characters.setter
    def Characters(self, characters : [Character]) -> None:
        """
        Setter de la liste des personnages jouables dans le jeu

        Args:
            characters ([Character]): Nouvelle liste des personnages jouables dans le jeu
        """
        self.__characters = characters

    @property
    def Images(self) -> [str]:
        """
        Getter de la liste des images représentant le jeu

        Returns:
            [str]: Liste des images représentant le jeu
        """
        return self.__images
    
    @Images.setter
    def Images(self, images : [str]) -> None:
        """
        Setter de la liste des images représentant le jeu

        Args:
            images ([str]): Nouvelle liste des images représentant le jeu
        """
        self.__images = images

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = int(data["id"])
        if "name" in data:
            self.Name = data["name"]
        if "characters" in data:
            if data["characters"] is not None:
                for character in data["characters"]:   
                    ch = Character()
                    ch.hydrate(character)
                    self.Characters.append(ch)
        if "images" in data:
            for image in data["images"]:
                 self.Images.append(image["url"])

    def toJSON(self):
        json = {
            "id": self.Id,
            "name": self.Name,
            "characters": [
                character.toJSON() for character in self.Characters
            ],
            "images": self.Images
        }
        return json
        

    # endregion