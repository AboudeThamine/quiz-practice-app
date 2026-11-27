# Project Context: Quiz Practice Application (Terminal / CLI)

## CORE PHILOSOPHY (READ FIRST)
- **Write the simplest possible code that works with zero bugs.**
- **No unnecessary features, no decorative banners, no extra helper classes, and no clever tricks.**
- **Keep the code short, direct, and minimal—just enough to fulfill the 4 assignment requirements cleanly.**
- Every line must be easy enough for 4 first-year students to trace and explain out loud to their professor.

## Assignment Requirements
Build a Python Quiz Practice Application using Object-Oriented Programming with two core classes: `Question` and `QuizManager`.
1. Store at least 8 questions (each with an ID, topic, 4 options A–D, and 1 correct answer). Allow questions to be added and edited.
2. Let a learner select a topic/quiz and answer all questions in it. Accept only options A to D (do not count invalid input as an answer).
3. Calculate the score and percentage. Show each incorrect answer alongside the correct answer, and save the learner's latest result and missed question IDs.
4. Offer a revision quiz using the questions missed in the learner's latest attempt. If there is no previous attempt or no missed questions, display an appropriate message.

## App Design & Structure
- **Interface:** Plain terminal / command-line interface using standard `input()` and `print()`.
- **Topic & Randomization:** Focuses on **Python** as the main topic, containing a pool of 12+ questions across 4–5 quiz sets (or selectable under Python). Use `random.sample()` (or `random.shuffle()`) so each quiz attempt presents randomized questions in a new order.
- **In-Memory Storage:** Store questions, `latest_result`, and `missed_question_ids` inside `QuizManager` attributes (lists/dictionaries). Do NOT use external files, JSON, or databases.
- **Menu Separation:** Separate Learner options (Take Quiz, Take Revision Quiz) from Instructor options (Add Question, Edit Question) in the main menu.

## File & Team Division (4 Members)
- `question.py`: Defines the `Question` class (`__init__`, instance attributes `id`, `topic`, `text`, `options`, `correct_answer`, and a simple display method).
- `quiz_manager.py`: Defines the `QuizManager` class managing the question list, initial Python questions, adding/editing questions by ID, running randomized quizzes with `A–D` validation, calculating score/percentage, saving `latest_result` and `missed_question_ids`, and running the revision quiz.
- `main.py`: Simple `while` loop terminal menu that creates a `QuizManager` object and calls its methods.

## Strict Syllabus Constraints
- **Use ONLY topics from the course syllabus:**
  - Data types, variables, expressions, `input()`, `print()`, f-strings, `round()`
  - Decision structures (`if`, `elif`, `else`, `and`/`or`/`not`, `in`)
  - Repetition structures (`while` loops, `for` loops, nested loops)
  - Functions (`def`, parameters, `return`) and modular `.py` files
  - Lists, tuples, strings (`.upper()`, `.strip()`), dictionaries, and sets
  - Objects and classes (`class`, `__init__`, `self`, instance attributes, methods, `__str__`)
  - Built-in `random` module (`random.sample()` or `random.shuffle()`)
- **Strictly EXCLUDE unlearned or complex features:**
  - NO File I/O (`open()`, `with`, CSV, JSON)
  - NO `try` / `except` blocks
  - NO list/dictionary comprehensions, `lambda`, decorators, `*args`/`**kwargs`, or GUI libraries
  - NO redundant error-checking bloat or over-engineered abstractions—keep every method short, direct
