from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    name = request.args.get('name')
    word = ['red', 'blue', 'green']
    return render_template("index.html", name=name, word=word)

@app.route('/index',methods=['post'])
def post():
    name = request.form['name']
    word = ['red', 'blue', 'green']
    return render_template('index.html',name=name, word=word)

if __name__ == "__main__":
    app.run(debug=True)
