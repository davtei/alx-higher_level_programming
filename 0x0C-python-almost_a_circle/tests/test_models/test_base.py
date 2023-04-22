#!/usr/bin/python3
"""Test script for running Unittest on module base."""
import unittest
from unittest.mock import patch, mock_open
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Provides unit tests to test for class Base instantiation."""

    def test_empty_args_two(self):
        """test id assignment for no arguments for two instantiations."""
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_empty_args_three(self):
        """test id assignment for no arguments for two instantiations."""
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, c.id - 2)

    def test_retrieve_id(self):
        """test for return of id assigned during instantiation."""
        a = Base(5)
        self.assertEqual(a.id, 5)

    def test_two_ids(self):
        """test for when two arguments are provided."""
        with self.assertRaises(TypeError):
            Base(1, 5)

    def test_id_is_range(self):
        """test for when id assignment is a range."""
        self.assertEqual(Base(range(1, 5)).id, range(1, 5))

    def test_id_is_bool_True(self):
        """test for when id is bool, True."""
        a = Base(True)
        self.assertEqual(a.id, True)

    def test_id_is_bool_False(self):
        """test for when id is bool, False."""
        b = Base(False)
        c = Base(0)
        self.assertEqual(b.id, c.id)

    def test_id_float(self):
        """test for id is float."""
        self.assertEqual(Base(1.2).id, 1.2)

    def test_id_str(self):
        """test for id is a string."""
        self.assertEqual(Base("alx").id, "alx")
        self.assertEqual(Base('a').id, 'a')

    def test_id_empty_list(self):
        """test for id is an empty list."""
        self.assertEqual(Base([]).id, [])

    def test_id_list(self):
        """test for id is a list."""
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_id_empty_dict(self):
        """test for id is an empty dictionary."""
        self.assertEqual(Base(dict()).id, dict())

    def test_id_dict(self):
        """test for id is a dictionary."""
        self.assertEqual(Base({'d': 1, 't': 2}).id, {'d': 1, 't': 2})

    def test_id_tuple(self):
        """test for id is a tuple."""
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))

    def test_id_set(self):
        """test for id is a set."""
        self.assertEqual(Base({1, 2, 'a'}).id, {1, 2, 'a'})

    def test_id_byte(self):
        """test for id is a byte."""
        self.assertEqual(Base(b'alx').id, b'alx')

    def test_id_is_public(self):
        """test for when id is public."""
        a = Base(5)
        self.assertEqual(a.id, 5)
        a.id = 10
        self.assertEqual(a.id, 10)

    def test_id_is_None(self):
        """test for when id is None."""
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_id_inf(self):
        """test for id is infinity."""
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_id_NaN(self):
        """test for id is NaN."""
        self.assertNotEqual(Base(float('nan')).id, float('nan'))


class TestBaseToJsonStr(unittest.TestCase):
    """Provides unit tests to test for to_json_string method."""

    def test_to_json_str_na(self):
        """test for no argument supplied."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_str_empty_list(self):
        """test for an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_str_none(self):
        """test argument is None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_str_type_R(self):
        """"test using type of argument with a Rectangle instance."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(type(Base.to_json_string([r.to_dictionary()])), str)

    def test_to_json_str_len_dict_R(self):
        """test using length of argument with a Rectangle instance."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 54)

    def test_to_json_str_len_2dict_R(self):
        """test using length of argument with two Rectangle instance."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 107)

    def test_to_json_str_type_Sq(self):
        """"test using type of argument with a Square instance."""
        sq = Square(10, 2, 0, 12)
        self.assertEqual(type(Base.to_json_string([sq.to_dictionary()])), str)

    def test_to_json_str_len_dict_Sq(self):
        """test using length of argument with a Square instance."""
        sq = Square(10, 2, 0, 12)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 40)

    def test_to_json_str_len_2dict_Sq(self):
        """test using length of argument with two Square instance."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        dicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 79)


class TestBaseSaveToFile(unittest.TestCase):
    """Provides unit tests to test for save_to_file method."""

    @classmethod
    def tearDown(self):
        """Delete pre-existing files before testing."""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_Base_no_arg(self):
        """test for absence of an argument."""
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_save_to_file_Base_None(self):
        """test whether an empty JSON array is written to the file
        with None as argument.
        """
        with patch('builtins.open', mock_open()) as file:
            Base.save_to_file(None)
            file.assert_called_once_with("Base.json", 'w')
            file().write.assert_called_once_with('[]')

    def test_save_to_file_Base_empty_list(self):
        """test with empty list as input.
        Verify whether am empty JSON array is written to the file."""
        Base.save_to_file([])
        with open("Base.json", 'r') as efile:
            self.assertEqual(efile.read(), '[]')

    def test_save_to_file_Base_extra_arg(self):
        """test with extra arguments."""
        with self.assertRaises(TypeError):
            Base.save_to_file([], [1])

    def test_save_to_file_Rectangle_no_arg(self):
        """test for absence of an argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_Rectangle_None(self):
        """test whether an empty JSON array is written to the file
        with None as argument.
        """
        with patch('builtins.open', mock_open()) as file:
            Rectangle.save_to_file(None)
            file.assert_called_once_with("Rectangle.json", 'w')
            file().write.assert_called_once_with('[]')

    def test_save_to_file_Rectangle_empty_list(self):
        """test with empty list as input.
        Verify whether am empty JSON array is written to the file."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as efile:
            self.assertEqual(efile.read(), '[]')

    def test_save_to_file_Rectangle_extra_arg(self):
        """test with extra arguments."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [2])

    def test_save_to_file_Rectangle_1Rectangle(self):
        """test with one instance of Rectangle."""
        r = Rectangle(10, 2, 0, 0, 12)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(len(file.read()), 54)

    def test_save_to_file_Rectangle_2Rectangles(self):
        """test with two instances of Rectangle."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(len(file.read()), 107)

    def test_save_to_file_Rectangle_existing_file(self):
        """test for saving to an existing file.
        Verify whether the JSON representation of the list of instances
        of the Rectangle class overwrites the existing data in the file.
        """
        r = Rectangle(10, 2, 0, 0, 12)
        Rectangle.save_to_file([r])
        r = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(len(file.read()), 53)

    def test_save_to_file_Square_no_arg(self):
        """test for absence of an argument."""
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_Square_None(self):
        """test whether an empty JSON array is written to the file
        with None as argument.
        """
        with patch('builtins.open', mock_open()) as file:
            Square.save_to_file(None)
            file.assert_called_once_with("Square.json", 'w')
            file().write.assert_called_once_with('[]')

    def test_save_to_file_Square_empty_list(self):
        """test with empty list as input.
        Verify whether am empty JSON array is written to the file."""
        Square.save_to_file([])
        with open("Square.json", 'r') as efile:
            self.assertEqual(efile.read(), '[]')

    def test_save_to_file_Square_extra_arg(self):
        """test with extra arguments."""
        with self.assertRaises(TypeError):
            Square.save_to_file([], [3])

    def test_save_to_file_Square_1Square(self):
        """test with one instance of Square."""
        sq = Square(10, 2, 0, 12)
        Square.save_to_file([sq])
        with open("Square.json", 'r') as file:
            self.assertEqual(len(file.read()), 40)

    def test_save_to_file_Square_2Squares(self):
        """test with two instances of Square."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", 'r') as file:
            self.assertEqual(len(file.read()), 79)

    def test_save_to_file_existing_file(self):
        """test for saving to an existing file.
        Verify whether the JSON representation of the list of instances
        of the Square class overwrites the existing data in the file.
        """
        r = Square(10, 2, 0, 12)
        Square.save_to_file([r])
        r = Square(8, 7, 0, 12)
        Square.save_to_file([r])
        with open("Square.json", 'r') as file:
            self.assertEqual(len(file.read()), 39)


