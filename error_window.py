# views/error_window.py
"""Окно для отображения ошибок парсинга."""

import tkinter as tk
from tkinter import scrolledtext


class ErrorWindow(tk.Toplevel):
    """Окно для просмотра ошибок при загрузке данных."""

    def __init__(self, parent, errors: list):
        super().__init__(parent)
        self.parent = parent
        self.errors = errors
        self.title("⚠️ ОШИБКИ ЗАГРУЗКИ")
        self.geometry("650x500")
        self.resizable(True, True)

        self._create_widgets()
        self.grab_set()

    def _create_widgets(self):
        """Создание виджетов окна."""
        header_frame = tk.Frame(self, bg="#f44336")
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="⚠️ ОШИБКИ ПРИ ЗАГРУЗКЕ ДАННЫХ",
            font=("Arial", 16, "bold"),
            bg="#f44336",
            fg="white",
            pady=15
        )
        title_label.pack()

        info_label = tk.Label(
            self,
            text=f"Всего обнаружено ошибок: {len(self.errors)}",
            font=("Arial", 12, "bold"),
            fg="#f44336",
            pady=10
        )
        info_label.pack()

        text_frame = tk.Frame(self)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.text_area = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg="#fff3f3",
            fg="#d32f2f",
            padx=10,
            pady=10,
            spacing1=3,
            spacing3=3
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

        if self.errors:
            error_block = "━" * 60 + "\n"
            error_block += "📋 СПИСОК ВСЕХ ОШИБОК:\n"
            error_block += "━" * 60 + "\n\n"

            for i, error in enumerate(self.errors, 1):
                error_block += f"{i}. {error}\n"
                error_block += "─" * 60 + "\n"

            error_block += f"\n⚠️ ИТОГО: {len(self.errors)} ошибок(и)\n"
            error_block += "━" * 60 + "\n"

            self.text_area.insert(tk.END, error_block)
        else:
            self.text_area.insert(tk.END, "✅ Ошибок не обнаружено!")

        self.text_area.config(state=tk.DISABLED)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)

        btn_close = tk.Button(
            btn_frame,
            text="🔙 ЗАКРЫТЬ И ПРОДОЛЖИТЬ РАБОТУ",
            command=self.destroy,
            width=35,
            height=2,
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_close.pack(pady=5)