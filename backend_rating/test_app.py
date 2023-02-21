import unittest
from app import app
import model as md
import time
from threading import Thread
from requests import post

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_prediction(self):
        # Succeed in predicting for a test example : score must be better or equal from the previous model
        response = self.app.post('/', json=md.test_predict["params"])
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json["rating"], md.test_predict["result"], "The model performance is worst than the original one")

        # Must at least have one anime information --> return 500
        response = self.app.post('/')
        self.assertEqual(response.status_code, 500)
    
    def test_request_rate(self):
        start_time = time.time()
        threads = []
        num_requests = md.test_stress["time"]
        for i in range(num_requests):
            t = Thread(target=self.__post_data)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        elapsed_time = time.time() - start_time

        self.assertLessEqual(elapsed_time, md.test_stress["time"], "Stress test failed")

    def __post_data(self):
        response = self.app.post('/', json=md.test_predict["params"])
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()