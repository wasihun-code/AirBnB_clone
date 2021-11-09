#!/usr/bin/python3
"""Documentation for the consule module"""


import cmd
class HBNBCommand(cmd.Cmd):
    """Documentation for the console class which uses cCmd
    public class which is used for command line purpose."""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Function for handling End of file or end of line"""
        return True

    def postloop(self):
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
