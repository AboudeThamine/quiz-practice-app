class Question:
    def __init__(self, q_id, topic, text, options, correct_answer):
        self.id = q_id
        self.topic = topic
        self.text = text
        self.options = options  # {"A": "...", "B": "...", "C": "...", "D": "..."}
        self.correct_answer = correct_answer.upper()
