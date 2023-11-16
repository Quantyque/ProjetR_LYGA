from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from controls.technical import TechnicalControls
from model.role import Role
from views.view_tournaments import ViewTournament
from views.view_video_game import ViewVideoGames
from views.view_ranking import ViewRanking
from views.view_player import ViewPlayer
from views.view_set import ViewSet
from views.view_user import ViewUser
from views.view_api_tests import ViewApiTests
from views.view_elo import ViewElo
from views.view_season import ViewSeason

# Initialisation de l'application Flask
app = Flask(__name__)

# CORS definition
CORS(app, resources={r"/*": {"origins": ["*"]}})

# Limiteur de requêtes
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per second"],
    storage_uri="memory://",
)

# Initialisation des vues
ViewVideoGames.register(app, route_base='/videogames', trailing_slash=False)
ViewPlayer.register(app, route_base='/player', trailing_slash=False)
ViewRanking.register(app, route_base='/rankings', trailing_slash=False)
ViewTournament.register(app, route_base='/tournaments', trailing_slash=False)
ViewUser.register(app, route_base='/user', trailing_slash=False)
ViewSet.register(app, route_base='/sets', trailing_slash=False)
ViewElo.register(app, route_base='/elo', trailing_slash=False)
ViewApiTests.register(app, route_base='/tests', trailing_slash=False)
ViewSeason.register(app, route_base='/season', trailing_slash=False)

# Lancement de l'application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)