from typing import Dict
from abc import ABC, abstractmethod

class IApiDao(ABC):

    @abstractmethod
    def request_api(self, query : str, variables: dict=None) -> Dict[str, str]:
        """
        Envoie une requête à l'API.

        Args:
            query (str): La requête GraphQL.
            variables (dict, optional): Les variables de la requête. Defaults to None.

        Returns:
            dict[str, str]: Les données de l'API.

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass