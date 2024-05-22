#!/usr/bin/python3
"""console of the clone app"""
import cmd
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """command class to take in commands"""

    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
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
        """Prints all string representations of all instances"""

        instance_list = []

        if not arg:
            # No argument passed, print all instances
            for key, value in storage.all().items():
                instance_list.append(str(value))
        else:
            # Argument passed, check if it's a valid class
            class_name = arg.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            # Print instances of the specified class
            for key, value in storage.all().items():
                if key.startswith(class_name + "."):
                    instance_list.append(str(value))

        print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

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
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        attr_name = arg_list[2]
        if len(arg_list) < 4:
            print("** value missing **")
            return

        attr_value = arg_list[3]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        storage.save()

    def default(self, line):
        """Handle commands in classes"""
        args = line.split(".")
        if len(args) == 2:
            class_name, command = args[0], args[1]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            elif command.startswith("show(") and command.endswith(")"):
                instance_id = command[5:-1]
                self.do_show(f"{class_name} {instance_id}")
            elif command.startswith("destroy(") and command.endswith(")"):
                instance_id = command[8:-1]
                self.do_destroy(f"{class_name} {instance_id}")
            elif command.startswith("update(") and command.endswith(")"):
                params = command[7:-1].split(", ")
                if len(params) == 3:
                    self.do_update(
                        f"{class_name} {params[0]} {params[1]} {params[2]}")
                else:
                    print("*** Unknown syntax:", line)
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """Counts the number of instances of a specified class"""

        count = 0
        all_objects = storage.all()
        class_name = arg.split()[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        for key in all_objects:
            if key.startswith(class_name + "."):
                count += 1


if __name__ == '__main__':

    HBNBCommand().cmdloop()
