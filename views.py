from flask import Flask
app = Flask(__name__)


@app.route('/movie/<title>')
def movie_info():
    return 'read'

@app.route('/')
def index():
    return """<html><body>
        <h1>Главная страница.</h1>
        <h3><a href="/hello/">Страница приветствия...</a></h3>
        </body></html>"""

@app.route('/hello/')
def hello():
    return """<html><body>
        <h1>Привет Flask!</h1>
        <h3><a href="/"><= назад</a></h3>
        </body></html>"""

if __name__ == '__main__':
    app.run()