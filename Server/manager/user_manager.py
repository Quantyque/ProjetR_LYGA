from manager.manager import Manager
from model.user import User
from exceptions import InvalidCredentials
from datetime import timedelta, datetime
from model.role import Role
import jwt, bcrypt, os, json, bcrypt, pyotp

class UserManager(Manager): 

    def __init__(self):
        super().__init__()

    # region Operations

    def register(self, username: str, password: str) -> None:
            
        try:

            user_infos = self.Database.exec_request("SELECT * FROM Users WHERE username = ?", (username,), True)

            if user_infos is not None:
                raise InvalidCredentials("Username already taken.")

            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user = User(None, username, Role.USER.value, password, None)
            self.Database.exec_request("INSERT INTO Users(username, password, role) VALUES (?, ?, ?)", (user.Username, user.Password, user.Role))
            print("ok")

        finally:
            pass

    def login(self, username: str, password: str) -> list(str()):

        try:

            result: str = ""

            user_infos = self.Database.exec_request("SELECT * FROM Users WHERE username = ?", (username,), True)

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
                result = json.dumps({"id" : user.Id, "username" : user.Username, "role": user.Role, "userPP": user.UserPP, "accessToken": jwt_encoded})

            else:
                raise InvalidCredentials("Invalid credentials.")
            
            return result
            
        finally:
            pass


    def get_all_users(self):
        self.Database.exec_request("SELECT * FROM User")
        pass

    def get_user_by_id(self, user: User):
        self.Database.exec_request("SELECT * FROM User WHERE id = ?", (user.Id,))
        pass

    def add_user(self, user: User):
        self.Database.exec_request("INSERT INTO User(id, username, password, role) VALUES (?, ?, ?)", (user.Id, user.Username, user.Password, user.Role))
        pass

    def update_user(self, user: User):
        pass

    def delete_user(self, id: int):
        pass

    # endregion