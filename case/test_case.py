import pytest
from greatsoft.common.ExcelHandler import excel_handler
import pathlib
from greatsoft.common.RequestHandler import RequestsManager

case_file = pathlib.Path.cwd().parent / "data" / "Case.xlsx"
# print(excel_handler(case_file))

class Test_case(object):
    @ pytest.mark.parametrize("case", excel_handler(case_file))
    def test_case(self, case):
        url = RequestsManager.make_url(case)
        datas =case["datas"] if case["datas"] else None
        header = case["header"] if case["header"] else None
        response = RequestsManager(url=url, method=case["method"], data=datas, header=json.loads(header))

if __name__ == "__main__":
    Test_case().test_case()