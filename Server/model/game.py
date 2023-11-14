from model.entity import Entity
from model.player import Player
from model.character import Character

class Game(Entity):
    """
    Représente une partie d'un set
    """

    def __init__(self):
        self.__id : int = None
        self.__players : [Player] = []
        self.__winnerId : int = None

    # region Properties

    @property
    def Id(self) -> int:
        """
        Getter de l'id de la partie

        Returns:
            int: Id de la partie
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        """
        Setter de l'id de la partie

        Args:
            id (int): Nouvel id de la partie
        """
        self.__id = id

    @property
    def Players(self) -> [Player]:
        """
        Getter de la liste des joueurs de la partie

        Returns:
            [Player]: Liste des joueurs de la partie
        """
        return self.__players
    
    @Players.setter
    def Players(self, players : [Player]) -> None:
        """
        Setter de la liste des joueurs de la partie

        Args:
            players ([Player]): Nouvelle liste des joueurs de la partie
        """
        self.__players = players

    @property
    def WinnerId(self) -> int:
        """
        Getter de l'id du joueur gagnant

        Returns:
            int: Id du joueur gagnant
        """
        return self.__winnerId
    
    @WinnerId.setter  
    def WinnerId(self, winnerId : int) -> None:
        """
        Setter de l'id du joueur gagnant

        Args:
            winnerId (int): Nouvel id du joueur gagnant
        """
        self.__winnerId = winnerId

    # endregion

    # region Operations

    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "selections" in data:
            for selection in data["selections"]:
                chara_data = selection["character"]
                character = Character()
                character.hydrate(chara_data)
                player_data = selection["entrant"]["standing"]["player"]
                player = Player()
                player.hydrate(player_data)
                player.Characters.append(character)
                self.Players.append(player)
                if "winnerId" in data:
                    if (selection["entrant"]["id"] == data["winnerId"]):
                        self.WinnerId = selection["entrant"]["standing"]["player"]["id"]

    def toJSON(self):
        json = {
            "id": self.Id,
            "players": [
                player.toJSON() for player in self.Players
            ],
            "winnerId": self.WinnerId
        }
        return json

    # endregion
