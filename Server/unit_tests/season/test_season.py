from model.set import Set
from model.player import Player
from model.ranking import Ranking
from model.elo import Elo
from model.videogame import Videogame
import unittest
from data_processing.sql.season.SeasonDaoSql import SeasonDaoSql

class TestSeason(unittest.TestCase):

    def test_current_season(self):
        """
        Test if the current season is the right one

        Raises:
            AssertionError: If the current season is not the right one
        """
        season_dao_sql = SeasonDaoSql()
        current_season = season_dao_sql.get_current_season()
        print("GROS VAAVAVJEH")
        self.assertEqual(current_season.Id, 1, "The current season is not the right one")