from main import app
import unittest
import json

class TestVideoGames(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_all_videogames_api_start_gg(self):
        """
        Test the route /videogames/all (API START GG)

        Returns:
            None

        Raises:
            AssertionError: If test fails
        """

        # VideoGames get all code 200 : success
        response = self.app.get('/videogames/all')
        self.assertEqual(response.status_code, 200, f'VideoGames (/all): Expected status code 200, but got {response.status_code}')

        # VideoGames get all : data check
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("characters", data[0])

        characters = data[0]["characters"]

        for character in characters:
            self.assertIn("id", character)
            self.assertIn("images", character)
            self.assertIn("name", character)
            self.assertIsInstance(character["images"], list)
            self.assertTrue(character["images"])

    def test_crud_videogames_sql(self):
        """
        Test the route /videogames (CRUD SQL)

        Returns:
            None
        
        Raises:
            AssertionError: If test fails
        """

        # VideoGames get all code 200 : success
        response = self.app.get('/videogames/audited')
        self.assertEqual(response.status_code, 200, f'VideoGames (/audited): Expected status code 200, but got {response.status_code}')

        # VideoGames get all : data check
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("id", data[0])
        self.assertIn("name", data[0])

        try:
            
            # VideoGames add audited code 201 : created
            response = self.app.post('/videogames/add-audited', json={"id": "999", "name": "test"})
            self.assertEqual(response.status_code, 201, f'VideoGames (/add-audited): Expected status code 201, but got {response.status_code}')

            # VideoGames add audited code 409 : conflict
            response = self.app.post('/videogames/add-audited', json={"id": "999", "name": "test"})
            self.assertEqual(response.status_code, 409, f'VideoGames (/add-audited): Expected status code 409, but got {response.status_code}')

            # VideoGames update audited code 200 : success
            response = self.app.put('/videogames/update-audited', json={"id": "999", "name": "test2"})
            self.assertEqual(response.status_code, 200, f'VideoGames (/update-audited): Expected status code 200, but got {response.status_code}')

            # VideoGames update audited code 400 : bad request
            response = self.app.put('/videogames/update-audited', json={"id": "test", "name": ""})
            self.assertEqual(response.status_code, 400, f'VideoGames (/update-audited): Expected status code 400, but got {response.status_code}')

            # VideoGames update audited code 409 : conflict
            response = self.app.put('/videogames/update-audited', json={"id": "999", "name": "test2"})
            self.assertEqual(response.status_code, 409, f'VideoGames (/update-audited): Expected status code 409, but got {response.status_code}')

        finally:

            # VideoGames delete audited code 200 : success
            response = self.app.delete('/videogames/delete-audited', json={"id": "999"})
            self.assertEqual(response.status_code, 200, f'VideoGames (/delete-audited): Expected status code 200, but got {response.status_code}')

            # VideoGames delete audited code 400 : bad request
            response = self.app.delete('/videogames/delete-audited', json={"id": ""})
            self.assertEqual(response.status_code, 400, f'VideoGames (/delete-audited): Expected status code 400, but got {response.status_code}')

            # VideoGames delete audited code 404 : not found
            response = self.app.delete('/videogames/delete-audited', json={"id": "999"})

            # VideoGames delete audited : data check
            data = json.loads(response.get_data(as_text=True))
            self.assertIn("message", data)


        

        

