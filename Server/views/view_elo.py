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
    Controleur permettant de lier les requêtes HTTP aux managers des elos
    """

    def __init__(self) -> None:
        self.__elo_manager = EloManager()

    @route('/default', methods=['POST'])
    def get_default_elo(self) -> str():
        """
        Renvoit l'elo par défaut d'un joueur en fonction de son id et de l'id du jeu vidéo

        Returns:
            str: elo par défaut du joueur
        """
        try:
            # Initialisation des variables
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id)

            # Envoi de la requête
            result = self.__elo_manager.get_default_elo(player_id, videogame_id)

            #Récupération du résultat
            res = str(result), 200
        
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
        
    @route('/add-default', methods=['POST'])
    @TechnicalControls.is_role([Role.ADMIN])
    def add_default_elo(self) -> str():
        """
        Ajoute un elo par défaut à un joueur

        Returns:
            str: elo par défaut ajouté
        """
        try:

            # Initialisation des variables
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id)

            # Envoi de la requête
            self.__elo_manager.add_default_elo(player_id, videogame_id)

            res = "Elo par défaut ajouté", 200
        
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
        
    @route('/edit-default', methods=['POST'])
    @TechnicalControls.is_role([Role.ADMIN])
    def edit_elo(self) -> str():
        """
        Modifie l'elo d'un joueur

        Returns:
            str: elo modifié
        """
        try:
            # Initialisation des variables
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')
            elo = request.get_json().get('elo')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id, elo)

            # Envoi de la requête
            self.__elo_manager.edit_elo(player_id, videogame_id, elo)

            res = "Elo modifié", 200
        
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
        

        
    @route('/delete-default', methods=['DELETE'])
    @TechnicalControls.is_role([Role.ADMIN])
    def delete_default_elo(self) -> str():
        """
        Deletes a player's default elo

        Returns:
            str: default elo deleted
        """
        try:
            # Initialisation des variables
            player_id = request.get_json().get('player_id')
            videogame_id = request.get_json().get('videogame_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(player_id, videogame_id)

            # Envoi de la requête
            self.__elo_manager.delete_default_elo(player_id, videogame_id)

            res = "Elo par défaut supprimé", 200
        
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
        
    @route('/get-history', methods=['POST'])
    def get_history(self) -> str():
        """
        Renvoi l'historique des elos d'un joueur

        Returns:
            str: historique des elos du joueur
        """
        try:
            # Initialisation des variables
            player_id = request.get_json().get('player_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(player_id)

            # Envoi de la requête
            result = self.__elo_manager.get_history_elos(player_id)

            #Récupération du résultat sous forme de json
            json = []
            for elo in result:
                json.append(elo.toJSON())

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
        