#!/usr/bin/python3
"""
Entry to command console
"""
import cmd



class HBNBCommand(cmd.Cmd):
    """
    class that defines the "entry point of the command interpreter"
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """EOF implementation to close the conse using Ctrl+d"""

        print()
        return True

    def do_quit(self, line):
        """Quit command to close the console"""

        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()