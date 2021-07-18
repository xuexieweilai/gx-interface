import pytest
import requests
import json


def get_token():
    url = "http://192.168.1.86:80/qc-engine/v3/sysusers/login"
    header = {"Content-Type":"application/json"}
    data = {"userName":"admin","password":"123"}
    response = requests.post(url=url, json=data, headers=header)
    token = response.json()["token"]
    return token


@ pytest.fixture(scope="session")
def header():
    return {"X-Access-Token": get_token()}




if __name__ == "__main__":
    get_token()