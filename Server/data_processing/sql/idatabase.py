class IDatabase:
    """
    Interface pour les bases de données
    """

    def exec_request(self, req : str, params : tuple = None):
        """
        Exécute une requête SQL.

        Args:
            req (str): La requête SQL.
            params (tuple, optional): Les paramètres de la requête. Defaults to None.

        Returns:
            list, optional: La liste des résultats de la requête.

        Raises:
            Exception: Si la requête échoue.
        """ 
        pass