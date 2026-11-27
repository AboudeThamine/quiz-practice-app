import random
from question import Question


class QuizManager:
    def __init__(self):
        self.questions = []
        self.latest_result = None
        self.missed_question_ids = []

    def load_initial_questions(self):
        self.questions = [
            Question("1", "Python Basics", "Which function displays output on the screen in Python?",
                     {"A": "echo()", "B": "print()", "C": "input()", "D": "show()"}, "B"),
            Question("2", "Python Basics", "What is the data type of 3.14 in Python?",
                     {"A": "int", "B": "str", "C": "float", "D": "bool"}, "C"),
            Question("3", "Python Basics", "Which string method removes leading and trailing spaces?",
                     {"A": "strip()", "B": "clean()", "C": "upper()", "D": "cut()"}, "A"),
            Question("4", "Python Control Flow", "Which keyword checks another condition after an if statement?",
                     {"A": "else if", "B": "elseif", "C": "elif", "D": "when"}, "C"),
            Question("5", "Python Control Flow", "Which loop repeats as long as a condition stays True?",
                     {"A": "for", "B": "while", "C": "repeat", "D": "loop"}, "B"),
            Question("6", "Python Control Flow", "What does True and False evaluate to?",
                     {"A": "True", "B": "False", "C": "None", "D": "1"}, "B"),
            Question("7", "Python Functions", "Which keyword is used to define a function in Python?",
                     {"A": "func", "B": "define", "C": "def", "D": "function"}, "C"),
            Question("8", "Python Functions", "What does a function return if it has no return statement?",
                     {"A": "0", "B": "False", "C": "Empty string", "D": "None"}, "D"),
            Question("9", "Python Functions", "Which built-in function rounds a decimal number?",
                     {"A": "round()", "B": "approx()", "C": "floor()", "D": "short()"}, "A"),
            Question("10", "Python Data Structures", "Which brackets are used to create a list in Python?",
                     {"A": "( )", "B": "{ }", "C": "[ ]", "D": "< >"}, "C"),
            Question("11", "Python Data Structures", "Which data structure stores key-value pairs?",
                     {"A": "list", "B": "tuple", "C": "set", "D": "dict"}, "D"),
            Question("12", "Python Data Structures", "Which collection is ordered and cannot be modified after creation?",
                     {"A": "list", "B": "tuple", "C": "dict", "D": "set"}, "B"),
        ]

    def get_topics(self):
        topics = []
        for q in self.questions:
            if q.topic not in topics:
                topics.append(q.topic)
        return topics

    def get_questions_by_topic(self, topic):
        matched = []
        for q in self.questions:
            if q.topic == topic:
                matched.append(q)
        return matched

    def run_quiz(self, quiz_questions, quiz_name):
        randomized = random.sample(quiz_questions, len(quiz_questions))
        score = 0
        missed_ids = []
        incorrect_details = []

        print(f"\nStarting {quiz_name} ({len(randomized)} questions)")

        for i in range(len(randomized)):
            q = randomized[i]
            print(f"\nQuestion {i + 1} of {len(randomized)}:")
            q.display()

            answer = input("Your answer (A-D): ").strip().upper()
            while answer not in ["A", "B", "C", "D"]:
                answer = input("Invalid input. Enter A, B, C, or D: ").strip().upper()

            if answer == q.correct_answer:
                score = score + 1
            else:
                missed_ids.append(q.id)
                incorrect_details.append((q, answer))

        total = len(randomized)
        percentage = round((score / total) * 100, 2)

        self.latest_result = {
            "topic": quiz_name,
            "score": score,
            "total": total,
            "percentage": percentage,
        }
        self.missed_question_ids = missed_ids

        print(f"\nQuiz Complete: {quiz_name}")
        print(f"Score: {score}/{total} ({percentage}%)")

        if len(incorrect_details) == 0:
            print("All answers were correct!")
        else:
            print("\nIncorrect Answers:")
            for item in incorrect_details:
                question = item[0]
                user_ans = item[1]
                correct_ans = question.correct_answer
                print(f"- {question.text}")
                print(f"  Your answer: {user_ans}. {question.options[user_ans]}")
                print(f"  Correct answer: {correct_ans}. {question.options[correct_ans]}")

    def take_quiz(self):
        topics = self.get_topics()
        if len(topics) == 0:
            print("\nNo topics available.")
            return

        print("\nAvailable Topics:")
        valid_choices = []
        for i in range(len(topics)):
            print(f"{i + 1}. {topics[i]}")
            valid_choices.append(str(i + 1))

        choice = input("\nSelect a topic number: ").strip()
        while choice not in valid_choices:
            choice = input("Invalid choice. Select a valid topic number: ").strip()

        selected_topic = topics[int(choice) - 1]
        quiz_questions = self.get_questions_by_topic(selected_topic)
        self.run_quiz(quiz_questions, selected_topic)

    def take_revision_quiz(self):
        if self.latest_result is None:
            print("\nNo previous quiz attempt found. Please take a quiz first.")
            return

        if len(self.missed_question_ids) == 0:
            print(f"\nLatest score: {self.latest_result['score']}/{self.latest_result['total']} ({self.latest_result['percentage']}%)")
            print("You got everything right in your latest attempt. No questions to revise!")
            return

        revision_questions = []
        for q in self.questions:
            if q.id in self.missed_question_ids:
                revision_questions.append(q)

        self.run_quiz(revision_questions, "Revision Quiz")

    def add_question(self):
        print("\nAdd a New Question")
        q_id = input("Enter question ID: ").strip()
        if q_id == "":
            print("Question ID cannot be empty.")
            return
        for q in self.questions:
            if q.id == q_id:
                print("A question with this ID already exists.")
                return

        topic = input("Enter topic (e.g. Python Basics): ").strip()
        if topic == "":
            print("Topic cannot be empty.")
            return
        for existing in self.get_topics():
            if existing.upper() == topic.upper():
                topic = existing

        text = input("Enter question text: ").strip()
        if text == "":
            print("Question text cannot be empty.")
            return

        options = {}
        for letter in ["A", "B", "C", "D"]:
            options[letter] = input(f"Enter option {letter}: ").strip()

        correct = input("Enter correct answer (A-D): ").strip().upper()
        while correct not in ["A", "B", "C", "D"]:
            correct = input("Invalid input. Enter A, B, C, or D: ").strip().upper()

        new_question = Question(q_id, topic, text, options, correct)
        self.questions.append(new_question)
        print("Question added successfully.")

    def edit_question(self):
        print("\nExisting Questions:")
        for q in self.questions:
            print(f"ID {q.id} [{q.topic}]: {q.text}")

        q_id = input("\nEnter the ID of the question to edit: ").strip()
        target = None
        for q in self.questions:
            if q.id == q_id:
                target = q

        if target is None:
            print("Question ID not found.")
            return

        new_topic = input(f"New topic (Enter to keep '{target.topic}'): ").strip()
        if new_topic != "":
            for existing in self.get_topics():
                if existing.upper() == new_topic.upper():
                    new_topic = existing
            target.topic = new_topic

        new_text = input("New question text (Enter to keep current): ").strip()
        if new_text != "":
            target.text = new_text

        for letter in ["A", "B", "C", "D"]:
            new_opt = input(f"New option {letter} (Enter to keep '{target.options[letter]}'): ").strip()
            if new_opt != "":
                target.options[letter] = new_opt

        new_ans = input(f"New correct answer A-D (Enter to keep '{target.correct_answer}'): ").strip().upper()
        while new_ans != "" and new_ans not in ["A", "B", "C", "D"]:
            new_ans = input("Invalid input. Enter A, B, C, or D (or Enter to keep): ").strip().upper()
        if new_ans != "":
            target.correct_answer = new_ans

        print("Question updated successfully.")
