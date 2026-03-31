# main.py
"""Контроллер приложения (точка входа)."""

import tkinter as tk
from tkinter import messagebox
from storage import FileStorage
from views import MainWindow
from views import MenuWindow
from views import HelpWindow
import logging


class ApplicationController:
    """Контроллер приложения."""

    def __init__(self):
        self.storage = FileStorage("data.txt")
        self.items = []
        self.main_window = None
        self.menu_window = None
        self._setup_logger()
        self._load_data()

    def _setup_logger(self):
        """Настройка логгера."""
        self.logger = logging.getLogger("main")
        self.logger.setLevel(logging.INFO)

    def _load_data(self):
        """Загрузка данных."""
        try:
            self.items = self.storage.load_all()
            self.logger.info(f"Загружено {len(self.items)} элементов меню")
        except Exception as e:
            self.logger.error(f"Ошибка загрузки данных: {e}")
            self.items = []

    def run(self):
        """Запуск приложения."""
        self.main_window = MainWindow(self)
        self.main_window.run()

    def show_menu_window(self):
        """Показ рабочего окна."""
        self.menu_window = MenuWindow(self, self.main_window.root)

    def show_help_window(self):
        """Показ окна справки."""
        HelpWindow(self.main_window.root)

    def exit_app(self):
        """Выход из приложения."""
        if messagebox.askyesno("Выход", "Вы действительно хотите выйти?"):
            self.logger.info("Приложение закрыто пользователем")
            self.main_window.destroy()

    def get_items(self):
        """Получение списка элементов."""
        return self.items

    def add_item(self):
        """Добавление элемента."""
        dialog = tk.Toplevel(self.menu_window.window)
        dialog.title("Добавить блюдо")
        dialog.geometry("400x400")
        dialog.transient(self.menu_window.window)
        dialog.grab_set()

        fields = {}
        labels = ["Тип", "Название", "Цена", "Время (ЧЧ:ММ)"]

        for i, label in enumerate(labels):
            tk.Label(dialog, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(dialog, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            fields[label] = entry

        def on_submit():
            try:
                from parser import MenuParser, ParserError

                line = f'{fields["Тип"].get()} "{fields["Название"].get()}" {fields["Цена"].get()} {fields["Время (ЧЧ:ММ)"].get()}'
                item = MenuParser.parse_line(line)
                self.items.append(item)
                self.menu_window.refresh_table()
                dialog.destroy()
                self.logger.info(f"Добавлено блюдо: {item.name}")
            except ParserError as e:
                messagebox.showerror("Ошибка ввода", str(e))

        tk.Button(dialog, text="Добавить", command=on_submit).grid(row=5, column=1, pady=20)

    def delete_item(self):
        """Удаление элемента."""
        selected = self.menu_window.get_selected_item()
        if not selected:
            self.menu_window.show_error("Выберите блюдо для удаления")
            return

        if messagebox.askyesno("Удаление", "Удалить выбранное блюдо?"):
            self.items = [item for item in self.items if item.to_tuple() != tuple(selected)]
            self.menu_window.refresh_table()
            self.logger.info(f"Удалено блюдо: {selected[1]}")

    def save_items(self):
        """Сохранение элементов."""
        try:
            self.storage.save_all(self.items)
            self.menu_window.show_info("Данные успешно сохранены!")
        except Exception as e:
            self.menu_window.show_error(f"Ошибка сохранения: {e}")
            self.logger.error(f"Ошибка сохранения: {e}")

    def go_back(self):
        """Возврат в главное меню."""
        self.menu_window.window.destroy()
        self.menu_window = None


if __name__ == "__main__":
    app = ApplicationController()
    app.run()