#!/usr/bin/python3
"""import the command interpreter module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    define a command interpreter for the program
    the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""

        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass
    
    def do_create(self, arg):
        """"Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:

            instance_id = args[1]
            key = cls_name + "." + instance_id
            instances = models.storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            instances = models.storage.all()
            if key in instances:
                del instances[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        instances = models.storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            try:
                cls_name = args[0]
                if cls_name in models.classes:
                    print([str(instance) for instance in instances.values()
                        if type(instance).__name__ == cls_name])
                else:
                    print("** class doesn't exist **")
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if cls_name not in models.classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = cls_name + "." + instance_id
            instances = models.storage.all()
            if key not in instances:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
            attr_value = args[3]
            instance = instances[key]
            attr_type = type(getattr(instance, attr_name, None))
            setattr(instance, attr_name, attr_type(attr_value))
            instance.save()
        except KeyError:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
