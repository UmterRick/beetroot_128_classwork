import unittest
from unittest.mock import patch
from lesson_20.example import get_page_html, get_order_from_db_by_id, get_contact_name


class ParsePageTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.python.org/"

    @patch("requests.get")
    def test_get_page(self, mock_object):
        mock_object.return_value.status_code = 200

        status_code = get_page_html(self.url)
        self.assertEqual(200, status_code)

    # @patch("requests.get")
    def test_get_page_2(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            status_code = get_page_html(self.url)

        self.assertEqual(200, status_code)

    def test_get_from_db(self):
        order_id = 111
        with patch("lesson_20.example.db_request") as mock_db:

            mock_db.return_value = (order_id, "Order 1", "My order", "2024-11-13")
            order = get_order_from_db_by_id(order_id)
        self.assertEqual(order, "Order 1")



class PhonebookTestCase(unittest.TestCase):

    def test_get_contact_name(self):
        expected_result = "John"
        with patch("builtins.input") as fake_input:
            with patch("builtins.print") as fake_print:
                fake_input.return_value = "John"
                actual_result = get_contact_name()
                fake_input.assert_called_once_with("Name:")

                fake_print.assert_called()
        self.assertEqual(expected_result, actual_result)

