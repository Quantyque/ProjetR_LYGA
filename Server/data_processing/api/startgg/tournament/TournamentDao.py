from data_processing.api.startgg.tournament.ITournamentDao import ITournamentDao
from model.tournament import Tournament
from model.videogame import Videogame
from data_processing.api.startgg.StartGGDao import StartGGDao
from data_processing.api.IApiDao import IApiDao
from exceptions import BadRequestException

class TournamentDao(ITournamentDao):

    def __init__(self) -> None:
        self.__api: IApiDao = StartGGDao()

    def get_tournaments_by_location(self, date : int, videogame : Videogame, coordonnees : str, distance : str) -> [Tournament]:
        """
        Récupère les tournois à une date et un jeu vidéo donnés.

        Args:
            date (int): La date.
            videogame (Videogame): Le jeu vidéo.

        Returns:
            [Tournament]: La liste des tournois.

        Raises:
            Exception: Si la requête échoue.
        """
        response = self.__api.request_api("""
                    query TournamentsAtLocation($afterDate : Timestamp!, $videogameId: ID!, $coordonnees : String!, $distance : String!) {
                        tournaments(
                            query: {filter: {past: true, videogameIds: [$videogameId], afterDate : $afterDate, location: {distanceFrom: $coordonnees, distance: $distance}}}
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
                            "afterDate": date,
                            "videogameId": videogame.Id,
                            "coordonnees" : coordonnees,
                            "distance" : distance
                        })
        
        if response["errors"]:
            raise BadRequestException(response["errors"][0]["message"])
        
        print(response)

        tournaments = []
        for data_tournament in response['data']['tournaments']['nodes']:
            tournament = Tournament()
            tournament.hydrate(data_tournament)
            tournaments.append(tournament)
        return tournaments