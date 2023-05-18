from data_helper import DataHelper
import os.path
import json

#n = 5
#a = n + 1
content = "test 8"
requested_id = 1
req_id = int(requested_id)

data_helper = DataHelper()
with open('data.json', 'r') as f:
    stored_data = json.load(f)
if type(stored_data) is dict:
    stored_data = [stored_data]
searched_data = next(iter(item for item in stored_data if item['id'] == req_id), None)
print(searched_data)