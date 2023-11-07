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
    def all_video_games(self) -> str():
        """
        Get all video games available on Smash.gg

        Return: 
            str: List of all video games available on Smash.gg
        """
        try:
            result = self.__video_game_manager.get_all_video_game()

            json = []
            for game in result:
                json.append(game.toJSON())

            return json, 200

        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500
    
    @route('/add-audited', methods=['POST'])
    # @TechnicalControls.is_role([Role.ADMIN])
    def add_audited_game(self) -> str():
        """
        Add a game to the list of audited games

        Args:
            id (int): Id of the game to add
            name (str): Name of the game to add
        
        Return:
            str: Message of success or error
        """
        try:
            
            id: int = int(request.get_json().get('id'))
            name: str = request.get_json().get('name')

            # Controls
            FunctionalControls.check_json_arguments_not_null(id, name)
            FunctionalControls.check_forbidden_chars(name)

            self.__video_game.Id = id
            self.__video_game.Name = name

            result = self.__video_game_manager.add_audited_game(self.__video_game)
            return result, 200
        
        except InvalidInput as e:
            log_info((e))
            return str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except DuplicateGame as e :
            log_info(str(e))
            return str(e), 409
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500
    
    @route('/audited', methods=['GET'])
    def get_audited_game(self) -> str():
        """
        Get all audited games

        Return:
            str: List of all audited games
        """
        try:
            return self.__video_game_manager.list_audited_game(), 200

        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500

    @route('/update-audited', methods=['PUT'])
    # @TechnicalControls.is_role([Role.ADMIN])    
    def update_audited_game(self) -> str():
        """
        Update a game in the list of audited games

        Args:
            id (int): Id of the game to update
            name (str): New name of the game to update
        
        Return:
            str: Message of success or error
        """
        try:
            id: int = int(request.get_json().get('id'))
            name: str = request.get_json().get('name')

            # Controls
            FunctionalControls.check_json_arguments_not_null(id, name)
            FunctionalControls.check_forbidden_chars(name)

            self.__video_game.Id = id
            self.__video_game.Name = name

            return self.__video_game_manager.update_audited_game(self.__video_game), 200
        
        except InvalidInput as e:
            log_info((e))
            return str(e), 400
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except GameNotAudited as e :
            log_info(str(e))
            return str(e), 404
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500

    @route('/delete-audited', methods=['DELETE'])
    # @TechnicalControls.is_role([Role.ADMIN])    
    def delete_audited_game(self) -> str():
        """
        Delete a game from the list of audited games

        Args:
            id (int): Id of the game to delete
        
        Return:
            str: Message of success or error
        """
        try:
            id: int = int(request.get_json().get('id'))

            # Controls
            FunctionalControls.check_json_arguments_not_null(id)

            self.__video_game.Id = id
            self.__video_game.Name = None

            return self.__video_game_manager.delete_audited_game(self.__video_game), 200
        
        except ValueError as e :
            log_info(str(e))
            return str(e), 400
        
        except InvalidInput as e:
            log_info((e))
            return str(e), 400
        
        except GameNotAudited as e :
            log_info(str(e))
            return str(e), 404
        
        except Exception as e :
            log_error(str(e))
            return INTERNAL_ERROR, 500