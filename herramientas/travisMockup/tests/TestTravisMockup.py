import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import TravisMockup

import unittest
import requests
import time
from threading import Thread

class TestTravisMockup(unittest.TestCase):

    def test_has_valid_headers_with_headers_invalid(self):
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token asdasdasd"
        }

        valid = TravisMockup.has_valid_headers(headers)

        self.assertEqual(False, valid)

    def test_has_valid_headers_with_headers_valid(self):
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token " + TravisMockup.VALID_TOKEN
        }

        valid = TravisMockup.has_valid_headers(headers)

        self.assertEqual(True, valid)
    
    def test_generate_build_state(self):
        TravisMockup.set_build_satus("passed")

        state = TravisMockup.generate_build_state()

        self.assertEqual("passed", state["builds"][0]["state"])

    def test_response_with_status(self):
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token " + TravisMockup.VALID_TOKEN
        }
        url = TravisMockup.SERVER_DOMAIN + ":" + str(TravisMockup.PORT) + "/repo/"+ TravisMockup.USERNAME +"%2F"+ TravisMockup.REPOSITORY + "/builds?limit=1&sort_by=finished_at:desc"
        response = requests.get(url, headers=headers)
        state = (response.json())["builds"][0]["state"]

        self.assertEqual("passed", state)

    def test_response_access_denied(self):
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token asdasdsad"
        }
        url = TravisMockup.SERVER_DOMAIN + ":" + str(TravisMockup.PORT) + "/repo/"+ TravisMockup.USERNAME +"%2F"+ TravisMockup.REPOSITORY + "/builds?limit=1&sort_by=finished_at:desc"
        response = requests.get(url, headers=headers)
        state = response.text

        self.assertEqual("access denied", state)


if __name__ == '__main__':
    thread = Thread(target=TravisMockup.run_app,args=[])
    #PARA QUE MUERA EL THREAD CUANDO FINALIZA EL PROGRAMA
    thread.daemon = True
    thread.start()
    #ESPERAMOS 5 SEGUNDOS PARA QUE INICIE LA API
    time.sleep(5)
    unittest.main()