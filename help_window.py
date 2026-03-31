# views/help_window.py
"""Окно справки (View)."""

import tkinter as tk
from tkinter import scrolledtext, messagebox


class HelpWindow(tk.Toplevel):
    """Окно справки."""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("📖 СПРАВКА")
        self.geometry("600x500")
        self.resizable(True, True)
        self._create_content()
        self.grab_set()

    def _create_content(self):
        """Создание содержимого окна."""
        header = tk.Label(
            self,
            text="📖 СПРАВКА ПО ПРОГРАММЕ",
            font=("Arial", 16, "bold"),
            bg="#2196F3",
            fg="white",
            pady=15,
        )
        header.pack(fill=tk.X)

        text_area = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Arial", 11), padx=15, pady=15
        )
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        help_text = """
📋 ОПИСАНИЕ ПРОГРАММЫ
Программа для управления меню ресторана.

🔘 ГЛАВНОЕ МЕНЮ
• РАБОТАТЬ - переход к таблице блюд
• СПРАВКА - эта информация
• ВЫХОД - закрыть программу

🔧 РАБОЧЕЕ ОКНО
• Добавить - новое блюдо
• Удалить - выбранное блюдо
• Сохранить - в файл data.txt

📝 ФОРМАТ ДАННЫХ
Тип "Название" Цена Время(ЧЧ:ММ)
Пример: Меню "Борщ" 150.50 00:30

💡 ОШИБКИ ЛОГИРУЮТСЯ В app.log
"""
        text_area.insert(tk.END, help_text)
        text_area.config(state=tk.DISABLED)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="Закрыть", command=self.destroy, width=15, bg="#FF9800", fg="white"
        ).pack()