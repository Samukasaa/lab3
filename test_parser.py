# tests/test_parser.py
"""Модульные тесты для парсера."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "tests")))

from parser import MenuParser, ParserError


class TestMenuParser(unittest.TestCase):
    """Тесты для класса MenuParser."""

    def test_parse_valid_line(self):
        """Тест парсинга корректной строки."""
        line = 'Меню "Борщ" 150.50 00:30'
        item = MenuParser.parse_line(line)
        self.assertEqual(item.name, "Борщ")
        self.assertEqual(item.price, 150.50)

    def test_parse_empty_string(self):
        """Тест парсинга пустой строки."""
        with self.assertRaises(ParserError):
            MenuParser.parse_line("")

    def test_parse_invalid_format(self):
        """Тест парсинга неверного формата."""
        with self.assertRaises(ParserError):
            MenuParser.parse_line("Неверный формат")

    def test_parse_missing_quotes(self):
        """Тест парсинга без кавычек."""
        with self.assertRaises(ParserError):
            MenuParser.parse_line("Меню Борщ 150.50 00:30")

    def test_parse_invalid_time(self):
        """Тест парсинга неверного времени."""
        with self.assertRaises(ParserError):
            MenuParser.parse_line('Меню "Борщ" 150.50 25:00')

    def test_validate_time_valid(self):
        """Тест валидации корректного времени."""
        self.assertTrue(MenuParser.validate_time("12:30"))
        self.assertTrue(MenuParser.validate_time("00:00"))
        self.assertTrue(MenuParser.validate_time("23:59"))

    def test_validate_time_invalid(self):
        """Тест валидации некорректного времени."""
        self.assertFalse(MenuParser.validate_time("25:00"))
        self.assertFalse(MenuParser.validate_time("12:60"))
        self.assertFalse(MenuParser.validate_time("invalid"))


if __name__ == "__main__":
    unittest.main()