import unittest
from obj_sales import CSVFile

class TestCSVFile(unittest.TestCase):
    
    def test_get_data(self):
        csv_file = CSVFile('shampoo_sales.txt')
        Expectation = [['01-01-2012', '266.0\n'], ['01-02-2012', '145.9\n']]
        self.assertEqual(csv_file.get_data(0,2),Expectation)
    
    def test_name(self):
        csv_file = CSVFile('shampoo_sales.txt')
        self.assertEqual(csv_file.name, 'shampoo_sales.txt')

    def test_expectation(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampo_sales')    