class TestBaseFromJsonString(unittest.TestCase):
    """Provides unit tests to test from_json_string method."""

    def test_from_json_string_Base_na(self):
        """test for no argument supplied."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_Base_None(self):
        """test for None argument supplied."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_Base_empty(self):
        """test with empty list as input."""
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_from_json_string_Base_extra_arg(self):
        """test with extra arguments."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], [1])

    def test_from_json_string_Rectangle_na(self):
        """test for no argument supplied."""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    def test_from_json_string_Rectangle_None(self):
        """test for None argument supplied."""
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_from_json_string_Rectangle_empty(self):
        """test with empty list as input."""
        self.assertEqual(Rectangle.from_json_string('[]'), [])

    def test_from_json_string_Rectangle_extra_arg(self):
        """test with extra arguments."""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string([], [1])

    def test_from_json_string_1Rectangle(self):
        """test with one instance of Rectangle."""
        r = Rectangle(10, 2, 0, 0, 12)
        list1 = r.to_dictionary()
        list_json = Rectangle.to_json_string(list1)
        list2 = Rectangle.from_json_string(list_json)
        self.assertEqual(list2, list1)

    def test_from_json_string_2Rectangles(self):
        """test with two instances of Rectangle."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        list1 = [r1.to_dictionary(), r2.to_dictionary()]
        list_json = Rectangle.to_json_string(list1)
        list2 = Rectangle.from_json_string(list_json)
        self.assertEqual(list2, list1)

    def test_from_json_string_Square_na(self):
        """test for no argument supplied."""
        with self.assertRaises(TypeError):
            Square.from_json_string()

    def test_from_json_string_Square_None(self):
        """test for None argument supplied."""
        self.assertEqual(Square.from_json_string(None), [])

    def test_from_json_string_Square_empty(self):
        """test with empty list as input."""
        self.assertEqual(Square.from_json_string('[]'), [])

    def test_from_json_string_Square_extra_arg(self):
        """test with extra arguments."""
        with self.assertRaises(TypeError):
            Square.from_json_string([], [1])

    def test_from_json_string_1Square(self):
        """test with one instance of Square."""
        sq = Square(10, 2, 0, 12)
        list1 = sq.to_dictionary()
        list_json = Square.to_json_string(list1)
        list2 = Square.from_json_string(list_json)
        self.assertEqual(list2, list1)

    def test_from_json_string_2Squares(self):
        """test with two instances of Square."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        list1 = [sq1.to_dictionary(), sq2.to_dictionary()]
        list_json = Square.to_json_string(list1)
        list2 = Square.from_json_string(list_json)
        self.assertEqual(list2, list1)


class TestBaseCreate(unittest.TestCase):
    """Provides unit tests to test the create method of class Base."""

    def test_create_Rectangle(self):
        """test whether instance with all attributes preset
        will be returned."""
        r1 = Rectangle(10, 2, 0, 12)
        rdict = r1.to_dictionary()
        r2 = Rectangle.create(**rdict)
        self.assertEqual(str(r1), str(r2))

    def test_create_Rectangle(self):
        """test whether instance with all attributes preset
        will be returned."""
        sq1 = Square(10, 2, 0, 12)
        sqdict = sq1.to_dictionary()
        sq2 = Square.create(**sqdict)
        self.assertEqual(str(sq1), str(sq2))


class TestBaseLoadFromFile(unittest.TestCase):
    """Provides unit tests to test the load_from_file_method of class Base."""

    @classmethod
    def tearDown(self):
        """Delete pre-existing files before testing."""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_Base_file_absent(self):
        """test with absent file."""
        b = Base.load_from_file()
        self.assertEqual(b, [])

    def test_load_from_file_Base_extra_arg(self):
        """test for extra argument supplied."""
        with self.assertRaises(TypeError):
            Base.load_from_file([], [1])

    def test_load_from_file_Rectangle_file_absent(self):
        """test with absent file."""
        r = Rectangle.load_from_file()
        self.assertEqual(r, [])

    def test_load_from_file_Rectangle_extra_arg(self):
        """test for extra argument supplied."""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], [1])

    def test_load_from_file_Rectangle_r1(self):
        """test for retrieving the first of two Rectangles."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file([r1, r2])
        list_r = Rectangle.load_from_file()
        self.assertEqual(str(list_r[0]), str(r1))

    def test_load_from_file_Rectangle_r2(self):
        """test for retrieving the second of two Rectangles."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file([r1, r2])
        list_r = Rectangle.load_from_file()
        self.assertEqual(str(list_r[1]), str(r2))

    def test_load_from_file_Rectangle_object_type(self):
        """test for type of saved content."""
        r1 = Rectangle(10, 2, 0, 1, 12)
        r2 = Rectangle(8, 7, 0, 1, 12)
        Rectangle.save_to_file([r1, r2])
        list_r = Rectangle.load_from_file()
        self.assertTrue(all(type(o) == Rectangle for o in list_r))

    def test_load_from_file_Square_file_absent(self):
        """test with absent file."""
        sq = Square.load_from_file()
        self.assertEqual(sq, [])

    def test_load_from_file_Square_extra_arg(self):
        """test for extra argument supplied."""
        with self.assertRaises(TypeError):
            Square.load_from_file([], [1])

    def test_load_from_file_Square_sq1(self):
        """test for retrieving the first of two Squares."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(list_sq[0]), str(sq1))

    def test_load_from_file_Square_sq1(self):
        """test for retrieving the second of two Squares."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(list_sq[1]), str(sq2))

    def test_load_from_file_Square_object_type(self):
        """test for retrieving the second of two Squares."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertTrue(all(type(o) == Square for o in list_sq))


