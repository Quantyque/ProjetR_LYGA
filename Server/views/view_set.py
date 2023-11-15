from manager.set_manager import SetManager
from model.set import Set
from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from exceptions import BadRequestException, InvalidInput
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.role import Role

class ViewSet(FlaskView):
    """
    Controller for linking HTTP requests to set managers
    """

    def __init__(self) -> None:
        self.__set_manager = SetManager()

    @route('/player', methods=['POST'])
    def get_last_sets_by_player(self) -> dict:
        """
        Renvoie les derniers sets d'un joueur

        Returns:
            dict: liste des derniers sets d'un joueur
        """
        try:
            # Initialisation des variables
            idPlayer = request.get_json().get('player_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(idPlayer)

            # Envoi de la requête
            result = self.__set_manager.get_last_sets_by_player(idPlayer)

            #Récupération du résultat sous forme de JSON
            json = []
            for set in result:
                json.append(set.toJSON())

            res = json, 200
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400
        
        except InvalidInput as e :
            log_info(str(e))
            res = str(e), 400
        
        except BadRequestException as e :
            log_info(str(e))
            res = str(e), 400
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500
        
        finally:
            return res

