from model.set import Set
from data_processing.api.startgg.set.ISetDaoApi import ISetDaoApi
from data_processing.api.startgg.set.SetDaoApi import SetDaoApi

class SetManager():
    """
    Classe permettant de gérer les sets
    """

    def __init__(self):
        self.__sg: ISetDaoApi = SetDaoApi()

    # region Operations

    def get_last_sets_by_player(self, idPlayer : int) -> [Set]:
        """
        Récupère les derniers sets d'un joueur.

        Args:
            idPlayer (int): L'id du joueur.
        
        Returns:
            [Set]: Les sets.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__sg.get_last_sets_by_player(idPlayer)

    
    #endregion