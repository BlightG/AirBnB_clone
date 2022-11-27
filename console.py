#!/usr/bin/python3
""" a console for the command loop """
import cmd
import sys
import re
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ the home of the commandloop """

    prompt = '(hbnb) '
    # file = None
    classdict = {"BaseModel": BaseModel,
                 "User": User,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review,
                 "State": State}
    classkeys = classdict.keys()

    def do_create(self, args):
        """Creates a new instance of BaseModel,
saves it (to the JSON file) and prints the id"""
        if args:
            if args in HBNBCommand.classkeys:
                newobj = HBNBCommand.classdict[args]()
                storage.save()
                print(newobj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, command):
        """Prints the string representation of an
instance based on the class name and id"""

        args = command.split()  # splits command line into list of arguments
        objdict = storage.all()
        if len(args) == 2:
            if args[0] not in HBNBCommand.classkeys:
                print("** class doesn't exist **")
            else:
                """
                    when user give <class> <class.id> and merge them
                    to a string with format <class>.<class.id> search
                    for a mathcing key in FileStorage.__objects and
                    print the corsponding object
                """
                objdict = storage.all()
                searchkey = f'{args[0]}.{args[1]}'
                if searchkey in objdict.keys():
                    print(objdict[searchkey])
                else:
                    print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, command):
        """Deletes an instance based on the class name and id
(save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
"""
        args = command.split()  # splits command line into list of arguments
        objdict = storage.all()

        if len(args) == 2:
            if args[0] not in HBNBCommand.classkeys:
                print("** class doesn't exist **")
            else:
                """
                    when user passes <class> <class.id> merge it into
                    a string with the format <class>.<class.id>
                    and then search for it in FileStorage.__object dict if
                    found delete it and save the new FileStorage.__object dict
                """
                objdict = storage.all()
                searchkey = f'{args[0]}.{args[1]}'
                if searchkey in objdict.keys():
                    del objdict[searchkey]
                    storage.save()
                else:
                    print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, command):
        """Prints all string representation of all instances
based or not on the class name. Ex: $ all BaseModel or $ all
"""
        args = command.split()  # splits command line into list of arguments
        object_dict = storage.all()

        if len(args) == 1:
            if args[0] in HBNBCommand.classkeys:
                for obj in object_dict.keys():
                    """if statment checks the input command is same as
name of class for objects in the object_dict
Filestorage.__objects) dict
"""
                    if args[0] == object_dict[obj].__class__.__name__:
                        print(object_dict[obj])
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            for obj in object_dict.keys():
                print(object_dict[obj])

    def do_count(self, command):
        """a module that returns the number of instances
belonging to a specific instance
"""
        args = command.split()  # splits command line into list of arguments
        object_dict = storage.all()
        count = 0

        if len(args) == 1:
            if args[0] in HBNBCommand.classkeys:
                for obj in object_dict.keys():
                    """if statment checks the input command is same as
name of class for objects in the object_dict
Filestorage.__objects) dict
"""
                    if args[0] == object_dict[obj].__class__.__name__:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")

    def do_update(self, commands):
        """Updates an instance based on the class name and id by
adding or updating attribute (save the change into the JSON file).
Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'
"""
        args = commands.split()
        if len(args) == 4:
            storedict = storage.all()  # stores all object in Storedict
            storekeys = storedict.keys()  # stores key  for sotrekeys
            key = f'{args[0]}.{args[1]}'
            # @key will hold a str to search storekeys
            if args[0] in HBNBCommand.classdict.keys():
                if key in storekeys:
                    # if the key is in storekeys updates corsponding instance
                    value = re.findall(r'(?<=")(\S+|\s+)(?=")', args[3])
                # using regex to remove " from beginig and end of attribute
                # if user doesnt use " arund attribute value it uses the args
                # itself
                    if value:
                        setattr(storedict[key], args[2], value[0])
                    else:
                        setattr(storedict[key], args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 0:
            print("** class name missing **")

    def emptyline(self):
        """ If this method is overriddes, the built in emptyline
            function which repeats the last nonempty command entered.
        """
        return

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def precmd(self, line):
        """pasrses line input from command line
            to take care of <classname>.<cmd>(variable)
            cases
        """
        args = line.split()
        new_line = self.Regex(args)
        if new_line:
            return new_line
        else:
            return line

    def Regex(self, line):
        """
                parses <class name>.all() type commadas to
                appropriate version
                line: list
        """
        pattern = r'(?<=\S)\.(?=\S)'
        result = re.split(pattern, line[0])
        if result != [line[0]]:
            new_list = re.split(r'\(\)', result[1])
            if new_list != [result[1]]:
                return f'{new_list[0]} {result[0]}'
            else:
                id = re.findall(r'(?<=\(")[a-zA-Z0-9\-]{36}(?="\))', result[1])
                cmd = re.findall(r'^\w+', result[1])
                if id:
                    return f'{cmd[0]} {result[0]} {id[0]}'


if __name__ == '__main__':
    HBNBCommand().cmdloop()
