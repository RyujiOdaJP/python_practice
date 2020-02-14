from flask import Flask,render_template
from search import GetHtml,ParseHtml

from flask import Markup

app = Flask(__name__)



@app.route('/')
# @app.route("/index")
def index():
    # name = request.args.get('name')
    # word = ['red', 'blue', 'green']
    html = GetHtml().getText()
    parse = ParseHtml().parseName_Date(html)
    info = ''
    for i in range(len(parse)):
        info += '<h1>' + parse[i] + '</h1><br>'

    return render_template("index.html", parse=Markup(info))

# @app.route('/index',methods=['post'])
# def post():
#     name = request.form['name']
#     word = ['red', 'blue', 'green']
#     return render_template('index.html',name=name, word=word)

if __name__ == "__main__":
    app.run(debug=True)
