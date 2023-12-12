from data_processing.api.IApiDao import IApiDao
from data_processing.api.startgg.StartGGDao import StartGGDao

class Api:

    def __init__(self):
        self.__sg: IApiDao = StartGGDao()

    @property
    def sg(self):
        """
        Retourne l'API StartGG

        Returns:
            IApiDao: API StartGG

        Raises:
            None
        """
        return self.__sg
    
    @sg.setter
    def sg(self, sg):
        """
        Met à jour l'API StartGG

        Args:
            sg (IApiDao): Nouvelle API StartGG

        Returns:
            None
        """
        self.__sg = sg
