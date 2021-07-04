import json
from pathlib import Path
from greatsoft.common.read_caseInExcel import read_excel_cases
from greatsoft.common.reqmethods import RequestsManager


def run(name):
    # Use a breakpoint in the code line below to debug your script.
    case_file = Path.cwd() / "data" / "Case.xlsx"
    cases_list = read_excel_cases(case_file)
    for case_dict in cases_list:
        id = case_dict["ID"]
        host = case_dict["host"]
        interface = case_dict["interface"]
        method = case_dict["method"]
        header = case_dict["header"]
        datas = case_dict["datas"]
        statue_code = case_dict["statue_code"]
        exp = case_dict["except"]
        url = host + interface
        reqm = RequestsManager(url=url,method=method, data=datas, header=json.loads(header))
        res = reqm.test_api()
        print(res.json())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


