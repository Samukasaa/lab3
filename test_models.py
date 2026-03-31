# tests/test_models.py
"""Модульные тесты для модели данных."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "")))

from models import MenuItem


class TestMenuItem(unittest.TestCase):
    """Тесты для класса MenuItem."""

    def test_create_item(self):
        """Тест создания объекта."""
        item = MenuItem("Меню", "Борщ", 150.50, "00:30")
        self.assertEqual(item.obj_type, "Меню")
        self.assertEqual(item.name, "Борщ")
        self.assertEqual(item.price, 150.50)
        self.assertEqual(item.cook_time, "00:30")

    def test_to_string(self):
        """Тест преобразования в строку."""
        item = MenuItem("Меню", "Борщ", 150.50, "00:30")
        expected = 'Меню "Борщ" 150.5 00:30'
        self.assertEqual(item.to_string(), expected)

    def test_to_tuple(self):
        """Тест преобразования в кортеж."""
        item = MenuItem("Меню", "Борщ", 150.50, "00:30")
        expected = ("Меню", "Борщ", "150.5", "00:30")
        self.assertEqual(item.to_tuple(), expected)

    def test_from_tuple(self):
        """Тест создания из кортежа."""
        data = ("Меню", "Борщ", "150.50", "00:30")
        item = MenuItem.from_tuple(data)
        self.assertIsInstance(item, MenuItem)
        self.assertEqual(item.name, "Борщ")

    def test_equality(self):
        """Тест проверки равенства."""
        item1 = MenuItem("Меню", "Борщ", 150.50, "00:30")
        item2 = MenuItem("Меню", "Борщ", 150.50, "00:30")
        item3 = MenuItem("Меню", "Суп", 150.50, "00:30")
        self.assertEqual(item1, item2)
        self.assertNotEqual(item1, item3)

    def test_repr(self):
        """Тест строкового представления."""
        item = MenuItem("Меню", "Борщ", 150.50, "00:30")
        repr_str = repr(item)
        self.assertIn("MenuItem", repr_str)
        self.assertIn("Борщ", repr_str)


if __name__ == "__main__":
    unittest.main()