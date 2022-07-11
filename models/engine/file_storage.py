
import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, object):
        my_id = str(object.id)
        class_name = str(type(object).__name__)
        my_key = f"{class_name}.{my_id}"

        self.__objects[my_key] = object

    def reload(self):
        try:
            with open(self.__file_path,"r", encoding="utf-8") as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def save(self):
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(my_dict, file)
