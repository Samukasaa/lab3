# views/menu_window.py
"""Рабочее окно с таблицей блюд (View)."""

import tkinter as tk
from tkinter import ttk, messagebox


class MenuWindow:
    """Рабочее окно с таблицей."""

    def __init__(self, controller, parent):
        self.controller = controller
        self.window = tk.Toplevel(parent)
        self.window.title("📋 Управление меню")
        self.window.geometry("800x500")
        self._create_widgets()

    def _create_widgets(self):
        """Создание виджетов рабочего окна."""
        toolbar = tk.Frame(self.window, bg="#e0e0e0", pady=10)
        toolbar.pack(fill=tk.X)

        tk.Button(toolbar, text="➕ Добавить", command=self.controller.add_item).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(toolbar, text="🗑️ Удалить", command=self.controller.delete_item).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(toolbar, text="💾 Сохранить", command=self.controller.save_items).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(toolbar, text="🔙 Назад", command=self.controller.go_back).pack(
            side=tk.RIGHT, padx=5
        )

        columns = ("type", "name", "price", "time")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        self.tree.heading("type", text="Тип")
        self.tree.heading("name", text="Название")
        self.tree.heading("price", text="Цена (₽)")
        self.tree.heading("time", text="Время")

        self.tree.column("type", width=100)
        self.tree.column("name", width=300)
        self.tree.column("price", width=100)
        self.tree.column("time", width=100)

        scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.refresh_table()

    def refresh_table(self):
        """Обновление таблицы."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for menu_item in self.controller.get_items():
            self.tree.insert("", tk.END, values=menu_item.to_tuple())

    def get_selected_item(self):
        """Получение выбранного элемента."""
        selected = self.tree.selection()
        if not selected:
            return None
        item_values = self.tree.item(selected[0])["values"]
        return item_values

    def show_error(self, message: str):
        """Показ сообщения об ошибке."""
        messagebox.showerror("Ошибка", message)

    def show_info(self, message: str):
        """Показ информационного сообщения."""
        messagebox.showinfo("Информация", message)