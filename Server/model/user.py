from model.entity import Entity
from typing import Optional

class User(Entity):

    def __init__(self, id: str, username: str, role: int, password: Optional[str] = None, userPP: Optional[str] = None):
        self.__id: int = id
        self.__username: str = username
        self.__role: int = role
        self.__password: str = password
        self.__userPP : str = userPP

    # region Properties

    @property
    def Id(self) -> int:
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Username(self) -> str:
        return self.__username
    
    @Username.setter
    def Username(self, username : str) -> None:
        self.__username = username

    @property
    def Role(self) -> int:
        return self.__role
    
    @Role.setter
    def Role(self, role : int) -> None:
        self.__role = role

    @property
    def Password(self) -> str:
        return self.__password
    
    @Password.setter
    def Password(self, password : str) -> None:
        self.__password = password

    @property
    def UserPP(self) -> str:
        return self.__userPP
    
    @UserPP.setter
    def UserPP(self, userPP : str) -> None:
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
            "password": self.Password,
            "userPP": self.UserPP
        }

