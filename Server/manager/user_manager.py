from model.user import User
from data_processing.sql.user.UserDao import UserDao as UserDaoSQL
from data_processing.sql.user.IUserDao import IUserDao as IUserDaoSQL
import bcrypt, pyotp

class UserManager(): 
    """
    Classe permettant de gérer les utilisateurs
    """

    def __init__(self):
        self.__db: IUserDaoSQL = UserDaoSQL()

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

        return self.__db.get_all_users()

    def get_user_by_id(self, user: User):
        
        return self.__db.get_user_by_id(user)

    def add_user(self, user: User):
        
        return self.__db.add_user(user)

    def update_user(self, user: User):
        
        return self.__db.update_user(user)

    def delete_user(self, id: int):
        
        return self.__db.delete_user(id)

    # endregion