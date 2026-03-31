# parser.py
"""Парсер строк меню с обработкой исключений."""

import re
from models import MenuItem


class ParserError(Exception):
    """Исключение для ошибок парсинга."""

    pass


class MenuParser:
    """Класс для парсинга строк меню."""

    PATTERN = r'^([\wа-яА-ЯёЁ]+)\s+"([^"]+)"\s+([\d.]+)\s+(\d{2}:\d{2})$'

    @staticmethod
    def parse_line(line: str) -> MenuItem:
        """
        Парсинг одной строки.

        Args:
            line: Строка для парсинга

        Returns:
            MenuItem: Объект блюда

        Raises:
            ParserError: Если строка некорректна
        """
        if not line or not line.strip():
            raise ParserError("Пустая строка")

        line = line.strip()
        match = re.match(MenuParser.PATTERN, line)

        if not match:
            raise ParserError(f"Некорректный формат строки: {line}")

        try:
            price = float(match.group(3))
            if price < 0:
                raise ParserError(f"Отрицательная цена: {price}")
        except ValueError as e:
            raise ParserError(f"Некорректная цена: {match.group(3)}") from e

        return MenuItem(
            obj_type=match.group(1),
            name=match.group(2),
            price=price,
            cook_time=match.group(4),
        )

    @staticmethod
    def validate_time(cook_time: str) -> bool:
        """
        Проверка формата времени ЧЧ:ММ.

        Args:
            cook_time: Строка времени

        Returns:
            bool: True если формат корректен
        """
        try:
            hours, minutes = map(int, cook_time.split(":"))
            return 0 <= hours <= 23 and 0 <= minutes <= 59
        except (ValueError, AttributeError):
            return False