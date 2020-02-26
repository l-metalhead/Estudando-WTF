from flask import Flask


app = Flask('What_the_Flask_Tutorial')

app.config['SECRET_KEY'] = "schablau"
app.config['DEBUG'] = True

from flask.ext.magic import MakeMagic
MakeMagic(app)
