import requests
import json


class RequestsManager(object):
    def __init__(self, url, method, header=None, json_data=None, id=None):
        self.url = url
        self.method = method
        # self.data = data
        self.header = header
        self.json_data = json_data
        self.id = id

    @ staticmethod
    def make_url(case):
        all_url = case["host"] + case["interface"]
        return all_url

    def send_request(self):
        if self.method == "GET":
            response = requests.get(url=self.url, headers= self.header, params=self.json_data)
            return response
        elif self.method == "POST":
            response = requests.post(url=self.url, headers=self.header, json=self.json_data)
            return response
        elif self.method == "DELETE":
            delete_url = self.url + str(self.id)
            response = requests.delete(url=delete_url, headers=self.header)
            return response
        elif self.method == "PUT":
            put_url = self.url + str(self.id)
            response = requests.put(url=put_url, headers=self.header, json=self.json_data)
            return response


# if __name__ == "__main__":
#     url = "http://192.168.1.86:80/qc-engine/v3/sysusers/login"
#     header = {"Content-Type":"application/json"}
#     data = {"userName":"admin","password":"123"}
#     RequestsManager(url=url, method="POST", header=header, data=json.dumps(data)).send_request()