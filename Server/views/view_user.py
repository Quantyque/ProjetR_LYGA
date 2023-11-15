from manager.user_manager import UserManager
from controls.functional import FunctionalControls
from exceptions import InvalidInput, InvalidCredentials, TokenExpired, UserNotFound
from flask import request
from logs import log_error, log_info
from constants import INTERNAL_ERROR
from flask_classful import FlaskView, route
from controls.technical import TechnicalControls
from model.role import Role
from model.user import User


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
        
    @route('/get-all', methods=['GET'])
    def get_all_users(self) -> str():
        """
        Retourne tous les utilisateurs

        Returns:
            str: liste des utilisateurs
        """
        try:
            # Envoi de la requête
            result = self.__user_manager.get_all_users()

            res = result, 200
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res
        
    @route('/get-by-id', methods=['POST'])
    def get_user_by_id(self) -> str():
        """
        Retourne un utilisateur en fonction de son id

        Returns:
            str: utilisateur
        """
        try:
            # Initialisation des variables
            id: int = request.get_json().get('id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id)

            # Envoi de la requête
            result = self.__user_manager.get_user_by_id(id)

            res = result, 200
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400

        except UserNotFound as e:
            log_info(str(e))
            res = str(e), 404
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res
        
    @route('/update', methods=['PUT'])
    def update_user(self) -> str():
        """
        Met à jour un utilisateur

        Returns:
            str: message de confirmation
        """
        try:
            # Initialisation des variables
            id: int = request.get_json().get('id')
            username: str = request.get_json().get('username')
            password: str = request.get_json().get('password')
            userPP: str = request.get_json().get('userPP')
            role: Role = request.get_json().get('role')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id)
            FunctionalControls.check_forbidden_chars(username, userPP)

            if password is not None:
                FunctionalControls.check_forbidden_chars(password)
            
            # Vérification de l'utilisateur
            TechnicalControls.check_is_user(request.headers.get('Authorization'), id)

            # Envoi de la requête
            self.__user_manager.update_user(User(id, username, password, userPP, role))

            res = "User updated", 200
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400

        except InvalidCredentials as e:
            log_info(str(e))
            res = str(e), 401

        except TokenExpired as e:
            log_info(str(e))
            res = str(e), 401

        except UserNotFound as e:
            log_info(str(e))
            res = str(e), 404
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res
        
    @route('/delete', methods=['DELETE'])
    def delete_user(self) -> str():
        """
        Supprime un utilisateur

        Returns:
            str: message de confirmation
        """
        try:
            # Initialisation des variables
            id: int = request.get_json().get('id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id)

            # Vérification de l'utilisateur
            TechnicalControls.check_is_user(request.headers.get('Authorization'), id)

            # Envoi de la requête
            self.__user_manager.delete_user(id)

            res = "User deleted", 200
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400

        except InvalidCredentials as e:
            log_info(str(e))
            res = str(e), 401

        except TokenExpired as e:
            log_info(str(e))
            res = str(e), 401

        except UserNotFound as e:
            log_info(str(e))
            res = str(e), 404
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res