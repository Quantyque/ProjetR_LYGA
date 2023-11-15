from manager.user_manager import UserManager
from controls.functional import FunctionalControls
from exceptions import InvalidInput, InvalidCredentials, TokenExpired
from flask import request
from logs import log_error, log_info
from constants import INTERNAL_ERROR
from flask_classful import FlaskView, route


class ViewUser(FlaskView):

    def __init__(self):
        self.__user_manager: UserManager = UserManager()

    @route('/register', methods=['POST'])
    def create(self) -> str():
        """
        Ajoute un utilisateur dans la base de données

        Returns:
            str: message de confirmation
        """
        try:
            # Initialisation des variables
            username: str = request.get_json().get('username')
            password: str = request.get_json().get('password')
            confirm_password: str = request.get_json().get('confirm_password')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id, username, password, confirm_password)
            FunctionalControls.check_forbidden_chars(username, password)
            FunctionalControls.check_password_match(password, confirm_password)

            # Envoi de la requête
            self.__user_manager.register(username, password)

            res = "User created", 200
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400
        
        except InvalidCredentials as e:
            log_info(str(e))
            res = str(e), 401

        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res

    @route('/login', methods=['POST'])
    def login(self) -> str():
        """
        Connecte un utilisateur à l'application

        Returns:
            str: token de connexion
        """
        try:
            # Initialisation des variables
            username: str = request.get_json().get('username')
            password: str = str(request.get_json().get('password'))

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(username, password)
            FunctionalControls.check_forbidden_chars(username, password)

            # Envoi de la requête
            result = self.__user_manager.login(username, password)

            res = result, 200
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400
        
        except TokenExpired as e:
            log_info(str(e))
            res = str(e), 401

        except InvalidCredentials as e:
            log_info(str(e))
            res = str(e), 401

        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res