from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/question-with-one-answer')
def index():
    return render_template('question.html')


@app.route('/the-question/')
def question():
    questiontext = request.args.get('questiontext')
    dropdown = request.args.get('dropdown')
    return render_template('answer.html', questiontext=questiontext, dropdown=dropdown)


if __name__ == '__main__':
    app.run(
        debug=True
    )
