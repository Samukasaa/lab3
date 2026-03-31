# models.py
"""Модель данных для блюда меню."""


class MenuItem:
    """Класс модели данных для блюда меню."""

    def __init__(self, obj_type: str, name: str, price: float, cook_time: str):
        self.obj_type = obj_type
        self.name = name
        self.price = price
        self.cook_time = cook_time

    def __eq__(self, other):
        if not isinstance(other, MenuItem):
            return False
        return (
            self.obj_type == other.obj_type
            and self.name == other.name
            and self.price == other.price
            and self.cook_time == other.cook_time
        )

    def __repr__(self):
        return f"MenuItem({self.obj_type}, {self.name}, {self.price}, {self.cook_time})"

    def to_string(self) -> str:
        """Преобразование объекта в строку для сохранения в файл."""
        return f'{self.obj_type} "{self.name}" {self.price} {self.cook_time}'

    def to_tuple(self) -> tuple:
        """Преобразование объекта в кортеж для отображения в таблице."""
        return (self.obj_type, self.name, str(self.price), self.cook_time)

    @classmethod
    def from_tuple(cls, data: tuple) -> "MenuItem":
        """Создание объекта из кортежа."""
        return cls(
            obj_type=data[0],
            name=data[1],
            price=float(data[2]),
            cook_time=data[3],
        )