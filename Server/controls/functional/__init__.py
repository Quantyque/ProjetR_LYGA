from exceptions import BadRequestException, InvalidInput
from constants import MISSING_ARGUMENTS, REGEX_FORBIDDEN_CHARS
import re

#************************************************************************************************
# Functional controls
#************************************************************************************************

class FunctionalControls:

    @staticmethod        
    def check_json_arguments_not_null(*args):
        """
        Check if the arguments provided are not null

        Args:
            *args: Values to check
        
        Raises:
            BadRequestException: If the value is null

        Returns:
            None
        """
        for input_provided in args:
            if input_provided is None:
                raise BadRequestException(MISSING_ARGUMENTS)
            
    @staticmethod
    def check_forbidden_chars(*args):
        """
        Check if the arguments provided contains forbidden chars

        Args:
            *args: Values to check

        Raises:
            InvalidInput: If the value contains forbidden chars

        Returns:
            None
        """
        for input_provided in args:
            if re.search(REGEX_FORBIDDEN_CHARS, input_provided):
                raise InvalidInput("Forbidden chars error : use only alphanumeric characters and spaces")
            
    @staticmethod
    def check_password_match(password: str, confirm_password: str) -> None:
        """
        Check if the passwords provided match

        Args:
            password (str): Password
            confirm_password (str): Password confirmation

        Raises:
            InvalidInput: If the passwords doesn't match

        Returns:
            None
        """
        if password != confirm_password:
            raise InvalidInput("Passwords doesn't match")