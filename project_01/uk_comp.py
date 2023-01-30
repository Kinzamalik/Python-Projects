import json

file=open("./test_UK_Company_House_Data.json","r")
read_file=file.read()
finalData=json.loads(read_file)
# print(finalData)

for data in finalData:
    print(data['company_number'],data['company_name'])
    