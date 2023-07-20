#!/usr/bin/python3

"""Module define first class Base"""
import json
import csv
from os.path import exists


class Base:
    """Module define first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):  # list of instances who inherits of Base
        """save JSON string representation of list_objs to a file
        Args:
            dictionary
        """
        filename = cls.__name__ + ".json"
        dictio = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(dictio)
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            file.write(json_str)

    def from_json_string(json_string):
        """from a  file loads()

        Args:
            dictionary
        """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create

        Args:
            dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # creates a dummy instance of the class of Re...
        if cls.__name__ == "Square":
            dummy = cls(1)  # creates a dummy instance of the class of Square
        if Cond is None:
            dummy = None

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:

        Args:
            cls
        """
        filename = cls.__name__ + ".json"
        if not exists(filename):
            return "[]"
        with open(filename, 'r') as file:
            json_string = file.read()
            dictionary = cls.from_json_string(json_string)
            instance_list = [cls.create(**obj) for obj in dictionary]
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save data to csv file

        Args:
            cls
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            if list_objs is None:
                return None
            writer = csv.writer(file)
            for ob in list_objs:

                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                elif cls.__name__ == "Square":
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        """load data to csv file

        Args:
            cls
        """

        filename = cls.__name__ + ".csv"
        list_objs = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    id, width, height, x, y = map(int, row)
                    obj = cls(width, height, x, y, id)
                elif cls.__name__ == "Square":
                    id, size, x, y = map(int, row)
                    obj = cls(size, x, y, id)
                list_objs.append(obj)
            return list_objs
