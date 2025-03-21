import os
import json
import pandas as pd
import re

allure_results_dir = "./result"
test_results = []

for filename in os.listdir(allure_results_dir):
    if filename.endswith(".json"):
        file_path = os.path.join(allure_results_dir, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            test_case = {
                "name": data.get("name"),
                "status": data.get("status"),
                # "start_time": data.get("start"),
                # "stop_time": data.get("stop"),
                # "duration": data.get("stop") - data.get("start") if data.get("start") and data.get("stop") else None,
                # "case_name": [data.get('parameters') for  casename in data.get("labels", [])]
                "case_name": data.get('parameters')[0]['value']
                # "labels": [label.get("value") for label in data.get("labels", [])],
                # "failure": data.get("statusDetails", {}).get("message")
            }
            print(test_case)
            # test_results.append(test_case)


# df = pd.DataFrame(test_results)
# print(df)

# 保存为 CSV 文件（可选）
# df.to_csv("allure_test_results.csv", index=False)