import sys
import json

print("######################################")
print("########### JSON ###################")
print("######################################")
with open('db.json', 'r') as f:
    db_dict = json.load(f)
    print(db_dict)