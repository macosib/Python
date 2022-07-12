import unittest
from unittest.mock import patch
from parameterized import parameterized

from main import _check_doc_in_documents, _shelf_doc_in_directories
from main import find_people, find_shelf, show_all_documents, add_people_doc, delete_doc, move_doc, add_shelf


class TestFunctionsMain(unittest.TestCase):

    @parameterized.expand([('2207 876234', True), ('11-2', True), ('10006', True), ('2', False), ('333', False)])
    def test_check_doc_in_documents(self, number, result):
        self.assertEqual(_check_doc_in_documents(number), result)

    @parameterized.expand([('1', True), ('2', True), ('3', True), ('6', False), ('7', False)])
    def test_shelf_doc_in_directories(self, number, result):
        self.assertEqual(_shelf_doc_in_directories(number), result)


    @patch('builtins.input', lambda *args: '2207 876234')
    def test_find_shelf(self):
        self.assertEqual(find_shelf(), '1')

    def test_show_all_documents(self):
        self.assertIsNotNone(show_all_documents())

    @patch('builtins.input', side_effect=['1123', 'driver licence', 'Zina Kuzina', '4'])
    def test_add_people_doc(self, mock_input):
        self.assertEqual(add_people_doc(), '4')

    @patch('builtins.input', lambda *args: '10006')
    def test_delete_doc(self):
        self.assertEqual(delete_doc(), '10006')

    @patch('builtins.input', side_effect=['2207 876234', '5'])
    def test_move_doc(self, mock_input):
        self.assertEqual(move_doc(), '5')

    @parameterized.expand([('2207 876234', 'Василий Гупкин'), ('11-2', 'Геннадий Покемонов'), ('1123', 'Zina Kuzina')])
    def test_find_people(self, number, result):
        self.assertEqual(find_people(number), result)

class ExpectedFailureTestFunctionsMain(unittest.TestCase):

    @unittest.expectedFailure
    @patch('builtins.input', lambda *args: '22222')
    def test_find_people_fail(self):
        self.assertEqual(find_people(), 'Василий Гупкин')
