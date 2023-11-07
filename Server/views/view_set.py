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

    @route('/player/', methods=['POST'])
    def get_last_sets_by_player(self) -> dict:
        """
        Returns the last sets of a player

        Returns:
            dict: list of sets
        """
        try:
            # Variable initialization
            idPlayer = request.get_json().get('player_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(idPlayer)

            # Sending the request
            result = self.__set_manager.get_last_sets_by_player(idPlayer)

            json = []
            for set in result:
                json.append(set.toJSON())

            return json, 200
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except BadRequestException as e :
            log_info(str(e))
            return str(e), 400
        
        except InvalidInput as e :
            log_info(str(e))
            return str(e), 400
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500

