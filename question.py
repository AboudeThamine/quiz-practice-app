class Question:
    def __init__(self, q_id, topic, quiz, text, options, correct_answer):
        self.id = q_id
        self.topic = topic
        self.quiz = quiz
        self.text = text
        self.options = options
        self.correct_answer = correct_answer.upper()

    def display(self):
        print(f"\n{self.text}")
        for letter in ["A", "B", "C", "D"]:
            print(f"  {letter}. {self.options[letter]}")
