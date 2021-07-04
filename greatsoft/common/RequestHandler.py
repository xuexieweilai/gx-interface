import requests


class RequestsManager(object):
    def __init__(self, url, method, data=None, header=None, jsonD=None):
        self.url = url
        self.method = method
        self.data = data
        self.header = header
        self.jsonD = jsonD

    @ staticmethod
    def make_url(case):
        all_url = case["host"] + case["interface"]
        return all_url

    def send_request(self):
        if self.method == "GET":
            response = requests.get(url=self.url, headers= self.header, params=self.data)
            return response
        elif self.method == "POST":
            response = requests.post(url=self.url, headers=self.header, data=self.data)
            return response


