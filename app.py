from flask import Flask, jsonify, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'enter':
            return redirect(url_for('exam', name=request.form['name'], rollno=request.form['rollno'], time=request.form['time']))
    return render_template('home.html')


@app.route('/exam', methods=['GET', 'POST'])
def exam():
    name = request.args.get('name', None)
    rollno = request.args.get('rollno', None)
    time = request.args.get('time', None)
    questions = []
    f = open('question_paper.txt', 'r')
    q = []
    for i in f:
        if i[0] == 'D':
            questions.append(q+[i])
            q = []
        else:
            q.append(i)

    return render_template('exam.html', name=name, rollno=rollno, time=time, questions=questions)


if __name__ == '__main__':
    app.run(debug=True)
