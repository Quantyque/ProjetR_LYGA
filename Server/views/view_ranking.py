from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from manager.ranking_manager import RankingManager
from utilities.crons import Crons
from controls.functional import FunctionalControls
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.role import Role
from exceptions import BadRequestException, InvalidInput
import datetime
import time

class ViewRanking(FlaskView):

    def __init__(self) -> None:
        self.__ranking_manager: RankingManager = RankingManager()
        self.__crons: Crons = Crons()

    @route('/parameters/auto-refresh', methods=['PUT'])
    def auto_ranking_refresh(self) -> str():
        """
        Automatically refresh player rankings based on past tournaments

        Args:
            activate (bool): Activate or deactivate the automatic refresh of the ranking
        
        Returns:
            str: Result of the request
        """
        try:
            activate: bool = request.get_json().get('activate')

            # Controls
            FunctionalControls.check_json_arguments_not_null(activate)

            # Initialize default values for the tournament (to be added in a config file)
            date_temp = datetime.datetime.today() - datetime.timedelta(days=1)
            date_unix = time.mktime(date_temp.timetuple())
            date = date_unix
            videogameId = 1386
            coordonnees = "47.316667, 5.016667"
            distance = "5km"

            if (activate == True):
                result = self.__crons.start_cron_task(self.__ranking_manager.update_ranking(date, videogameId, coordonnees, distance))
            else:
                result = self.__crons.stop_cron_task(self.__ranking_manager.update_ranking(date, videogameId, coordonnees, distance))

            return result, 200
        
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

    @route('/update', methods=['POST'])
    def manual_update_ranking(self) -> str():
        """
        Updates player rankings based on past tournaments since a given date manually with a query

        Args:
            date (datetime): Date from which to update the ranking
            videogameId (int): Id of the videogame for which to update the ranking
            coordonnees (str): Coordinates of the tournament location
            distance (str): Distance around the tournament location to search for players

        Returns:
            str: Result of the request
        """
        try:
            # Variable initialization
            date = request.get_json().get('date')
            videogameId = request.get_json().get('videogameId')
            coordonnees = request.get_json().get('coordonnees')
            distance = request.get_json().get('distance')

            # Controls
            FunctionalControls.check_json_arguments_not_null(date, videogameId, coordonnees, distance)

            # Sending the request
            result = self.__ranking_manager.update_ranking(date, videogameId, coordonnees, distance)

            # Results display
            for player_id in result:
                print(str(player_id) + " : " + result[player_id].Name + " : " + str(result[player_id].Elos[videogameId].Score))

            json = {}
            for player_id in result:
                json[player_id] = result[player_id].toJSON()

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

    


