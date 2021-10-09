import json

with open('covid_cases.json', 'r') as case:
    try = json.load(case)

print(try)