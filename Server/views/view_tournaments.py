from flask import request
from logs import log_info, log_error
from exceptions import BadRequestException, InvalidInput
from constants import INTERNAL_ERROR
from manager.tournament_manager import TournamentManager
from manager.video_game_manager import VideoGameManager
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.role import Role

class ViewTournament(FlaskView):

    def __init__(self) -> None:
        self.__tournament_manager = TournamentManager()

    @route('/location/', methods=['POST'])
    def tournament_by_location(self) -> dict:
        """
        Returns a list of tournaments by date, game and location

        Returns:
            dict: list of tournaments
        """
        try:
            # Variable initialization
            date = request.get_json().get('date')
            videogameId = request.get_json().get('videogameId')
            coordonnees = request.get_json().get('coordonnees')
            distance = request.get_json().get('distance')

            FunctionalControls.check_json_arguments_not_null(date, videogameId, coordonnees, distance)

            # Retrieving the selected video game
            videogame = VideoGameManager().get_video_game_by_id(videogameId)

            # Sending the request
            result = self.__tournament_manager.get_tournaments_by_location(date, videogame, coordonnees, distance)

            json = []
            for tournament in result:
                json.append(tournament.toJSON())

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