#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Interpreter for HBNB Command program"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Method to exit the program"""
        return True

    def do_EOF(self, arg):
        """Method to exit the program"""
        print('')
        return True

    def emptyline(self):
        """When an empty line is entered, take no action"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


    


    
