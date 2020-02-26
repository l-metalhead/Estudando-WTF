from flask import Flask, render_template


app = Flask('What_the_Flask_Tutorial')

@app.route('/html_page/<nome>')  # template path
def html_page(nome):
    return render_template('html_page.html', nome=nome)

app.run()