# tests/test_storage.py
"""Модульные тесты для хранилища."""

import unittest
import sys
import os
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "tests/tests")))

from storage import FileStorage
from models import MenuItem


class TestFileStorage(unittest.TestCase):
    """Тесты для класса FileStorage."""

    def setUp(self):
        """Подготовка тестовых данных."""
        self.test_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt")
        self.test_file.close()
        self.storage = FileStorage(self.test_file.name)

    def tearDown(self):
        """Очистка после теста."""
        if os.path.exists(self.test_file.name):
            os.remove(self.test_file.name)

    def test_save_and_load(self):
        """Тест сохранения и загрузки."""
        items = [
            MenuItem("Меню", "Борщ", 150.50, "00:30"),
            MenuItem("Меню", "Суп", 200.00, "00:45"),
        ]
        self.storage.save_all(items)
        loaded = self.storage.load_all()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].name, "Борщ")

    def test_load_nonexistent_file(self):
        """Тест загрузки несуществующего файла."""
        storage = FileStorage("nonexistent_file.txt")
        items = storage.load_all()
        self.assertEqual(len(items), 0)


if __name__ == "__main__":
    unittest.main()