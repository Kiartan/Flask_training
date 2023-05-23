import json


def find_last_id():
    with open('test.json', 'r') as f:
        data = json.load(f)
        if type(data) is dict:
            data = [data]
        id_list = [d.get('id', None) for d in data]
        last_id = int(id_list[-1])
        return(last_id)

def write_posted_content(n, content):
    #updated_content={'id': n, 'posted_data': content}
    updated_content={n: {'posted_data': content}}
    return(updated_content)

def update_json(last_id, content):
    new_id = last_id + 1
    new_post = write_posted_content(new_id, content)
    with open('test.json', 'r') as f:
        data = json.load(f)
        if type(data) is dict:
            data = [data]
        data.append(new_post)
    with open('test.json', 'w') as j:
        json.dump(data, j, indent = 3)
    return(new_id)
    
def transform_txt_to_json():
    with open('./test.txt', 'r') as f:            
        txt_content = f.read()
    if txt_content is not None:
        with open('./test.json','w') as j:
            saved_content = write_posted_content(0, txt_content)
            json.dump(saved_content, j, indent = 3)
    init_id = int(0)
    return(init_id)
    
def find_requested_data(req_id):
    #searched_id = int(req_id)
    with open('test.json', 'r') as f:
        stored_data = json.load(f)
    #requested_data = next(iter(item for item in stored_data if item['id'] == searched_id), None)
    for i in stored_data:
        if i == req_id:
            return(i['posted_data'])
    #return(requested_data)


                