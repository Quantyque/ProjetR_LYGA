from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from manager.season_manager import SeasonManager
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.season import Season
from exceptions import BadRequestException, InvalidInput

class ViewSeason(FlaskView):
    """
    Controleur permettant de lier les requêtes HTTP au manager des saisons
    """

    def __init__(self) -> None:
        self.__season_manager = SeasonManager()

    @route('/get', methods=['GET'])
    def get_season_by_id(self) -> str():
        """
        Renvoi une saison en fonction de son id

        Returns:
            str: saison
        """
        try:
            # Initialisation des variables
            season_id = request.args.get('season_id')

            # Verification des variables
            FunctionalControls.check_arguments_not_null(season_id)

            # Envoi de la requête
            result = self.__season_manager.get_season_by_id(season_id)

            res = result.toJSON(), 200
        
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
    def get_all_seasons(self) -> str():
        """
        Renvoi toutes les saisons

        Returns:
            str: saisons
        """
        try:
            # Envoi de la requête
            result = self.__season_manager.get_all_seasons()

            json = []
            for season in result:
                json.append(season.toJSON())

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
        
    @route('/add', methods=['POST'])
    def add_season(self) -> str():
        """
        Ajoute une saison

        Returns:
            str: saison
        """
        try:
            # Initialisation des variables
            number = request.get_json().get('number')
            start_date = request.get_json().get('start_date')
            end_date = request.get_json().get('end_date')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(number, start_date, end_date)

            # Envoi de la requête
            self.__season_manager.add_season(number, start_date, end_date)

            res = "Saison ajoutée", 200
        
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
        
    @route('/update', methods=['POST'])
    def update_season(self) -> str():
        """
        Met à jour une saison

        Returns:
            str: saison
        """
        try:
            # Initialisation des variables
            id = request.get_json().get('season_id')
            number = request.get_json().get('number')
            start_date = request.get_json().get('start_date')
            end_date = request.get_json().get('end_date')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id, number, start_date, end_date)

            # Envoi de la requête
            self.__season_manager.update_season(id, number, start_date, end_date)

            res = "Saison mise à jour", 200
        
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
        
    @route('/remove', methods=['POST'])
    def remove_season(self) -> str():
        """
        Supprime une saison

        Returns:
            str: saison
        """
        try:
            # Initialisation des variables
            id = request.get_json().get('season_id')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id)

            # Envoi de la requête
            self.__season_manager.remove_season(id)

            res = "Saison supprimée", 200
        
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
