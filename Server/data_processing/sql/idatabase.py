from typing import Optional

class IDatabase:
    """
    Interface pour les bases de données
    """

    def exec_request_one(self, req: str, params: Optional[tuple] = None) -> object:
        """
        Exécute une requête SQL en renvoyant un seul résultat.

        Args:
            req (str): La requête SQL.
            params (tuple, optional): Les paramètres de la requête. Defaults to None.

        Returns:
            object: Le résultat de la requête.

        Raises:
            Exception: Si la requête échoue.
        """ 
        pass

    def exec_request_multiple(self, req: str, params: Optional[tuple] = None) -> Optional[list]:
        """
        Exécute une requête SQL en renvoyant plusieurs résultats.

        Args:
            req (str): La requête SQL.
            params (tuple, optional): Les paramètres de la requête. Defaults to None.

        Returns:
            list, optional: La liste des résultats de la requête.

        Raises:
            Exception: Si la requête échoue.
        """ 
        pass