#!/usr/bin/python3
"""console of the clone app"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command class to take in commands"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """Exit the interpreter when Ctrl+D is pressed"""
        return

    def emptyline(self):
        pass

    def help(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
