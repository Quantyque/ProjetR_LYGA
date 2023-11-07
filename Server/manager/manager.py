from data_processing.sql.sqlite_database import SQLiteDatabase
from data_processing.sql.idatabase import IDatabase
import os
import requests
from constants import STARTGG_API_URL

class Manager:
    """
    Classe hérité par les managers pour utiliser la base de données et l'api startgg
    """

    def __init__(self):
        self.__db : IDatabase = SQLiteDatabase()

    # region Properties

    @property
    def Database(self) -> IDatabase:
        """
        Base de données de l'application
        """
        return self.__db
    
    @Database.setter
    def Database(self, db : IDatabase) -> None:
        self.__db = db

    # endregion

    # region Operations

    def request_api(self, query : str, variables: dict=None) -> dict[str, str]:
        """
        Récupère les données de l'api startgg

        Args:
            query (str): La requête graphql
            variables (dict, optional): Les variables de la requête. None par défaut.

        Returns:
            dict[str, str]: Le résultat de la requête
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

    # endregion

