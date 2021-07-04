import pandas as pd


def excel_handler(case_file):
    df = pd.read_excel(case_file)
    cases_list = df.to_dict(orient="records")
    # cases_list = [{}, {}, {}]
    return cases_list
