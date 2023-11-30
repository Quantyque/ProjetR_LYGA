from flask import request
from logs import log_info, log_error
from exceptions import BadRequestException, InvalidInput
from constants import INTERNAL_ERROR
from manager.tournament_manager import TournamentManager
from manager.video_game_manager import VideoGameManager
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls

class ViewTournament(FlaskView):
    """
    Controller permettant de gérer les tournois
    """

    def __init__(self) -> None:
        self.__tournament_manager = TournamentManager()

    @route('/location', methods=['POST'])
    def tournament_by_location(self) -> (str, int):
        """
        Renvoi une liste de tournois par date, jeu et lieu

        Args:
            afterDate (str): date de début de recherche
            beforeDate (str): date de fin de recherche
            videogameId (int): id du jeu vidéo
            coordonnees (dict): coordonnées GPS
            distance (int): distance de recherche

        Returns:
            str: tournois
            int: code HTTP
        """
        try:
            # Initialisation des variables
            afterDate = request.get_json().get('afterDate')
            beforeDate = request.get_json().get('beforeDate')
            videogameId = request.get_json().get('videogameId')
            coordonnees = request.get_json().get('coordonnees')
            distance = request.get_json().get('distance')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(afterDate, beforeDate, videogameId, coordonnees, distance)

            # Récupération du jeu vidéo selectionné
            videogame = VideoGameManager().get_video_game_by_id(videogameId)

            # Envoi de la requête
            result = self.__tournament_manager.get_tournaments_by_location(afterDate, beforeDate, videogame, coordonnees, distance)

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