import tkinter as tk
from tkinter import messagebox
from quiz_manager import QuizManager


class QuizApp:
    def __init__(self, window):
        # 1. Create the main window and connect to QuizManager
        self.window = window
        self.window.title("Quiz Practice Application")
        self.window.geometry("500x400")

        self.manager = QuizManager()
        self.manager.load_initial_questions()

        # 2. Create one main Frame (box) that holds whichever screen is currently visible
        self.screen = tk.Frame(self.window)
        self.screen.pack(pady=20)

        # 3. Start on the Home Screen
        self.show_home_screen()

    def clear_screen(self):
        # Delete everything inside the screen Frame before drawing a new screen
        for item in self.screen.winfo_children():
            item.destroy()

    # ---------------- HOME SCREEN ----------------
    def show_home_screen(self):
        self.clear_screen()

        tk.Label(self.screen, text="Quiz Practice Application", font=("Arial", 16, "bold")).pack(pady=15)

        # Learner section
        tk.Label(self.screen, text="Learner Menu", font=("Arial", 11, "bold")).pack(pady=(10, 5))
        tk.Button(self.screen, text="Take a Topic Quiz", width=25, command=self.show_topic_screen).pack(pady=4)
        tk.Button(self.screen, text="Take Revision Quiz", width=25, command=self.start_revision).pack(pady=4)

        # Instructor / Admin section (for Requirement 1: Add & Edit questions)
        tk.Label(self.screen, text="Instructor Menu", font=("Arial", 11, "bold")).pack(pady=(15, 5))
        tk.Button(self.screen, text="Manage Question Bank", width=25, command=self.show_admin_screen).pack(pady=4)

    # ---------------- LEARNER: TOPIC SELECTION ----------------
    def show_topic_screen(self):
        self.clear_screen()

        tk.Label(self.screen, text="Choose a Topic", font=("Arial", 14, "bold")).pack(pady=15)

        topics = self.manager.get_topics()
        for topic in topics:
            # Create a button for each topic
            btn = tk.Button(self.screen, text=topic, width=20)
            btn.config(command=lambda chosen=topic: self.open_topic_quiz(chosen))
            btn.pack(pady=4)

        tk.Button(self.screen, text="Back to Home", width=20, command=self.show_home_screen).pack(pady=20)

    def open_topic_quiz(self, topic):
        messagebox.showinfo("Quiz Starting", f"Loading questions for: {topic}")

    def start_revision(self):
        messagebox.showinfo("Revision Quiz", "Checking your latest missed questions...")

    # ---------------- INSTRUCTOR: ADD / EDIT MENU ----------------
    def show_admin_screen(self):
        self.clear_screen()

        tk.Label(self.screen, text="Manage Question Bank", font=("Arial", 14, "bold")).pack(pady=15)
        tk.Button(self.screen, text="Add a New Question", width=25, command=self.show_add_screen).pack(pady=5)
        tk.Button(self.screen, text="Edit an Existing Question", width=25, command=self.show_edit_screen).pack(pady=5)
        tk.Button(self.screen, text="Back to Home", width=25, command=self.show_home_screen).pack(pady=20)

    def show_add_screen(self):
        self.clear_screen()
        tk.Label(self.screen, text="Add Question (Form Next)", font=("Arial", 13, "bold")).pack(pady=15)
        tk.Button(self.screen, text="Back", width=15, command=self.show_admin_screen).pack(pady=10)

    def show_edit_screen(self):
        self.clear_screen()
        tk.Label(self.screen, text="Edit Question (Form Next)", font=("Arial", 13, "bold")).pack(pady=15)
        tk.Button(self.screen, text="Back", width=15, command=self.show_admin_screen).pack(pady=10)


# Start the program
window = tk.Tk()
app = QuizApp(window)
window.mainloop()
