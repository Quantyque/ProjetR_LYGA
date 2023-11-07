class IDatabase:
    """
    Interface pour les bases de données
    """

    def exec_request(self, req : str, params : tuple = None):
        """
        Exécute une requête sur la base de données

        Args:
            req (str): La requête à exécuter
            params (tuple, optional): Les paramètres de la requête.

        Returns:
            list: Liste des résultats de la requête
        """ 
        pass