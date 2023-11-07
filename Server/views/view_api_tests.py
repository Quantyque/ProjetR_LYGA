from unit_tests.api_tests import ApiTests
from constants import INTERNAL_ERROR
from logs import log_error, log_info
from flask_classful import FlaskView, route
from controls.functional import FunctionalControls
from controls.technical import TechnicalControls
from model.role import Role
from exceptions import BadRequestException, InvalidInput

class ViewApiTests(FlaskView):

    @staticmethod
    @route('/run', methods=['GET'])
    def run_unit_tests():
        """
            Run unit tests

            Returns:
                (str, int): Unit tests result and status code
        """
        try:
            return ApiTests.run_unit_tests(), 200

        except Exception as e:
            log_error(str(e))
            return INTERNAL_ERROR, 500
    