class TestBaseSaveToFileCSV(unittest.TestCase):
    """Provides unit tests to test the save_to_file_csv of class Base."""

    @classmethod
    def tearDown(self):
        """Delete pre-existing files before testing."""
        try:
            os.remove("Base.csv")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_save_to_file_csv_Base_no_args(self):
        """test for absent argument."""
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()

    def test_save_to_file_csv_Base_extra_args(self):
        """test for extra argument."""
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([], [1])

    def test_save_to_file_csv_Base_empty(self):
        """test for empty list."""
        Base.save_to_file_csv([])
        with open("Base.csv", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_csv_Base_None(self):
        """test for None argument."""
        Base.save_to_file_csv(None)
        with open("Base.csv", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_csv_Rectangle_no_args(self):
        """test for absent argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_Rectangle_extra_args(self):
        """test for extra argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], [1])

    def test_save_to_file_csv_Rectangle_empty(self):
        """test for empty list."""
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_csv_Rectangle_None(self):
        """test for None argument."""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_csv_1Rectangle(self):
        """test for one Rectangle instance."""
        r = Rectangle(10, 2, 0, 1, 12)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", 'r') as file:
            self.assertTrue(file.read(), "12,10,2,0,1")

    def test_save_to_file_csv_2Rectangle(self):
        """test for two Rectangle instances."""
        r1 = Rectangle(10, 2, 0, 1, 12)
        r2 = Rectangle(8, 7, 0, 1, 12)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", 'r') as file:
            self.assertTrue(file.read(), "12,10,2,0,1\n12,8,7,0,1")

    def test_save_to_file_csv_Square_no_args(self):
        """test for absent argument."""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

    def test_save_to_file_csv_Square_extra_args(self):
        """test for extra argument."""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], [1])

    def test_save_to_file_csv_Square_empty(self):
        """test for empty list."""
        Square.save_to_file_csv([])
        with open("Square.csv", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_csv_Square_None(self):
        """test for None argument."""
        Square.save_to_file_csv(None)
        with open("Square.csv", 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_csv_1Square(self):
        """test for one Square instance."""
        sq = Square(10, 2, 0, 12)
        Square.save_to_file_csv([sq])
        with open("Square.csv", 'r') as file:
            self.assertTrue(file.read(), "12,10,2,0")

    def test_save_to_file_csv_2Square(self):
        """test for two Square instances."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", 'r') as file:
            self.assertTrue(file.read(), "12,10,2,0\n12,8,7,0")


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Provides unit tests to test load_from_file_csv method of class Base."""

    @classmethod
    def tearDown(self):
        """Delete pre-existing files before testing."""
        try:
            os.remove("Base.csv")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_Base_no_arg(self):
        """test for absence of file."""
        empty = Base.load_from_file_csv()
        self.assertEqual(empty, [])

    def test_load_from_file_csv_Base_extra_arg(self):
        """test for extra arguments."""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], [1])

    def test_load_from_file_csv_Rectangle_no_arg(self):
        """test for absence of file."""
        empty = Rectangle.load_from_file_csv()
        self.assertEqual(empty, [])

    def test_load_from_file_csv_Rectangle_extra_arg(self):
        """test for extra arguments."""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv([], [1])

    def test_load_from_file_csv_Rectangle_r1(self):
        """test for retrieving the first of two Rectangles."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file_csv([r1, r2])
        list_r = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_r[1]), str(r2))

    def test_load_from_file_csv_Rectangle_r2(self):
        """test for retrieving the second of two Rectangles."""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file_csv([r1, r2])
        list_r = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_r[1]), str(r2))

    def test_load_from_file_csv_Rectangle_object_type(self):
        """test for type of saved content."""
        r1 = Rectangle(10, 2, 0, 1, 12)
        r2 = Rectangle(8, 7, 0, 1, 12)
        Rectangle.save_to_file_csv([r1, r2])
        list_r = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(o) == Rectangle for o in list_r))

    def test_load_from_file_csv_Square_no_arg(self):
        """test for absence of file."""
        empty = Square.load_from_file_csv()
        self.assertEqual(empty, [])

    def test_load_from_file_csv_Square_extra_arg(self):
        """test for extra arguments."""
        with self.assertRaises(TypeError):
            Square.load_from_file_csv([], [1])

    def test_load_from_file_csv_Square_sq1(self):
        """test for retrieving the first of two Squares."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file_csv([sq1, sq2])
        list_sq = Square.load_from_file_csv()
        self.assertEqual(str(list_sq[0]), str(sq1))

    def test_load_from_file_csv_Square_sq2(self):
        """test for retrieving the second of two Squares."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file_csv([sq1, sq2])
        list_sq = Square.load_from_file_csv()
        self.assertEqual(str(list_sq[1]), str(sq2))

    def test_load_from_file_csv_Square_object_type(self):
        """test for retrieving the second of two Squares."""
        sq1 = Square(10, 2, 0, 12)
        sq2 = Square(8, 7, 0, 12)
        Square.save_to_file_csv([sq1, sq2])
        list_sq = Square.load_from_file_csv()
        self.assertTrue(all(type(o) == Square for o in list_sq))


if __name__ == "__main__":
    unittest.main()
