#!/usr/bin/python3
""" module for the Aibnb clone console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Interpreter for HBNB Command program"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Method to exit the program"""
        return self.do_quit(arg)

    def emptyline(self):
        """When an empty line is entered, take no action"""
        pass

    def do_help(self, arg):
        """Get help on commands"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it and prints the id
        """
        if len(arg) == 0 or not isinstance(arg, str):
            print('** class name missing **')
        elif arg not in [ 'BaseModel','User', 'State', 'City',
                'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg + '()')
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance based on class name and id.
        """
        if len(args) == 0:
            print('** class name missing **')
            return

            cls = get_cls(args[0])

        if cls is None:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
            ins = cls()
            ins.id = agrs[1]

        try:
            instance = cls.get(ins.id)
        except Exception as e:
            return

        print(instance)

    def do_destroy(self, arg):
        """
        Destroy an instance based on class name and id.
        """
        args = arg.split()
        if not args or args[0] == "":
            self.handle_error("** class name missing **")
        else:
            try:
                class_name, instance_id = args[0], args[1]
                key = "{}.{}".format(class_name, instance_id)
                instances = storage.all()
                if key not in instances:
                    self.handle_error("** no instance found **")
                else:
                    del instances[key]
                    storage.save()
            except IndexError:
                self.handle_error("** instance id missing **")

    def do_all(self, arg):
        """
        Print all string representations of instances based on class name.
        """
        args = arg.split()
        objects = storage.all()

        if not args or args[0] == "":
            print([str(objects[obj]) for obj in objects])
        else:
            class_name = args[0]
            if class_name not in objects:
                self.handle_error("** class doesn't exist **")
            else:
                print([str(objects[obj]) for obj in objects if class_name in obj])

    def do_update(self, arg):
        """
        Update an instance based on class name and id by adding or updating attribute.
        """
        args = arg.split()
        if not args or args[0] == "":
            self.handle_error("** class name missing **")
        else:
            try:
                class_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3].strip('\"')
                key = "{}.{}".format(class_name, instance_id)
                instances = storage.all()
                if key not in instances:
                    self.handle_error("** no instance found **")
                elif len(args) < 4:
                    self.handle_error("** attribute name missing **")
                elif len(args) < 5:
                    self.handle_error("** value missing **")
                else:
                    instance = instances[key]
                    setattr(instance, attr_name, attr_value)
                    instance.save()
            except IndexError:
                self.handle_error("** instance id missing **")
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()


    


    
