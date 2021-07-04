import pandas as pd


def read_excel_cases(case_file):
    df = pd.read_excel(case_file)
    cases_list = df.to_dict(orient="reordes")
    return cases_list
