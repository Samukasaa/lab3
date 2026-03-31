# storage.py
"""Хранилище данных с логированием ошибок."""

import os
import logging
from parser import MenuParser, ParserError
from models import MenuItem


class FileStorage:
    """Класс для управления файлами данных."""

    def __init__(self, filename: str = "data.txt", log_file: str = "app.log"):
        self.filename = filename
        self.log_file = log_file
        self._setup_logger()

    def _setup_logger(self):
        """Настройка логгера."""
        self.logger = logging.getLogger("storage")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(self.log_file, encoding="utf-8")
            file_handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def load_all(self) -> list:
        """
        Загрузка всех элементов с обработкой ошибок.

        Returns:
            list: Список объектов MenuItem
        """
        items = []
        errors = []

        if not os.path.exists(self.filename):
            self.logger.info(f"Файл {self.filename} не найден, создан новый список")
            return items

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        items.append(MenuParser.parse_line(line))
                    except ParserError as e:
                        error_msg = f"Строка {line_num}: {e}"
                        errors.append(error_msg)
                        self.logger.warning(f"Пропущена некорректная строка: {error_msg}")
        except IOError as e:
            self.logger.error(f"Ошибка чтения файла: {e}")
            raise

        if errors:
            self.logger.info(f"Всего пропущено строк с ошибками: {len(errors)}")

        return items

    def save_all(self, items: list) -> bool:
        """
        Сохранение всех элементов в файл.

        Args:
            items: Список объектов MenuItem

        Returns:
            bool: True если успешно
        """
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for item in items:
                    f.write(item.to_string() + "\n")
            self.logger.info(f"Успешно сохранено {len(items)} элементов")
            return True
        except IOError as e:
            self.logger.error(f"Ошибка записи в файл: {e}")
            raise