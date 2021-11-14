#!/usr/bin/python3
"""Documentation for the consule module"""


import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Documentation for the console class which uses cCmd
    public class which is used for command line purpose."""

    prompt = '(hbnb) '
    argv = sys.argv[1:]

    def do_create(self, name):
        if name:
            name = BaseModel()
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(name, f)
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in FileStorage.__file_path.items():
                    if (key == "id"):
                        print(value)
        else:
            print("**class name missing **")

    def do_show(self):
        pass

    def do_EOF(self, line):
        """Function for handling End of file or end of line"""
        return True

    def do_quit(self, line):
        """Function to implement clean exit"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
