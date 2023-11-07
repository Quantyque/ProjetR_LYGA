from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from manager.player_manager import PlayerManager
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.role import Role
from exceptions import BadRequestException, InvalidInput

class ViewPlayer(FlaskView):
    """
    Controller for linking HTTP requests to player managers
    """

    def __init__(self) -> None:
        self.__player_manager = PlayerManager()

    @route('/infos', methods=['POST'])
    def get_infos_player(self) -> str():
        """
        Returns player information based on id

        Returns:
            str: player information
        """
        try:

            # Variable initialization
            player_id = request.get_json().get('player_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(player_id)

            # Sending the request
            result = self.__player_manager.get_player_by_id(player_id)

            return result.toJSON(), 200
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except InvalidInput as e :
            log_info(str(e))
            return str(e), 400
        
        except BadRequestException as e :
            log_info(str(e))
            return str(e), 400
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500
        
    @route('/all', methods=['GET'])
    def get_all_players(self) -> str():
        """
        Returns a list of all players in the database

        Returns:
            str: list of all players in the database
        """
        try:

            # Sending the request
            result = self.__player_manager.get_all_players()

            json = []
            for idplayer in result:
                json.append(result[idplayer].toJSON())

            return json, 200
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500

    @route('/all_ranked', methods=['POST']) 
    def get_ranked_players(self) -> str():
        """
        Returns the players ranked by elo for a given game who have played the minimum number of tournaments.

        Returns:
            str: list of players ranked by elo for a given game who have played the minimum number of tournaments.
        """
        try:
            # Variable initialization
            videogame_id = request.get_json().get('videogame_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(videogame_id)

            # Sending the request
            result = self.__player_manager.get_ranked_players(videogame_id)

            json = []
            for idplayer in result:
                json.append(result[idplayer].toJSON())

            return json, 200
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except InvalidInput as e :
            log_info(str(e))
            return str(e), 400
        
        except BadRequestException as e :
            log_info(str(e))
            return str(e), 400
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500
    


