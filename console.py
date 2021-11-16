#!/usr/bin/python3
"""Documentation for console"""


import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """conole class using cmd public class for CLI"""

    prompt = '(hbnb) '
    classes = ["Ameenity", "User"]

    def do_create(self, name):
        """Create module"""
        if name:
            name = BaseModel()
            with open(FileStorage.__file_path, 'w') as f:
                json. dump(name, f)
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in FileStorage.__file_path.items():
                    if (key == "id"):
                        print(value)
        else:
            print("** class name missing **")

    def do_show(self):
        pass

    def do_EOF(self, line):
        """Handling end of ile"""
        return True

    def do_quit(self, line):
        """handling quit"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
