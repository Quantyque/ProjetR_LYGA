from model.entity import Entity

class Season (Entity):
    """
    Represente une saison d'un classement
    """

    def __init__(self):
        self.__id : int = None
        self.__number : int = None
        self.__start_date : int = None
        self.__end_date : int = None

    # region Properties

    @property
    def Id(self) -> int:
        """
        Getter de l'id de la saison

        Returns:
            int: Id de la saison
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        """
        Setter de l'id de la saison

        Args:
            id (int): Nouvel id de la saison
        """
        self.__id = id

    @property
    def Number(self) -> int:
        """
        Getter du numéro de la saison

        Returns:
            int: Numéro de la saison
        """
        return self.__number
    
    @Number.setter
    def Number(self, number : int) -> None:
        """
        Setter du numéro de la saison

        Args:
            number (int): Nouveau numéro de la saison
        """
        self.__number = number

    @property
    def StartDate(self) -> int:
        """
        Getter de la date de début de la saison

        Returns:
            int: Date unix de début de la saison
        """
        return self.__start_date
    
    @StartDate.setter
    def StartDate(self, start_date : int) -> None:
        """
        Setter de la date de début de la saison

        Args:
            start_date (int): Nouvelle date de début de la saison
        """
        self.__start_date = start_date

    @property
    def EndDate(self) -> int:
        """
        Getter de la date de fin de la saison

        Returns:
            int: Date unix de fin de la saison
        """
        return self.__end_date
    
    @EndDate.setter
    def EndDate(self, end_date : int) -> None:
        """
        Setter de la date de fin de la saison

        Args:
            end_date (int): Nouvelle date de fin de la saison
        """
        self.__end_date = end_date

    # endregion

    def hydrate(self, data : dict) -> None:
        if "id" in data:
            self.Id = data["id"]
        if "number" in data:
            self.Number = data["number"]
        if "startDate" in data:
            self.StartDate = data["startDate"]
        if "endDate" in data:
            self.EndDate = data["endDate"]

    def toJSON(self) -> dict:
        return {
            "id" : self.Id,
            "number" : self.Number,
            "startDate" : self.StartDate,
            "endDate" : self.EndDate
        }