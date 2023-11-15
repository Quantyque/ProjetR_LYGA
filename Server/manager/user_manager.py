from model.user import User
from data_processing.sql.user.UserDaoSql import UserDaoSql
from data_processing.sql.user.IUserDaoSql import IUserDaoSql
import bcrypt, pyotp

class UserManager(): 
    """
    Classe permettant de gérer les utilisateurs
    """

    def __init__(self):
        self.__db: IUserDaoSql = UserDaoSql()

    # region Operations

    def register(self, username: str, password: str) -> None:
        """
        Inscrit un utilisateur.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.

        Raises:
            DuplicateUser: Si l'utilisateur existe déjà.
        """
        return self.__db.register(username, password)


    def login(self, username: str, password: str) -> list(str()):
        """
        Connecte un utilisateur.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.

        Returns:
            list(str()): Le token et le secret.
    
        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
            InvalidPassword: Si le mot de passe est incorrect.
        """
        return self.__db.login(username, password)

    def get_all_users(self):
        """
        Retourne tous les utilisateurs

        Returns:
            list(User): La liste des utilisateurs

        Raises:
            HTTPError: Si la requête échoue.
        """

        return self.__db.get_all_users()

    def get_user_by_id(self, id: int):
        """
        Retourne un utilisateur en fonction de son id

        Args:
            user (User): L'utilisateur à récupérer

        Returns:
            User: L'utilisateur correspondant à l'id

        Raises:
            HTTPError: Si la requête échoue.
        """
        
        return self.__db.get_user_by_id(id)

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
        
        return self.__db.update_user(user)

    def delete_user(self, id: int):
        """
        Supprime un utilisateur.

        Args:
            id (int): L'id de l'utilisateur à supprimer.

        Returns:
            None

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """
        
        return self.__db.delete_user(id)

    # endregion