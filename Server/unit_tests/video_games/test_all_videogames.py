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
        result, status_code = video_games_view.all_video_games()
        self.assertEqual(status_code, 200, f'Expected status code 200, but got {status_code}')

    def test_returns_all_video_games(self):
        """
        Test if the method returns all video games

        Returns:
            None

        Raises:
            AssertionError: If the method doesn't return all video games
        """
        view_games = ViewVideoGames()
        result = view_games.all_video_games()

        self.assertIsInstance(result, tuple, f"The object is not an instance of tuple: {type(result)}")

        data_list = result[0]
        self.assertIsInstance(data_list, list, f"The object is not an instance of list: {type(data_list)}")
        self.assertNotEqual(len(data_list), 0, "The list is empty (length is 0)")

        for item in data_list:
            self.assertIsInstance(item, dict, f"The item is not an instance of dict: {type(item)}")

