from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from manager.elo_manager import EloManager
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.role import Role
from exceptions import BadRequestException, InvalidInput

class ViewElo(FlaskView):
    """
    Controller for linking HTTP requests to managers for elos
    """

    def __init__(self) -> None:
        self.__elo_manager = EloManager()

    @route('/default', methods=['POST'])
    def get_default_elo(self) -> str():
        """
        Returns a player's default elo based on his id and the video game id

        Returns:
            str: player's default elo
        """
        try:
            # Variable initialization
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id)

            # Sending the request
            result = self.__elo_manager.get_default_elo(player_id, videogame_id)

            return str(result), 200
        
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
        
    @route('/add-default', methods=['POST'])
    def add_default_elo(self) -> str():
        """
        Adds a default elo to a player

        Returns:
            str: default elo added
        """
        try:

            # Variable initialization
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id)

            # Sending the request
            self.__elo_manager.add_default_elo(player_id, videogame_id)

            return "Elo par défaut ajouté", 200
        
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
        
    @route('/edit-default', methods=['POST'])
    def edit_elo(self) -> str():
        """
        Modifies a player's elo

        Returns:
            str: elo modified
        """
        try:
            # Variable initialization
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')
            elo = request.get_json().get('elo')

            # Controls
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id, elo)

            # Sending the request
            self.__elo_manager.edit_elo(player_id, videogame_id, elo)

            return "Elo modifié", 200
        
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
        
    @route('/delete-default', methods=['DELETE'])
    def delete_default_elo(self) -> str():
        """
        Deletes a player's default elo

        Returns:
            str: default elo deleted
        """
        try:
            # Variable initialization
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id)

            # Sending the request
            self.__elo_manager.delete_default_elo(player_id, videogame_id)

            return "Elo par défaut supprimé", 200
        
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
        
    @route('/get-history', methods=['POST'])
    def get_history(self) -> str():
        """
        Returns a player's elo history

        Returns:
            str: player's elo history
        """
        try:
            # Variable initialization
            player_id = request.get_json().get('player_id')

            # Controls
            FunctionalControls.check_json_arguments_not_null(player_id)

            # Sending the request
            result = self.__elo_manager.get_history_elos(player_id)

            json = []
            for elo in result:
                json.append(elo.toJSON())

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
        