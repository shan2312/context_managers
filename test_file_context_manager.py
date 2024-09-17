import unittest
from io import StringIO
import csv
from collections import namedtuple
from file_context_manager import CsvFileReaderContext, csv_file_reader, detect_delimiter  # Replace 'your_module' with actual module name

class TestCsvFileReader(unittest.TestCase):

    def setUp(self):
        # Sample CSV data
        self.csv_data_comma = "name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago\n"
        self.csv_data_semicolon = "name;age;city\nAlice;30;New York\nBob;25;Los Angeles\nCharlie;35;Chicago\n"
        self.csv_data_tab = "name\tage\tcity\nAlice\t30\tNew York\nBob\t25\tLos Angeles\nCharlie\t35\tChicago\n"

    def test_csv_file_reader_context_comma(self):
        f =  open('test.csv', "w")
        f.write(self.csv_data_comma)
        f.close()
        with CsvFileReaderContext('test.csv') as reader:
            row = next(reader)
            self.assertEqual(row.name, 'Alice')
            self.assertEqual(row.age, '30')
            self.assertEqual(row.city, 'New York')

    def test_csv_file_reader_context_semicolon(self):
        f =  open('test.csv', "w")
        f.write(self.csv_data_semicolon)
        f.close()
        with CsvFileReaderContext('test.csv') as reader:
            row = next(reader)
            self.assertEqual(row.name, 'Alice')
            self.assertEqual(row.age, '30')
            self.assertEqual(row.city, 'New York')

    def test_csv_file_reader_context_tab(self):
        f =  open('test.csv', "w")
        f.write(self.csv_data_semicolon)
        f.close()
        with CsvFileReaderContext('test.csv') as reader:
            row = next(reader)
            self.assertEqual(row.name, 'Alice')
            self.assertEqual(row.age, '30')
            self.assertEqual(row.city, 'New York')

    def test_csv_file_reader_function_comma(self):
        f =  open('test.csv', "w")
        f.write(self.csv_data_comma)
        f.close()
        with csv_file_reader('test.csv') as row_generator:
            row = next(row_generator)
            self.assertEqual(row.name, 'Alice')
            self.assertEqual(row.age, '30')
            self.assertEqual(row.city, 'New York')

    def test_csv_file_reader_function_semicolon(self):
        f =  open('test.csv', "w")
        f.write(self.csv_data_semicolon)
        f.close()
        with csv_file_reader('test.csv') as row_generator:
            row = next(row_generator)
            self.assertEqual(row.name, 'Alice')
            self.assertEqual(row.age, '30')
            self.assertEqual(row.city, 'New York')

    def test_csv_file_reader_function_tab(self):
        f =  open('test.csv', "w")
        f.write(self.csv_data_semicolon)
        f.close()
        
        with csv_file_reader('test.csv') as row_generator:
            row = next(row_generator)
            self.assertEqual(row.name, 'Alice')
            self.assertEqual(row.age, '30')
            self.assertEqual(row.city, 'New York')

    def test_detect_delimiter(self):
        self.assertEqual(detect_delimiter(self.csv_data_comma), ',')
        self.assertEqual(detect_delimiter(self.csv_data_semicolon), ';')
        self.assertEqual(detect_delimiter(self.csv_data_tab), '\t')


    def test_file_without_header(self):
        f =  open('test.csv', "w")
        f.write("Alice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago\n")
        f.close()
        
        with self.assertRaises(ValueError):
            with CsvFileReaderContext('test.csv') as reader:
                next(reader)

if __name__ == '__main__':
    unittest.main()
