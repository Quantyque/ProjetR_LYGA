from model.user import User
from abc import ABC, abstractmethod

class IUserDao(ABC):

    @abstractmethod
    def register(self, username: str, password: str) -> None:
        """
        Enregistre un nouvel utilisateur.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.

        Returns:
            None

        Raises:
            DuplicateUser: Si l'utilisateur existe déjà.
        """
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> list(str()):
        """
        Connecte un utilisateur.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.

        Returns:
            list(str()): Le token de connexion.

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
            InvalidPassword: Si le mot de passe est incorrect.
        """
        pass

    @abstractmethod 
    def get_all_users(self):
        pass

    @abstractmethod 
    def get_user_by_id(self, user: User):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass
    
    @abstractmethod
    def delete_user(self, id: int):
        pass