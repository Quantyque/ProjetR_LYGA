from model.set import Set
from model.player import Player
from model.ranking import Ranking
from model.elo import Elo
from model.videogame import Videogame
from model.season import Season
import unittest

class TestRanking(unittest.TestCase):

    def test_new_elo(self):
        """
        Test if the elo of the winner as raised and the elo of the loser has decreased

        Raises:
            AssertionError: If the elo of the winner as not raised and the elo of the loser has not decreased
        """
        player_a = Player()
        player_a.Id = 1
        player_a.Name = "test"
        player_a.Elos[0] = Elo()
        player_a.Elos[0].Score = 1000
        player_b = Player()
        player_b.Id = 2
        player_b.Name = "test_b"
        player_b.Elos[0]= Elo()
        player_b.Elos[0].Score = 1000
        set = Set()
        set.Players.append(player_a)
        set.Players.append(player_b)
        set.WinnerId = 1
        set.Round = 1
        set.EventNbEntrants = 1
        ranking = Ranking([])
        elo_player_a, elo_player_b = ranking.get_new_elo(player_a, player_b, set, 0)
        self.assertTrue(elo_player_a > player_a.Elos[0].Score, "The elo of the winner has not increased")
        self.assertTrue(elo_player_b < player_b.Elos[0].Score, "The elo of the loser has not decreased")

    def test_init_players(self):
        """
        Test if the player is initialized correctly

        Raises:
            AssertionError: If the player is not initialized correctly
        """
        player_a = Player()
        player_a.Id = 6141
        player_a.Name = "test"
        players = {}
        players[player_a.Id] = player_a
        ranking = Ranking([])
        videogame = Videogame()
        videogame.Id = 0
        season = Season()
        season.Id = 1
        ranking.init_players(player_a, videogame, season)
        self.assertTrue(player_a.Id in ranking.Players, "The player has not been initialized")
        self.assertTrue(0 in player_a.Elos, "The player has not been initialized")
        self.assertEqual(player_a.Elos[0].Score, 1000, "The player has not been initialized")