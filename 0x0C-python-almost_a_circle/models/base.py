#!/usr/bin/python3
"""The first class Base module."""
import json
import turtle
import csv


class Base:
    """The first class Base.
    This is the "base" of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class Base.
        Args:
            id (int): the id of a new instance of class Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation
        of list_dictionaries.
        Arg:
            list_dictionaries (list): list of dictionaries."""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation
        of list_objs to a file.
        Arg:
            list_objs (list): a list of instancing inheriting from base.
        """
        fname = cls.__name__ + ".json"
        with open(fname, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
        representation json_string.
        Arg:
            json_string (str): a string representing a list of dictionaries.
        """
        if json_string == "[]" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attributes already
        set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(2, 2)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances."""
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, 'r') as jfile:
                dicts = Base.from_json_string(jfile.read())
                return [cls.create(**dic) for dic in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that writes the CSV serialization to a file.
        Arg:
            list_objs (list): list of objects.
        """
        fname = cls.__name__ + ".csv"
        with open(fname, 'w', newline="") as csvfile:
            if list_objs == [] or list_objs is None:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                escribe = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    escribe.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Class method that returns a list of class instances from
        a CSV file.
        """
        fname = cls.__name__ + ".csv"
        try:
            with open(fname, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                dicts = [dict([key, int(val)] for key, val in d.items())
                         for d in dicts]
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method that opens a window and draws all the Rectangles
        and Squares.
        Args:
            list_rectangles (list): list of Rectangle objects to draw
            list_squares (list): list of Square objects to draw
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#001F3F")
        turt.pensize(3)
        turt.shape("turtle")

        colors = ["#FF4136", "#FF851B", "#FFDC00", "#2ECC40", "#0074D9",
                  "#B10DC9"]
        i = 0

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            turt.color(colors[i % len(colors)])
            for j in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()
            i += 1

        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            turt.color(colors[i % len(colors)])
            for j in range(4):
                turt.forward(sq.width)
                turt.left(90)
            turt.hideturtle()
            i += 1

        turtle.exitonclick()
