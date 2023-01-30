import json


def uk_company_house():
    file = open('test_UK_Company_House_Data.json')
    data = file.read()
    test_uk_company_house = json.loads(data)
    empty_dict = []
    for i in test_uk_company_house:
        try:
            confirmation_statement_next_made_up_to = i["confirmation_statement"]["next_made_up_to"]
            confirmation_statement_next_due = i["confirmation_statement"]["next_due"]
            previous_company_names_name = [i["previous_company_names"][x]["name"] for x in range(len(i["previous_company_names"]))]
        except KeyError:
            confirmation_statement_next_made_up_to = None
            confirmation_statement_next_due = None
            previous_company_names_name = None

        data = {
            "id": i["etag"],
            "company_number": i["company_number"],
            "confirmation_statement.next_made_up_to": confirmation_statement_next_made_up_to,
            "confirmation_statement.next_due": confirmation_statement_next_due,
            "company_name": i["company_name"],
            "previous_company_names.name": previous_company_names_name,
            "accounts.last_accounts.period_end_on": i["accounts"]["last_accounts"]["period_end_on"],
            "jurisdiction": i["jurisdiction"],
            "registered_office_address.locality": i["registered_office_address"]["locality"],
            "registered_office_address.country": i["registered_office_address"]["country"]
        }
        empty_dict.append(data)
    return empty_dict

print(uk_company_house())
