from main import app
import unittest
import json

class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_all_user(self):
        """
        Test the route /get-all

        Returns:
            None

        Raises:
            AssertionError: If test fails
        """

        #  User get all code 200 : success
        response = self.app.get('/user/get-all')
        self.assertEqual(response.status_code, 200, f'User (/get-all) : Expected status code 200, but got {response.status_code}')

    def test_crud_user(self):
        """
        Test the route /register

        Returns:
            None

        Raises:
            AssertionError: If test fails
        """
        try :
            # User register code 201 : success
            response = self.app.post('/user/register', json={"username": "abcdefg", "password": "abcdefg", "confirm_password": "abcdefg"})
            self.assertEqual(response.status_code, 201, f'User (/register): Expected status code 201, but got {response.status_code}')

            # User register code 400 : password and confirm_password are different
            response = self.app.post('/user/register', json={"username": "abcdefg", "password": "abcdefg", "confirm_password": "abcdef"})
            self.assertEqual(response.status_code, 400, f'User (/register): Expected status code 400, but got {response.status_code}')

            # User register code 409 : username already exists
            response = self.app.post('/user/register', json={"username": "abcdefg", "password": "abcdefg", "confirm_password": "abcdefg"})
            self.assertEqual(response.status_code, 409, f'User (/register): Expected status code 409, but got {response.status_code}')

            # User login code 200 : success
            response = self.app.post('/user/login', json={"username": "abcdefg", "password": "abcdefg"})
            self.assertEqual(response.status_code, 200, f'User (/login): Expected status code 200, but got {response.status_code}')

            # Get user id
            data = json.loads(response.get_data(as_text=True))
            userId = data['id']

            # User login code 401 : username does not exist
            response = self.app.post('/user/login', json={"username": "abcdef", "password": "abcdefg"})
            self.assertEqual(response.status_code, 401, f'User (/login): Expected status code 401, but got {response.status_code}')

            # User login code 401 : password is incorrect
            response = self.app.post('/user/login', json={"username": "abcdefg", "password": "abcdef"})
            self.assertEqual(response.status_code, 401, f'User (/login): Expected status code 401, but got {response.status_code}')

            # User update code 200 : success
            response = self.app.put('/user/update', json={"id": userId, "role": 0, "username": "abc", "userPP": "https://icons.veryicon.com/png/o/miscellaneous/two-color-icon-library/user-286.png"})
            self.assertEqual(response.status_code, 200, f'User (/update): Expected status code 200, but got {response.status_code}')

            # User update code 400 : username already exists
            response = self.app.put('/user/update', json={"id": userId, "role": 0, "username": "abc", "userPP": "https://icons.veryicon.com/png/o/miscellaneous/two-color-icon-library/user-286.png"})
            self.assertEqual(response.status_code, 409, f'User (/update): Expected status code 409, but got {response.status_code}')

            # User update code 404 : user not found
            response = self.app.put('/user/update', json={"id": 0, "role": 0, "username": "abc", "userPP": "https://icons.veryicon.com/png/o/miscellaneous/two-color-icon-library/user-286.png"})
            self.assertEqual(response.status_code, 404, f'User (/update): Expected status code 404, but got {response.status_code}')

        finally:

            # User delete code 200 : success
            response = self.app.delete('/user/delete', json={"id": userId})
            self.assertEqual(response.status_code, 200, f'User (/delete): Expected status code 200, but got {response.status_code}')

            # User delete code 404 : user not found
            response = self.app.delete('/user/delete', json={"id": userId})
            self.assertEqual(response.status_code, 404, f'User (/delete): Expected status code 404, but got {response.status_code}')

    def test_get_user_by_id(self):
        """
        Test the route /get-by-id

        Returns:
            None

        Raises:
            AssertionError: If test fails
        """

        # User get by id code 200 : success
        response = self.app.post('/user/get-by-id', json={'id': 1})
        self.assertEqual(response.status_code, 200, f'User (/get-by-id): Expected status code 200, but got {response.status_code}')

        # User get by id code 404 : user not found
        response = self.app.post('/user/get-by-id', json={'id': 0})
        self.assertEqual(response.status_code, 404, f'Expected status code 404, but got {response.status_code}')
