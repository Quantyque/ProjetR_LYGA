import json

class Entity:
    """
    Classe abstraite représentant une entité de l'application
    """
    def hydrate(self, data : dict) -> None:
        """
        Initialise la variable self avec les données du dictionnaire data

        Args:
            data (dict): Dictionnaire contenant les données à hydrater
        """
        pass

    def toJSON(self) -> dict:
        """
        Convertit l'objet en JSON

        Returns:
            dict[str, str]: Objet convertit en JSON
        """
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)