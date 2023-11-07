from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from controls.technical import TechnicalControls
from model.role import Role

# Tournaments
from views.view_tournaments import ViewTournament

# Videos games
from views.view_video_game import ViewVideoGames

# Ranking
from views.view_ranking import ViewRanking

# Players
from views.view_player import ViewPlayer

#Sets
from views.view_set import ViewSet

# Users
from views.view_user import ViewUser

# Tests
from views.view_api_tests import ViewApiTests

#Elos
from views.view_elo import ViewElo

# App init
app = Flask(__name__)

# CORS definition
CORS(app, resources={r"/*": {"origins": ["*"]}})

# Request limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per second"],
    storage_uri="memory://",
)

# Views init
ViewVideoGames.register(app, route_base='/videogames', trailing_slash=False)
ViewPlayer.register(app, route_base='/player', trailing_slash=False)
ViewRanking.register(app, route_base='/rankings', trailing_slash=False)
ViewTournament.register(app, route_base='/tournaments', trailing_slash=False)
ViewUser.register(app, route_base='/user', trailing_slash=False)
ViewSet.register(app, route_base='/sets', trailing_slash=False)
ViewElo.register(app, route_base='/elo', trailing_slash=False)
ViewApiTests.register(app, route_base='/tests', trailing_slash=False)

# Launch app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)