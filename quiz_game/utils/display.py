
# utils/display.py

import random

def display_question(question, index):
    """
    Display a single quiz question and its options.

    :param question: A quiz question
    :param index: Question number
    """
    print(f"Question {index + 1}: {question['question']}")
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"  {chr(65 + i)}. {option}")
    return options

def get_user_input():
    """
    Get user input for their answer choice.
    """
    while True:
        answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("Invalid input. Please enter A, B, C, or D.")
