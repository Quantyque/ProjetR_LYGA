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
        Renvoi une liste de tournois par date, jeu et lieu

        Returns:
            dict: liste de tournois
        """
        try:
            # Initialisation des variables
            date = request.get_json().get('date')
            videogameId = request.get_json().get('videogameId')
            coordonnees = request.get_json().get('coordonnees')
            distance = request.get_json().get('distance')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(date, videogameId, coordonnees, distance)

            # Récupération du jeu vidéo selectionné
            videogame = VideoGameManager().get_video_game_by_id(videogameId)

            # Envoi de la requête
            result = self.__tournament_manager.get_tournaments_by_location(date, videogame, coordonnees, distance)

            # Récupération du résultat sous forme de JSON
            json = []
            for tournament in result:
                json.append(tournament.toJSON())

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