from flask import request
from logs import log_info, log_error
from constants import INTERNAL_ERROR
from manager.video_game_manager import VideoGameManager
from model.videogame import Videogame
from exceptions import DuplicateGame, GameNotAudited, InvalidInput
from controls.functional import FunctionalControls
from flask_classful import FlaskView, route
from controls.technical import TechnicalControls
from model.role import Role

class ViewVideoGames(FlaskView):

    def __init__(self):
        self.__video_game_manager = VideoGameManager()
        self.__video_game = Videogame()

    @route('/all', methods=['GET'])
    # @TechnicalControls.is_role([Role.ADMIN])
    def all_video_games(self) -> str():
        """
        Recupere tous les jeux disponibles sur Start.gg

        Return: 
            str: Liste de tous les jeux disponibles sur Start.gg
        """
        try:
            # Envoi de la requête
            result = self.__video_game_manager.get_all_video_game()

            # Récupération du résultat sous forme de JSON
            json = []
            for game in result:
                json.append(game.toJSON())

            res = json, 200

        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res
    
    @route('/add-audited', methods=['POST'])
    @TechnicalControls.is_role([Role.ADMIN])
    def add_audited_game(self) -> str():
        """
        Ajout d'un jeu à la liste des jeux audités

        Args:
            id (int): Id du jeu à ajouter
            name (str): Nom du jeu à ajouter
        
        Return:
            str: Message de succès ou d'erreur
        """
        try:
            # Initialisation des variables
            id: int = int(request.get_json().get('id'))
            name: str = request.get_json().get('name')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id, name)
            FunctionalControls.check_forbidden_chars(name)

            self.__video_game.Id = id
            self.__video_game.Name = name

            # Envoi de la requête
            result = self.__video_game_manager.add_audited_game(self.__video_game)
            
            res = result, 201
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400
        
        except DuplicateGame as e :
            log_info(str(e))
            res = str(e), 409
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res
    
    @route('/audited', methods=['GET'])
    def get_audited_game(self) -> str():
        """
        Réupère la liste des jeux audités

        Return:
            str: Liste des jeux audités
        """
        try:
            res = self.__video_game_manager.list_audited_game(), 200

        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res

    @route('/update-audited', methods=['PUT'])
    @TechnicalControls.is_role([Role.ADMIN])    
    def update_audited_game(self) -> str():
        """
        Modifie un jeu dans la liste des jeux audités

        Args:
            id (int): Id du jeu à modifier
            name (str): Nouveau nom du jeu à modifier
        
        Return:
            str: Message de succès ou d'erreur
        """
        try:
            # Initialisation des variables
            id: int = int(request.get_json().get('id'))
            name: str = request.get_json().get('name')

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id, name)
            FunctionalControls.check_forbidden_chars(name)

            self.__video_game.Id = id
            self.__video_game.Name = name

            res = self.__video_game_manager.update_audited_game(self.__video_game), 200
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400    
        
        except GameNotAudited as e :
            log_info(str(e))
            res = str(e), 404

        except DuplicateGame as e :
            log_info(str(e))
            res = str(e), 409
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res

    @route('/delete-audited', methods=['DELETE'])
    @TechnicalControls.is_role([Role.ADMIN])    
    def delete_audited_game(self) -> str():
        """
        Supprime un jeu de la liste des jeux audités

        Args:
            id (int): Id du jeu à supprimer
        
        Return:
            str: Message de succès ou d'erreur
        """
        try:
            # Initialisation des variables
            id: int = int(request.get_json().get('id'))

            # Verification des variables
            FunctionalControls.check_json_arguments_not_null(id)

            self.__video_game.Id = id
            self.__video_game.Name = None

            res = self.__video_game_manager.delete_audited_game(self.__video_game), 200
        
        except ValueError as e :
            log_info(str(e))
            res = str(e), 400
        
        except InvalidInput as e:
            log_info((e))
            res = str(e), 400
        
        except GameNotAudited as e :
            log_info(str(e))
            res = str(e), 404
        
        except Exception as e :
            log_error(str(e))
            res = INTERNAL_ERROR, 500

        finally:
            return res