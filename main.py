from quiz_manager import QuizManager

manager = QuizManager()
manager.load_initial_questions()

choice = ""
while choice != "5":
    print("\nQuiz Practice Application")
    print("\nLearner Options:")
    print("1. Take Quiz")
    print("2. Take Revision Quiz")
    print("\nInstructor Options:")
    print("3. Add Question")
    print("4. Edit Question")
    print("\n5. Exit")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        manager.take_quiz()
    elif choice == "2":
        manager.take_revision_quiz()
    elif choice == "3":
        manager.add_question()
    elif choice == "4":
        manager.edit_question()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
