#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class that defines the "entry point of the command interpreter"
    """
    prompt = "(hbnb)"
    classes = {
        "BaseModel", "State", "City",
        "Amenity", "Place", "Review", "User"
    }
