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

    def get_last_sets_by_player(self, idPlayer : int, page : int) -> [Set]:
        """
        Retourne les 10 sets d'un joueur en fonction d'une page.

        Args:
            idPlayer (int): L'id du joueur.
            page (int): La page à afficher.

        Returns:
            [Set]: Les sets.

        Raises:
            Exception: Si la requête échoue.
        """
        pass
        return self.__sg.get_last_sets_by_player(idPlayer, page)

    
    #endregion