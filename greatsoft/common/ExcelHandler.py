import pandas as pd
from pandas import DataFrame


def excel_handler(case_file, sheet_name):
    df = pd.read_excel(case_file, sheet_name=sheet_name)
    cases_list = df.to_dict(orient="records")
    return cases_list




def wirte_testresult_to_report(result, test_reports_path, sheet_name):
    data = {"test_result": [result]}
    report = test_reports_path / "report.xlsx"
    df = DataFrame(data)
    df.to_excel(report, sheet_name=sheet_name)
