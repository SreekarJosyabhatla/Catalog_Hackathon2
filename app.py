from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for quizzes
quizzes = []

@app.route('/')
def index():
    return render_template('index.html', quizzes=quizzes)

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        name = request.form['name']
        questions = request.form.getlist('question')
        correct_answers = request.form.getlist('correct_answer')
        quiz = {'name': name, 'questions': []}
        for q, a in zip(questions, correct_answers):
            quiz['questions'].append({'question': q, 'correct_answer': a})
        quizzes.append(quiz)
        return redirect(url_for('index'))
    return render_template('create_quiz.html')

@app.route('/participate/<int:quiz_id>', methods=['GET', 'POST'])
def participate(quiz_id):
    quiz = quizzes[quiz_id]
    if request.method == 'POST':
        answers = request.form.getlist('answer')
        score = sum(1 for i, q in enumerate(quiz['questions']) if q['correct_answer'] == answers[i])
        return render_template('participate.html', quiz=quiz, score=score)
    return render_template('participate.html', quiz=quiz)

if __name__ == '__main__':
    app.run(debug=True)
