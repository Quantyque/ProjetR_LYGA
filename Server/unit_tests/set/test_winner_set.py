from model.set import Set
from model.player import Player
import unittest

class TestWinnerSet(unittest.TestCase):

    def test_winner_set(self):
        """
        Test if the method returns the winner of the set

        Raises:
            AssertionError: If the method doesn't return the winner of the set
        """
        player = Player()
        player.Id = 1
        player.Name = "test"
        player_b = Player()
        player_b.Id = 2
        player_b.Name = "test_b"
        set = Set()
        set.Players.append(player)
        set.Players.append(player_b)
        set.WinnerId = 1
        self.assertEqual(set.get_winner_looser(player, player_b), (player, player_b), "The winner is not the player 1")
        
