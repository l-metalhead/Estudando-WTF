from flask import Flask


app = Flask('What_the_Flask_Tutorial')

@app.route('/')
def hello_world():
    return 'Hello World! <strong>I\'m learning Flask</strong>', 200

app.run()