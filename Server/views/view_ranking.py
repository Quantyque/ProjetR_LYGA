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
    @TechnicalControls.is_role([Role.ADMIN])
    def auto_ranking_refresh(self) -> str():
        """
        Rafraichit automatiquement le classement des joueurs en fonction des tournois passés

        Args (Requested PUT JSON)):
            activate (bool): Active ou désactive le rafraichissement automatique du classement
        
        Returns:
            str: Resultat de la requête
        """
        try:
            # Initialisation des variables
            activate: bool = request.get_json().get('activate')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(activate)

            # Initialise les valeurs par défaut du tournoi (à ajouter dans un fichier de config)
            date_temp = datetime.datetime.today() - datetime.timedelta(days=1)
            date_unix_after = time.mktime(date_temp.timetuple())
            after_date = date_unix_after
            date_unix_before = time.mktime(datetime.datetime.today().timetuple())
            before_date = date_unix_before
            videogameId = 1386
            coordonnees = "47.316667, 5.016667"
            distance = "5km"

            if (activate == True):
                result = self.__crons.start_cron_task(self.__ranking_manager.update_ranking(after_date, before_date, videogameId, coordonnees, distance))
            else:
                result = self.__crons.stop_cron_task(self.__ranking_manager.update_ranking(after_date, before_date, videogameId, coordonnees, distance))

            res = result, 200
        
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
    @TechnicalControls.is_role([Role.ADMIN])
    def manual_update_ranking(self) -> str():
        """
        Met à jour le classement des joueurs en fonction des tournois passés depuis une date donnée manuellement

        Args (Requested POST JSON)):
            date (datetime) : Date à partir de laquelle mettre à jour le classement
            videogameId (int) : Id du jeu vidéo pour lequel mettre à jour le classement
            coordonnees (str) : Coordonnées du lieu du tournoi
            distance (str) : Distance autour du lieu du tournoi pour chercher les joueurs

        Returns:
            str: Resultat de la requête
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

            # Envoie de la requête
            result = self.__ranking_manager.update_ranking(afterDate, beforeDate, videogameId, coordonnees, distance)

            # Affichage du résultat
            for player_id in result:
                print(str(player_id) + " : " + result[player_id].Name + " : " + str(result[player_id].Elos[videogameId].Score))

            # Récupération du résultat sous forme de JSON
            json = {}
            for player_id in result:
                json[player_id] = result[player_id].toJSON()

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

    


