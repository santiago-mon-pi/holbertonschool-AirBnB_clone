#!/usr/bin/python3
"""
Entry to command console
"""
from datetime import datetime
from models.base_model import BaseModel
from models.__init__ import storage
import cmd

class_name_obj = {
    "BaseModel": BaseModel
}

class HBNBCommand(cmd.Cmd):
    """
    class that defines the "entry point of the command interpreter"
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """EOF implementation to close the conse using Ctrl+d"""

        return True

    def do_quit(self, line):
        """Quit command to close the console"""

        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        gv = line.split()
        gc = len(line)
        if gc == 0:
            print("** class name missing **")
        else:
            if gv[0] in class_name_obj:
                instance = class_name_obj[gv[0]]()
                storage.new(instance)
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        gv = line.split()
        gc = len(line)

        all_instance = storage.all()
        if gc == 0:
            new_instance = []
            for key, obj in all_instance.items():
                new_instance.append(str(obj))
            print(new_instance)
            return

        if gv[0] not in class_name_obj:
            print("** class doesn't exist **")
            return
        else:
            new_list = []
            for key, obj in all_instance.items():
                if gv[0] == type(obj).__name__:
                    new_list.append(str(obj))
            print(new_list)

    def do_show(self, line):
        gv = line.split()
        gc = len(line)

        my_flag = False

        if gc == 0:
            print("** class name missing **")
            return

        if gv[0] not in class_name_obj:
            print("** class doesn't exist **")
            return

        if gc == 1:
            print("** instance id missing **")
            return

        my_instances = storage.all()
        key = f"{gv[0]}.{gv[1]}"

        if key in my_instances.keys():
            print(my_instances[key])
        else:
            print("** no instace found **")

    def do_destroy(self, line):
        gv = line.split()
        gc = len(line)
        if gc == 0:
            print("** class name missing **")
            return
        
        if gv[0] not in class_name_obj:
            print("** class doesn't exist **")
            return
        
        if gc == 1:
            print("** instance id missing **")
            return
        
        my_instances = storage.all()
        key = f"{gv[0]}.{gv[1]}"

        if key in my_instances.keys():
            del my_instances[key]
            storage.save()
            return
        else:
            print("** no instance found **")
        
    def do_update(self, line):
        gv = line.split()
        gc = len(line)

        if gc == 0:
            print("** class name missing **")
            return
        
        if gv[0] not in class_name_obj:
            print("** class doesn't exist **")
            return
        
        if gc == 1:
            print("** instance id missing **")
            return

        my_instances = storage.all()
        key = f"{gv[0]}.{gv[1]}"
        
        if key in my_instances.keys():
            obj_ref = my_instances[key]

            if gc == 2:
                print("** attribute name missing **")
                return
            elif gc == 3:
                print("** value missing **")
                return
            else:
                obj_ref.__dict__[gv[2]] = gv[3][1:-1]
                obj_ref.updated_at = datetime.now()
                storage.save()
        else:
            print("** no instace found **")
            return

if __name__ == "__main__":
    HBNBCommand().cmdloop()