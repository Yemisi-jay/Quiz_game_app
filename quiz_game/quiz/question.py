
# quiz/question.py

import requests

def fetch_quiz_questions(amount=10, category=None, difficulty=None):
    """
    Fetch quiz questions from the Open Trivia Database API.

    :param amount: Number of questions to fetch
    :param category: Optional category of questions
    :param difficulty: Optional difficulty level ('easy', 'medium', 'hard')
    :return: List of questions
    """
    url = 'https://opentdb.com/api.php'
    params = {
        'amount': amount,
        'type': 'multiple'  # Only fetch multiple choice questions
    }
    if category:
        params['category'] = category
    if difficulty:
        params['difficulty'] = difficulty

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()

    return data['results']
