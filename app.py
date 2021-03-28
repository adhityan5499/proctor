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
    if request.method=='POST':
        if request.form['submit']=='submit':
            import subprocess
            import json
            output = subprocess.Popen(["python", "audio_save_required_audios_only.py",time], shell=True, stdout=subprocess.PIPE)
            jsonS, _ = output.communicate()
            data = json.loads(jsonS)
            results = []
            for i in f: results.append(i)
            return redirect(url_for('result', name=anme, rollno=rollno, time=time, results=results))

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

@app.route('/result', methods=['GET', 'POST'])
def result():
    name = request.args.get('name', None)
    rollno = request.args.get('rollno', None)
    time = request.args.get('time', None)
    f = open('results.txt','r')
    results = []
    for i in f: results.append(i)
    return render_template('result.html', name=name, rollno=rollno, time=time, questions=questions, results=results)

if __name__ == '__main__':
    app.run(debug=True)
