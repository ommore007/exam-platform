from flask import Flask, render_template, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'secret'

# Categories आणि Years
CATEGORIES = ["पोलिस", "आर्मी", "तलाठी", "SSC", "रेल्वे"]
YEARS = ["2021", "2022", "2023", "2024", "2025", "2026"]

# 100 प्रश्न (पोलिस साठी, बाकी category साठी सध्या same)
def get_questions():
    q = []
    for i in range(1, 101):
        q.append({
            "text": f"प्रश्न {i}: खालीलपैकी योग्य पर्याय निवडा?",
            "options": ["पर्याय A", "पर्याय B", "पर्याय C", "पर्याय D"],
            "correct": 0
        })
    return q

@app.route('/')
def index():
    return render_template('index.html', categories=CATEGORIES, years=YEARS)

@app.route('/start/<category>/<year>/<paper>')
def start_exam(category, year, paper):
    session['category'] = category
    session['year'] = year
    session['paper'] = paper
    session['questions'] = get_questions()
    session['answers'] = [-1] * 100
    session['q_index'] = 0
    return redirect(url_for('exam'))

@app.route('/exam', methods=['GET', 'POST'])
def exam():
    if request.method == 'POST':
        # उत्तर सेव करा
        answer = int(request.form['answer'])
        idx = session['q_index']
        answers = session['answers']
        answers[idx] = answer
        session['answers'] = answers
        
        # पुढील प्रश्न किंवा निकाल
        if idx + 1 < 100:
            session['q_index'] = idx + 1
            return redirect(url_for('exam'))
        else:
            return redirect(url_for('result'))
    
    idx = session['q_index']
    q = session['questions'][idx]
    return render_template('exam.html', 
                         question=q,
                         q_num=idx+1,
                         total=100,
                         category=session['category'],
                         year=session['year'],
                         paper=session['paper'])

@app.route('/result')
def result():
    answers = session['answers']
    questions = session['questions']
    score = 0
    for i in range(100):
        if answers[i] == questions[i]['correct']:
            score += 1
    return render_template('result.html', score=score, total=100)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
