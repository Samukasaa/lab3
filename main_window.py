# views/main_window.py
"""Главное окно приложения (View)."""

import tkinter as tk
from tkinter import messagebox


class MainWindow:
    """Главное окно приложения."""

    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title('🍽️ Ресторан "На берегу"')
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        """Создание виджетов главного окна."""
        header = tk.Label(
            self.root,
            text='🍽️ Ресторан "На берегу"',
            font=("Arial", 18, "bold"),
            bg="#2196F3",
            fg="white",
            pady=20,
        )
        header.pack(fill=tk.X)

        frame = tk.Frame(self.root, pady=30)
        frame.pack()

        btn_work = tk.Button(
            frame,
            text="🔧 РАБОТАТЬ",
            command=self.controller.show_menu_window,
            width=20,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            cursor="hand2",
        )
        btn_work.pack(pady=10)

        btn_help = tk.Button(
            frame,
            text="📖 СПРАВКА",
            command=self.controller.show_help_window,
            width=20,
            height=2,
            font=("Arial", 12),
            bg="#FF9800",
            fg="white",
            cursor="hand2",
        )
        btn_help.pack(pady=10)

        btn_exit = tk.Button(
            frame,
            text="🚪 ВЫХОД",
            command=self.controller.exit_app,
            width=20,
            height=2,
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            cursor="hand2",
        )
        btn_exit.pack(pady=10)

    def run(self):
        """Запуск главного цикла."""
        self.root.mainloop()

    def destroy(self):
        """Уничтожение окна."""
        self.root.destroy()