#!/usr/bin/python3

"""
This Module Defines Unittest for Console command interpreter.
Unittest classes:
    TestHBNBCommand_prompt
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import models from storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
