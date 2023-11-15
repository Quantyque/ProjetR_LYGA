from data_processing.sql.user.IUserDaoSql import IUserDaoSql
from exceptions import InvalidCredentials, UserNotFound
from datetime import timedelta, datetime
from model.user import User
from model.role import Role
from data_processing.sql.dao import Dao
import jwt, bcrypt, os, json, bcrypt, pyotp

class UserDaoSql(IUserDaoSql, Dao):
        
    def __init__(self):
        super().__init__()

    # region Operations

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

        user_infos = self.db.exec_request("SELECT * FROM Users WHERE username = ?", (username,), True)

        if user_infos is not None:
            raise InvalidCredentials("Username already taken.")

        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(None, username, Role.USER.value, password, None)
        self.db.exec_request("INSERT INTO Users(username, password, role) VALUES (?, ?, ?)", (user.Username, user.Password, user.Role))

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

        result: str = ""

        user_infos = self.db.exec_request("SELECT * FROM Users WHERE username = ?", (username,), True)

        if user_infos is not None:
            user = User(user_infos[0], user_infos[1], user_infos[3], None, user_infos[4])
            user_password = user_infos[2]
        else:
            raise InvalidCredentials("Invalid credentials.")

        if bcrypt.checkpw(password.encode('utf-8'), user_password.encode('utf-8')):

            exp = datetime.now() + timedelta(hours=8) 
            payload = user.toJSON()
            payload["exp"] = exp.timestamp()   
            jwt_encoded = jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm=os.getenv('JWT_ALGO'))
            user_json = user.toJSON()
            user_json["accessToken"] = jwt_encoded
            result = json.dumps(user_json)

        else:
            raise InvalidCredentials("Invalid credentials.")
        
        return result
            

    def get_all_users(self):
        """
        Retourne tous les utilisateurs

        Returns:
            list(User): La liste des utilisateurs

        Raises:
            HTTPError: Si la requête échoue.
        """

        users = self.db.exec_request("SELECT * FROM Users")

        if users is not None:
            users = [User(user[0], user[1], user[3], None, user[4]) for user in users]
            json_users = [user.toJSON() for user in users]
            
        else:
            raise Exception("Invalid credentials.")
        
        return json_users
        

    def get_user_by_id(self, id: int):
        """
        Retourne un utilisateur en fonction de son id

        Args:
            user (User): L'utilisateur à récupérer

        Returns:
            User: L'utilisateur correspondant à l'id

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """

        data = self.db.exec_request("SELECT * FROM Users WHERE id = ?", (id,))

        if data:
            user = data[0]
            user = User(user[0], user[1], user[3], None, user[4])
            json_user = user.toJSON()

        else:
            raise UserNotFound("User not found.")
        
        return json_user

    def update_user(self, user: User) -> None:
        """
        Met à jour un utilisateur.

        Args:
            user (User): L'utilisateur à mettre à jour.

        Returns:
            None

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """

        user_infos = self.db.exec_request("SELECT * FROM Users WHERE username = ?", (user.Id,), True)

        if user_infos is None:
            raise UserNotFound("User not found.")

        if user.Password is not None:
            password = bcrypt.hashpw(user.Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.db.exec_request("UPDATE Users SET username = ?, password = ?, role = ?, userPP = ? WHERE id = ?", (user.Username, password, user.Role, user.UserPP, user.Id))

        else:
            self.db.exec_request("UPDATE Users SET username = ?, role = ?, userPP = ? WHERE id = ?", (user.Username, user.Role, user.UserPP, user.Id))

    def delete_user(self, id: int) -> None:
        """
        Supprime un utilisateur.

        Args:
            id (int): L'id de l'utilisateur.

        Returns:
            None

        Raises:
            UserNotFound: Si l'utilisateur n'existe pas.
        """
        
        user_infos = self.db.exec_request("SELECT * FROM Users WHERE id = ?", (id,), True)

        if user_infos is None:
            raise UserNotFound("User not found.")

        self.db.exec_request("DELETE FROM Users WHERE id = ?", (id,))

    # endregion