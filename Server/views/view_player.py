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
    Controleur permettant de lier les requêtes HTTP aux managers des joueurs
    """

    def __init__(self) -> None:
        self.__player_manager = PlayerManager()

    @route('/infos', methods=['POST'])
    def get_infos_player(self) -> str():
        """
        Renvoi les informations d'un joueur en fonction de son id

        Returns:
            str: informations du joueur
        """
        try:
            # Initialisation des variables
            player_id = request.get_json().get('player_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(player_id)

            # Envoi de la requête
            result = self.__player_manager.get_player_by_id(player_id)

            return result.toJSON(), 200
        
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
        
    @route('/all', methods=['GET'])
    def get_all_players(self) -> str():
        """
        Renvoi la liste de tous les joueurs de la base de données

        Returns:
            str: liste de tous les joueurs de la base de données
        """
        try:

            # Envoi de la requête
            result = self.__player_manager.get_all_players()

            # Récupération du résultat sous forme de JSON
            json = []
            for idplayer in result:
                json.append(result[idplayer].toJSON())

            res = json, 200
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500
        
        finally:
            return res

    @route('/all_ranked', methods=['POST']) 
    def get_ranked_players(self) -> str():
        """
        Renoi la liste des joueurs classés par elo pour un jeu donné ayant joué le nombre de tournois minimum

        Returns:
            str: liste des joueurs classés par elo pour un jeu donné ayant joué le nombre de tournois minimum
        """
        try:
            # Initialisation des variables
            videogame_id = request.get_json().get('videogame_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(videogame_id)

            # Envoi de la requête
            result = self.__player_manager.get_ranked_players(videogame_id)

            # Récupération du résultat sous forme de JSON
            json = []
            for idplayer in result:
                json.append(result[idplayer].toJSON())

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
    


