from model.user import User
from abc import ABC, abstractmethod

class IUserDaoSql(ABC):

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

    def admin_register(self, username: str, password: str, role: int) -> None:
        """
        Enregistre un nouvel utilisateur avec un role (ADMIN).
        
        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.
            role (int): Le rôle de l'utilisateur.
            
        Returns:
            None
            
        Raises:
            DuplicateUser: Si l'utilisateur existe déjà.    
        """

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
    def get_all_users(self) -> [User]:
        """
        Retourne tous les utilisateurs

        Returns:
            list(User): La liste des utilisateurs

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod 
    def get_user_by_id(self, id: int) -> User:
        """
        Retourne un utilisateur en fonction de son id

        Args:
            user (User): L'utilisateur à récupérer

        Returns:
            User: L'utilisateur correspondant à l'id

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """
        pass

    @abstractmethod
    def update_user(self, user: User):
        """
        Met à jour un utilisateur.

        Args:
            user (User): L'utilisateur à mettre à jour.

        Returns:
            None

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """
        pass
    
    @abstractmethod
    def delete_user(self, id: int):
        """
        Supprime un utilisateur.

        Args:
            id (int): L'id de l'utilisateur.

        Returns:
            None

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """
        pass

    @abstractmethod
    def get_roles(self):
        """
        Retourne les rôles.

        Returns:
            list(str()): La liste des rôles.
        """
        pass