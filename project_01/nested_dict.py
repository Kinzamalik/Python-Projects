
import json
with open("./mapping_company_house.json", "r") as f:
    data = json.load(f)
    print(data)
for employee in data["UK_company_house"]:
    print(employee["index"], employee["colName"])

