from model.entity import Entity

class Character(Entity):
    """
    Représente un personnage jouable dans un jeu vidéo
    """

    def __init__(self):
        self.__id : int = None
        self.__name : str = None
        self.__images : [str] = []

    # region Properties

    @property
    def Id(self) -> int:
        """
        Id du personnage
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Name(self) -> str:
        """
        Nom du personnage
        """
        return self.__name
    
    @Name.setter
    def Name(self, name : str) -> None:
        self.__name = name

    @property
    def Images(self) -> [str]:
        """
        Images du personnage
        """
        return self.__images
    
    @Images.setter
    def Images(self, images : [str]) -> None:
        self.__images = images

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "name" in data:
            self.Name = data["name"]
        if "images" in data:
            if data["images"] != None:
                for dataImages in data["images"]:
                    self.Images.append(dataImages["url"])

    def toJSON(self):
        json = {
            "id" : self.Id,
            "name" : self.Name,
            "images" : [
                image for image in self.Images
            ],
        }
        return json

    # endregion