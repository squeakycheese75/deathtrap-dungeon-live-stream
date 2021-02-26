import json 
data = {}

with open('./src/content.json') as f:
    data = json.load(f)

def get_page(page_number: int):
    for p in data['pages']:
        if p['page'] == page_number:
            return p
    return {}



# resval = get_page(1)
# print(resval['narrative'])