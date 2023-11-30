from typing import Optional

class IDatabase:
    """
    Interface pour les bases de données
    """

    def exec_request(self, req: str, params: Optional[tuple] = None, data_fetch_one: Optional[bool] = False) -> Optional[list]:
        """
        Exécute une requête SQL.

        Args:
            req (str): La requête SQL.
            params (tuple, optional): Les paramètres de la requête. Defaults to None.
            data_fetch_one (bool, optional): True si on veut récupérer un seul élément, False sinon. Defaults to False.

        Returns:
            list, optional: La liste des résultats de la requête.

        Raises:
            Exception: Si la requête échoue.
        """ 
        pass