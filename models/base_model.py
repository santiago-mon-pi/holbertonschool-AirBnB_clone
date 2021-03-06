

import uuid
import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    def __init__(self, **kwargs):
        """
        __init__ = constructor method
        id = identification number
        created_at = date and time when created
        updated_at = date and time when updated

        """
        if kwargs:
            """Sets all attributes except class"""
            for k, value in kwargs.items():
                if k != "__class__":
                    setattr(self, k, value)

            if kwargs.get("created_at", None) and type(self.created_at) is str:
                get_d = datetime.datetime.strptime(kwargs["created_at"], time_format)
                self.created_at = get_d
            else:
                self.created_at = datetime.datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                get_d = datetime.datetime.strptime(kwargs["updated_at"], time_format)
                self.updated_at = get_d
            else:
                self.updated_at = datetime.datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid.uuid4())

            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        class_name = "[{}]".format(type(self).__name__)
        return "{} ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        temp_dict = self.__dict__.copy()
        if "created_at" in temp_dict:
            set_d = temp_dict["created_at"].strftime(time_format)
            temp_dict["created_at"] = set_d

        if "updated_at" in temp_dict:
            set_d = temp_dict["updated_at"].strftime(time_format)
            temp_dict["updated_at"] = set_d

        temp_dict["__class__"] = __class__.__name__

        return temp_dict
