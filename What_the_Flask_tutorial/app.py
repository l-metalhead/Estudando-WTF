from flask import Flask


app = Flask('What_the_Flask_Tutorial')

@app.route('/<name>')
def index(name):
    if name.lower() == 'lucas':
        return f'Olá {name}', 200
    return 'Not Found', 404

app.run()