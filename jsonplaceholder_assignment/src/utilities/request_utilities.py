import requests
import os
import logging as logger
from jsonplaceholder_assignment.src.configs.api_hosts import API_HOSTS


class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'prod')
        self.base_url = API_HOSTS[self.env]

    def get(self, endpoint, headers=None, data=None):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        r = requests.get(url=self.url, data=data, headers=headers)
        logger.info("GET API response: {}".format(r))

        return r

    def post(self, endpoint, payload, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        r = requests.post(url=self.url, data=payload, headers=headers)
        logger.info("POST API response: {}".format(r))

        return r

