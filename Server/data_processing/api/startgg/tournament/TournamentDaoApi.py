from data_processing.api.startgg.tournament.ITournamentDaoApi import ITournamentDaoApi
from model.tournament import Tournament
from model.videogame import Videogame
from exceptions import BadRequestException
from data_processing.api.api import Api

class TournamentDaoApi(ITournamentDaoApi, Api):

    def __init__(self) -> None:
        super().__init__()

    def get_tournaments_by_location(self, afterDate : int, beforeDate : int, videogame : Videogame, coordonnees : str, distance : str) -> [Tournament]:
        """
        Récupère les tournois à une date et un jeu vidéo donnés.

        Args:
            afterDate (int): La date a partir de laquelle rechercher les tournois.
            beforeDate (int): La date jusqu'à laquelle rechercher les tournois.
            videogame (Videogame): Le jeu vidéo.
            coordonnees (str): coordonnees de la localisation des tournois à récupérer
            distance (str): distance de la localisation des tournois à récupérer

        Returns:
            [Tournament]: La liste des tournois.

        Raises:
            Exception: Si la requête échoue.
        """
        # Récupération des tournois
        response = self.sg.request_api("""
                    query TournamentsAtLocation($afterDate : Timestamp!, $beforeDate : Timestamp!, $videogameId: ID!, $coordonnees : String!, $distance : String!) {
                        tournaments(
                            query: {filter: {past: true, videogameIds: [$videogameId], afterDate : $afterDate, beforeDate: $beforeDate, location: {distanceFrom: $coordonnees, distance: $distance}}}
                        ) {
                            nodes {
                            id
                            name
                            owner{
                                name
                            }
                            lat
                            lng
                            events(filter: {}) {
                                id
                                name
                                numEntrants
                                tournament {
                                    id
                                    name
                                }
                                videogame{
                                    id
                                    name
                                }
                            }
                            }
                        }
                        }
                        """, {
                            "afterDate": afterDate,
                            "beforeDate": beforeDate,
                            "videogameId": videogame.Id,
                            "coordonnees" : coordonnees,
                            "distance" : distance
                        })
        
        # Gestion des erreurs
        if "errors" in response:
            raise BadRequestException(response["errors"][0]["message"])

        # Ajout des tournois à la liste
        tournaments = []
        for data_tournament in response['data']['tournaments']['nodes']:
            tournament = Tournament()
            tournament.hydrate(data_tournament)
            tournaments.append(tournament)
        return tournaments