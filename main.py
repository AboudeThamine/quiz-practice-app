import tkinter as tk
from tkinter import messagebox
from quiz_manager import QuizManager


class QuizAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Practice Application")
        self.root.geometry("550x420")
        self.root.configure(bg="#f4f6f9")

        self.manager = QuizManager()
        self.manager.load_initial_questions()

        self.container = tk.Frame(self.root, bg="#f4f6f9")
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_main_menu()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_screen()

        tk.Label(
            self.container,
            text="Quiz Practice Application",
            font=("Segoe UI", 18, "bold"),
            bg="#f4f6f9",
            fg="#1e293b",
        ).pack(pady=(10, 25))

        buttons = [
            ("Take a Topic Quiz", self.show_topic_selection),
            ("Take Revision Quiz", self.start_revision),
            ("Add a Question", self.show_add_question),
            ("Edit a Question", self.show_edit_question),
            ("Exit", self.root.quit),
        ]

        for text, command in buttons:
            tk.Button(
                self.container,
                text=text,
                command=command,
                font=("Segoe UI", 11),
                width=26,
                pady=8,
                bg="#2563eb",
                fg="white",
                relief="flat",
                cursor="hand2",
            ).pack(pady=6)

    def show_topic_selection(self):
        self.clear_screen()
        tk.Label(
            self.container,
            text="Select a Topic",
            font=("Segoe UI", 15, "bold"),
            bg="#f4f6f9",
        ).pack(pady=(10, 15))

        for topic in self.manager.get_topics():
            tk.Button(
                self.container,
                text=topic,
                command=lambda t=topic: messagebox.showinfo("Topic", f"Selected: {t}"),
                font=("Segoe UI", 11),
                width=22,
                pady=6,
                bg="#0f766e",
                fg="white",
                relief="flat",
            ).pack(pady=5)

        tk.Button(
            self.container, text="← Back to Menu", command=self.show_main_menu
        ).pack(pady=20)

    def start_revision(self):
        messagebox.showinfo("Revision Quiz", "Revision quiz screen coming next!")

    def show_add_question(self):
        self.clear_screen()
        tk.Label(
            self.container, text="Add a New Question", font=("Segoe UI", 14, "bold"), bg="#f4f6f9"
        ).pack(pady=10)
        tk.Button(self.container, text="← Back to Menu", command=self.show_main_menu).pack(pady=20)

    def show_edit_question(self):
        self.clear_screen()
        tk.Label(
            self.container, text="Edit a Question", font=("Segoe UI", 14, "bold"), bg="#f4f6f9"
        ).pack(pady=10)
        tk.Button(self.container, text="← Back to Menu", command=self.show_main_menu).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizAppGUI(root)
    root.mainloop()
