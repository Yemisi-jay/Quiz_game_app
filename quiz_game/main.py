"""# main.py

from quiz.quiz_game import run_quiz

def main():
    run_quiz(amount=10, difficulty='easy')

if __name__ == "__main__":
    main()"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.secret_key = os.environ.get('SECRET_KEY', 'e89ce4d610a577369b1af38a8ade86cf')  # Use a secure, randomly generated key
    app.run(debug=True)
