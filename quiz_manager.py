class QuizManager:
    def __init__(self):
        self.questions = []
        self.latest_result = None
        self.missed_question_ids = []

    def load_initial_questions(self):
        pass

    def get_topics(self):
        # Temporary sample topics so your GUI menu has buttons to show
        return ["Python", "Math", "General Knowledge"]

    def get_questions_by_topic(self, topic):
        return []

    def add_question(self, q_id, topic, text, options, correct_answer):
        pass

    def edit_question(self, q_id, new_text, new_options, new_correct_answer):
        pass
