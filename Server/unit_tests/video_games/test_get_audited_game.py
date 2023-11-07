from views.view_video_game import ViewVideoGames
import unittest

class TestAllVideoGames(unittest.TestCase):

    def test_returns_status_code_200(self):
        """
        Test if the method returns status code 200

        Returns:
            None

        Raises:
            AssertionError: If the method doesn't return status code 200
        """
        video_games_view = ViewVideoGames()
        result, status_code = video_games_view.get_audited_game()
        self.assertEqual(status_code, 200, f'Expected status code 200, but got {status_code}')