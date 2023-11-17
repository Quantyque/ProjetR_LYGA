from manager.set_manager import SetManager
from model.set import Set
from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from exceptions import BadRequestException, InvalidInput
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls

class ViewSet(FlaskView):
    """
    Controller permettant de gérer les sets
    """

    def __init__(self) -> None:
        self.__set_manager = SetManager()


    @route('/player', methods=['POST'])
    def get_last_sets_by_player(self) -> dict:
        """
        Retourne les 10 sets d'un joueur en fonction d'une page.

        Returns:
            dict: Les sets.

        Raises:
            Exception: Si la requête échoue.
        """
        try:
            # Initialisation des variables
            idPlayer = request.get_json().get('player_id')
            page = request.get_json().get('page')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(idPlayer, page)

            # Envoi de la requête
            result = self.__set_manager.get_last_sets_by_player(idPlayer, page)

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

