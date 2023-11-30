from model.entity import Entity
from typing import Optional
from model.role import Role

class User(Entity):
    """
    Représente un utilisateur de l'application
    """

    def __init__(self, id: str, username: str, role: Role, password: Optional[str] = None, userPP: Optional[str] = None):
        self.__id: int = id
        self.__username: str = username
        self.__role: Role = role
        self.__password: str = password
        self.__userPP : str = userPP

    # region Properties

    @property
    def Id(self) -> int:
        """
        Getter de l'id de l'utilisateur

        Returns:
            int: Id de l'utilisateur
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        """
        Setter de l'id de l'utilisateur

        Args:
            id (int): Nouvel id de l'utilisateur
        """
        self.__id = id

    @property
    def Username(self) -> str:
        """
        Getter du nom d'utilisateur

        Returns:
            str: Nom d'utilisateur
        """
        return self.__username
    
    @Username.setter
    def Username(self, username : str) -> None:
        """
        Setter du nom d'utilisateur

        Args:
            username (str): Nouveau nom d'utilisateur
        """
        self.__username = username

    @property
    def Role(self) -> int:
        """
        Getter du rôle de l'utilisateur en fonction de l'énumération Role

        Returns:
            int: Numéro du rôle de l'utilisateur en fonction de l'énumération Role
        """
        return self.__role
    
    @Role.setter
    def Role(self, role : int) -> None:
        """
        Setter du rôle de l'utilisateur en fonction de l'énumération Role

        Args:
            role (int): Nouveau rôle de l'utilisateur en fonction de l'énumération Role
        """
        self.__role = role

    @property
    def Password(self) -> str:
        """
        Getter du mot de passe de l'utilisateur

        Returns:
            str: Mot de passe de l'utilisateur
        """
        return self.__password
    
    @Password.setter
    def Password(self, password : str) -> None:
        """
        Setter du mot de passe de l'utilisateur

        Args:
            password (str): Nouveau mot de passe de l'utilisateur
        """
        self.__password = password

    @property
    def UserPP(self) -> str:
        """
        Getter de l'url de l'avatar de l'utilisateur

        Returns:
            str: Url de l'avatar de l'utilisateur
        """
        return self.__userPP
    
    @UserPP.setter
    def UserPP(self, userPP : str) -> None:
        """
        Setter de l'url de l'avatar de l'utilisateur

        Args:
            userPP (str): Nouvelle url de l'avatar de l'utilisateur
        """
        self.__userPP = userPP

    # endregion

    def hydrate(self, data: dict):
        if "id" in data:
            self.Id = data["id"]
        if "username" in data:
            self.Username = data["username"]
        if "role" in data:
            self.Role = data["role"]
        if "password" in data:
            self.Password = data["password"]
        if "userPP" in data:
            self.UserPP = data["userPP"]
    
    def toJSON(self):
        return {
            "id": self.Id,
            "username": self.Username,
            "role": self.Role,
            "userPP": self.UserPP
        }

