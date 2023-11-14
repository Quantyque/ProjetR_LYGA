from data_processing.api.IApiDao import IApiDao
from typing import Dict
import os
import requests
from constants import STARTGG_API_URL

class StartGGDao(IApiDao):

    def request_api(self, query : str, variables: dict=None) -> Dict[str, str]:
        """
        Réalise une requête à l'API StartGG.

        Args:
            query (str): La requête GraphQL.
            variables (dict, optional): Les variables de la requête. Defaults to None.

        Returns:
            dict[str, str]: Les données de l'API.

        Raises:
            HTTPError: Si la requête échoue.
        """
        
        headers : dict = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('STARTGG_KEY')}"
        }

        fullquery : dict = {
            "query": query
            ,
            "variables": variables
        }
        response = requests.post(STARTGG_API_URL, json=fullquery, headers=headers)
        
        if response.status_code != 200:
            raise Exception(response.text)
        
        return response.json()