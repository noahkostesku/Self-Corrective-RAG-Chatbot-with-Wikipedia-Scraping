from flask import Flask, render_template, request, jsonify
from demo import self_corrective_rag

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        feedback = request.form.get('feedback')  
        result = self_corrective_rag(question, feedback)
        return jsonify(result) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
