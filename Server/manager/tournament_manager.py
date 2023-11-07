from model.tournament import Tournament
from manager.manager import Manager
from model.videogame import Videogame

class TournamentManager(Manager):
    """
    Classe permettant de gérer les tournois
    """
    def __init__(self):
        super().__init__()

    # region Operations

    def get_tournaments_by_location(self, date : int, videogame : Videogame, coordonnees : str, distance : str) -> [Tournament]:
        response = super().request_api("""
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
        tournaments = []
        for data_tournament in response['data']['tournaments']['nodes']:
            tournament = Tournament()
            tournament.hydrate(data_tournament)
            tournaments.append(tournament)
        return tournaments

    #endregion