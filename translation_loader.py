import json 

class Translation():
    def __init__(self, input_file):
        self.language = input_file.split('.')[0]

        with open('./translations/' + input_file) as data:
            json_data = json.load(data)
            self.json = json_data

            


        pass