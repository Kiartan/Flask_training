import json

class DataHelper:
    def __init__(self):
        pass
    
    def id_generator(self, last_id):
        i = self.last_id_finder()
        return(i+1)

    def posted_content_writer(self, n, content):
        updated_content={'id': n, 'posted_data': content}
        return(updated_content)

    def json_updater(self, last_id, content):
        new_id = self.id_generator(last_id)
        new_post = self.posted_content_writer(new_id, content)
        with open('data.json', 'r') as f:
            data = json.load(f)
            if type(data) is dict:
                data = [data]
            data.append(new_post)
        with open('data.json', 'w') as j:
            json.dump(data, j, indent = 4)
        return(new_id)
    
    def txt_to_json_transformator(self):
        with open('./test.txt', 'r') as f:            
            txt_content = f.read()
        if txt_content is not None:
            with open('./data.json','w') as j:
                saved_content = self.posted_content_writer(0, txt_content)
                json.dump(saved_content, j, indent = 4)
        return (0)

    def last_id_finder(self):
        with open('data.json', 'r') as f:
            data = json.load(f)
            if type(data) is dict:
                data = [data]
            id_list = [d.get('id', None) for d in data]
            last_id = int(id_list[-1])
            return(last_id)
                