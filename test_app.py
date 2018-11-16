import unittest

from app import app as a
import app

class TestConference(unittest.TestCase):

    def test_conference(self):
        self.test_app = a.test_client()
        response = self.test_app.get("http://localhost:5000/hello/<name>")
        self.assertEquals(response.status, "200 OK")


    #def test_two(self):
        #response = self.test_app.get('http://localhost:5000/hello/ruben', SERVER_NAME="localhost")
        #self.assertEqual(result, "localhost")

if __name__ == "__main__":
    unittest.main()
