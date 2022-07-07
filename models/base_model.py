

import uuid
import datetime


class BaseModel:

    def __init__(self):
        """
        __init__ = constructor method
        id = identification number
        created_at = date and time when created
        updated_at = date and time when updated

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        class_name = "[{}]".format(type(self).__name__)
        return "{} ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        temp_dict["__class__"] = __class__.__name__
        return temp_dict
