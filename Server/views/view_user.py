from manager.user_manager import UserManager
from controls.functional import FunctionalControls
from exceptions import InvalidInput, InvalidCredentials, TokenExpired
from flask import request
from logs import log_error, log_info
from constants import INTERNAL_ERROR
from flask_classful import FlaskView, route
from controls.technical import TechnicalControls
from model.role import Role


class ViewUser(FlaskView):

    def __init__(self):
        self.__user_manager: UserManager = UserManager()

    @route('/register/', methods=['POST'])
    def create(self) -> str():
        try:
            username: str = request.get_json().get('username')
            password: str = request.get_json().get('password')
            confirm_password: str = request.get_json().get('confirm_password')

            # Controls
            FunctionalControls.check_json_arguments_not_null(id, username, password, confirm_password)
            FunctionalControls.check_forbidden_chars(username, password)
            FunctionalControls.check_password_match(password, confirm_password)

            self.__user_manager.register(username, password)

            return "Registration completed", 200
        
        except InvalidInput as e:
            log_info((e))
            return str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except InvalidCredentials as e:
            log_info(str(e))
            return str(e), 401

        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500

    @route('/login', methods=['POST'])
    def login(self) -> str():
        try:
            username: str = request.get_json().get('username')
            password: str = str(request.get_json().get('password'))

            # Controls
            FunctionalControls.check_json_arguments_not_null(username, password)
            FunctionalControls.check_forbidden_chars(username, password)

            result = self.__user_manager.login(username, password)

            return result, 200
        
        except InvalidInput as e:
            log_info((e))
            return str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except TokenExpired as e:
            log_info(str(e))
            return str(e), 401

        except InvalidCredentials as e:
            log_info(str(e))
            return str(e), 401

        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500