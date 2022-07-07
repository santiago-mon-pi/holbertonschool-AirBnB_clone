from base64 import encode
from encodings import utf_8
import json
from multiprocessing.sharedctypes import Value
from optparse import Values


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = dict()
    
    def all(self):
        return self.__objects


    def new(self, object):
        my_id = str(object.id)
        class_name = str(type(object).__name__)
        my_key = f"{class_name}.{my_id}"

        self.__objects[my_key] = object

    def reload(self):
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                json_data = json.loads(file.read())
                for key, value in json_data.items():
                    class_name = value["__class__"]
                    self.__objects[key] = globals()[class_name](**value)
        except Exception:
            pass
    

    def save(self):
        my_dict = dict()
        for key, value in self.__objects.items():
            my_obj = value.to_dict()
            my_dict[key] = my_obj
        data_json = json.dumps(my_dict)
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(data_json)
            
