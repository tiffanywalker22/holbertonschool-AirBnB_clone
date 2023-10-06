#!/usr/bin/python3
# console.py
# Tiffany Walker and Ethan Zalta
""" the console """

import cmd


class HBNBCommand(cmd.Cmd):
    """prompt for cmd interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits program using ctrl+d (EOF)"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
