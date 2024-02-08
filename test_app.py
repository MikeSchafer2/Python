# test_app.py

import unittest
from app import app, db


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def tearDown(self):
        pass



    def test_home(self):

        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data, b'Hello, World!')



if __name__ == '__main__':

    unittest.main()