import unittest

from app import app


class AppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get("/add/10/20")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 30)


if __name__ == "__main__":
    unittest.main()

    