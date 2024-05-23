from flask import Blueprint, render_template, request, redirect, url_for, session
from quiz.quiz_game import run_quiz

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/start_quiz', methods=['POST'])
def start_quiz():
    amount = 10
    difficulty = 'easy'
    session['score'] = 0
    session['questions'] = run_quiz(amount, difficulty)
    session['current_question'] = 0
    return redirect(url_for('main.quiz'))

@main.route('/quiz')
def quiz():
    if 'questions' not in session:
        return redirect(url_for('main.index'))
    
    question_data = session['questions'][session['current_question']]
    return render_template('quiz.html', question=question_data, question_num=session['current_question'] + 1)

@main.route('/answer', methods=['POST'])
def answer():
    if 'questions' not in session:
        return redirect(url_for('main.index'))

    user_answer = request.form.get('answer')
    correct_answer = session['questions'][session['current_question']]['correct_answer']

    if user_answer == correct_answer:
        session['score'] += 1

    session['current_question'] += 1

    if session['current_question'] >= len(session['questions']):
        return redirect(url_for('main.result'))

    return redirect(url_for('main.quiz'))

@main.route('/result')
def result():
    if 'score' not in session:
        return redirect(url_for('main.index'))

    score = session['score']
    total = len(session['questions'])

    return render_template('result.html', score=score, total=total)
