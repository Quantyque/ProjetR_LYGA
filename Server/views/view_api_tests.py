from unit_tests.api_tests import ApiTests
from constants import INTERNAL_ERROR
from logs import log_error
from flask_classful import FlaskView, route
from controls.technical import TechnicalControls
from model.role import Role

class ViewApiTests(FlaskView):
    """
    Controller permettant de gérer les tests unitaires
    """

    @staticmethod
    @route('/run', methods=['GET'])
    @TechnicalControls.is_role([Role.ADMIN])
    def run_unit_tests() -> (str, int):
        """
            Lance les tests unitaires

            Returns:
                (str, int): Resultat des tests unitaires et code HTTP
        """
        try:
            return ApiTests.run_unit_tests(), 200

        except Exception as e:
            log_error(str(e))
            return INTERNAL_ERROR, 500
    
