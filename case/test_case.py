import pytest
from greatsoft.common.ExcelHandler import excel_handler, wirte_testresult_to_report
import pathlib
from greatsoft.common.RequestHandler import RequestsManager
import json
import requests
from greatsoft.db_connection.engine import Engine
from greatsoft.utils.logHandler import Logger



case_file = pathlib.Path.cwd().parent / "data" / "Case.xlsx"
test_reports_path = pathlib.Path.cwd().parent / "reports"

class Test_Case(object):
    @ pytest.mark.parametrize("case", excel_handler(case_file, sheet_name="login"))
    def test_login_interface(self, case):
        """ 用户登录接口测试 """
        # logger.info("Case Id[%s]" %(case["ID"]))
        # logger.info("Case title[%s]" % (case["title"]))
        url = RequestsManager.make_url(case)
        data = case["json_data"] if case["json_data"] else None
        json_data = json.loads(data)
        header = case["header"] if case["header"] else None
        reqm = RequestsManager(url=url, method=case["method"], json_data=json_data, header=json.loads(header))
        res = reqm.send_request()
        if case["ID"] == 1:
            # assert "token" in res.json().keys()
            if "token" in res.json().keys():
                to_excel_result =
                wirte_testresult_to_report(result="PASS", test_reports_path=test_reports_path, sheet_name="lofin")
        else:
            assert res.json()["message"] == case["except"]


    @ pytest.mark.parametrize("case", excel_handler(case_file, sheet_name="sysusers"))
    def test_sysusers_interface(self, case, header):
        """ 添加，查询，修改 用户 接口 """
        url = RequestsManager.make_url(case)
        data = case["json_data"] if case["json_data"] else None
        json_data = json.loads(data)
        header = header
        if case["ID"] < 4:
            reqm = RequestsManager(url=url, method=case["method"], json_data=json_data, header=header)
            res = reqm.send_request()
            if case["ID"] == 1 :
                assert res.json()["message"] == case["except"]
            elif case["ID"] == 2:
                assert res.json()["message"] == case["except"]
            elif case["ID"] == 3:
                assert res.json()["datas"][0]["userName"] == case["except"] and res.status_code == 200
        if case["ID"] >= 4:
            userName = json.loads(case["json_data"])["userName"]
            userId = Engine().get_userId_by_userName(userName)
            reqm = RequestsManager(url=url, method=case["method"], header=header, id=userId, json_data=json_data)
            res = reqm.send_request()
            assert res.text == "成功"


    @ pytest.mark.parametrize("case", excel_handler(case_file, sheet_name="delete"))
    def test_deleteUser_interface(self, case, header):
        userName = json.loads(case["json_data"])["userName"]
        userId = Engine().get_userId_by_userName(userName)
        url = RequestsManager.make_url(case)
        method = case["method"]
        header = header
        response = RequestsManager(url=url, header=header,method=method, id=userId).send_request()
        assert response.status_code == 200



if __name__ == "__main__":
    logger = Logger("System Manager Model")
    print(logger)