#!/usr/bin/python3
"""console of the clone app"""
import cmd
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """command class to take in commands"""

    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel
    }
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """handles the end if file (ctrl+D)"""
        print()
        return True

    def emptyline(self):
        pass

    def help(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split(" ")
        class_name = arg_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        key = f"{arg_list[0]}.{arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()
    
    def do_all(self, arg):
        """Prints all string representation of all instances"""

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        instances = []

        args_list = arg.split(" ")

        class_name = args_list[0]

        key = f"{args_list[0]}"
        if not arg:
            for class_name in self.classes:
                instances.extend(storage.all()[key])
        else:
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            instances.extend(storage.all()[key])

        print(instances)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
