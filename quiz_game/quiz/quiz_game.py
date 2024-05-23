
# quiz/quiz_game.py

from quiz.question import fetch_quiz_questions
from utils.display import display_question, get_user_input

def run_quiz(amount=10, category=None, difficulty='easy'):
    """
    Run the quiz by fetching and displaying questions one at a time.

    :param amount: Number of questions to fetch and display
    :param category: Optional category of questions
    :param difficulty: Optional difficulty level ('easy', 'medium', 'hard')
    """
    print("Fetching quiz questions...")
    questions = fetch_quiz_questions(amount, category, difficulty)
    
    score = 0
    for index, question in enumerate(questions):
        options = display_question(question, index)
        user_answer = get_user_input()
        
        correct_answer = question['correct_answer']
        correct_option = chr(65 + options.index(correct_answer))
        
        if user_answer == correct_option:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_option}. {correct_answer}\n")
        
        if index < len(questions) - 1:
            input("Press Enter to proceed to the next question...")

    print(f"Quiz completed! Your score is {score}/{amount}.")
    if score == amount:
        print("Congratulations! You got all questions correct!")
    else:
        print("Try again to get a perfect score!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        run_quiz(amount, category, difficulty)
