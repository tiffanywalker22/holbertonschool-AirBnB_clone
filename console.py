#!/usr/bin/python3
# console.py
# Tiffany Walker and Ethan Zalta
""" the console """

import cmd
from models.base_model import BaseModel
from models import storage

accepted_classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """prompt for cmd interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits program using ctrl+d (EOF)"""
        return True
    
    def emptyline(self):
        """empty line does nothing"""
        return False

    def do_create(self, args):
        """Creates a new instance of a given class"""
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args in accepted_classes.keys():
            newInst = accepted_classes[args]()
            newInst.save()
            print(newInst.id)
        else:
            print("** class doesn't exist **")

        def do_show(self, args):
            """Prints a string representation of an instance 
            using class and id"""
            args_list = args.split(" ")
            if len(args) == 0:
                print("** class name missing **")
            elif args_list[0] in accepted_classes.keys():
                if len(args_list) < 2:
                    print("** instance id missing **")
                else:
                    search_key = args_list[0] + "." + args_list[1]
                    all_objs = storage.all()
                    if search_key in all_objs:
                        print(str(all_objs[search_key]))
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

        def do_destroy(self, args):
            """Deletes an instance of an object, 
            takes class name and id as arguments"""
            args_list = args.split(" ")
            if len(args) == 0:
                print("** class name missing **")
            elif args_list[0] in accepted_classes.keys():
                if len(args_list) < 2:
                    print("** instance id missing **")
                else:
                    search_key = args_list[0] + "." + args_list[1]
                    all_objs = storage.all()
                    if search_key in all_objs:
                        del all_objs[search_key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

        def do_all(self, args):
            """Prints all objects of a given valid class or if no class given
            prints all objects."""
            if len(args) == 0:
                for key in storage.all():
                    print([str(storage.all()[key])])
            elif args not in accepted_classes.keys():
                print("** class doesn't exist")
            else:
                for key in storage.all().keys():
                    class_key = key.split(".")
                    if args == class_key[0]:
                        print([str(storage.all()[key])])

        def do_update(self, args):
            """Changes a specific attribute of a specific instance
            args needed: class, id, attribute, value"""
            args_list = args.split(" ")
            missing_args = {0: "** class name missing **",
            1: "** instance id missing **",
            2: "** attribute name missing **",
            3: "** class doesn't exist **"}

            if len(args) == missing_args.keys():
                print(missing_args[len(args)])
            elif args_list[0] not in accepted_classes.keys():
                print("** class doesn't exist **")
            else:
                search_key = args_list[0] + "." + args_list[1]
                all_objs = storage.all()
                if search_key in all_objs:
                    setattr(all_objs[search_key], args_list[2],
                            args_list[3].strip('"\''))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
