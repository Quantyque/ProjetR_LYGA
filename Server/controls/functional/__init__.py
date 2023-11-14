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
        Vériier que les arguments fournis ne sont pas nuls

        Args:
            *args: Valeurs à vérifier

        Raises:
            BadRequestException: Si la valeur est nulle

        Returns:
            None
        """
        for input_provided in args:
            if input_provided is None:
                raise BadRequestException(MISSING_ARGUMENTS)
            
    @staticmethod
    def check_forbidden_chars(*args):
        """
        Vérifier que les arguments fournis ne contiennent pas de caractères interdits

        Args:
            *args: Valeurs à vérifier

        Raises:
            InvalidInput: Si la valeur contient des caractères interdits

        Returns:
            None
        """
        for input_provided in args:
            if re.search(REGEX_FORBIDDEN_CHARS, input_provided):
                raise InvalidInput("Forbidden chars error : use only alphanumeric characters and spaces")
            
    @staticmethod
    def check_password_match(password: str, confirm_password: str) -> None:
        """
        Vérifier que les mots de passe fournis correspondent

        Args:
            password (str): Mot de passe
            confirm_password (str): Confirmation du mot de passe

        Raises:
            InvalidInput: Si les mots de passe ne correspondent pas

        Returns:
            None
        """
        if password != confirm_password:
            raise InvalidInput("Passwords doesn't match")