from flask import *   # flask class define and import flask 

app = Flask(__name__)   # class object app is declared , here name is arugment of flask constructor 

@app.route('/')  # flask decorators, define decortaors must use leading slash
def admin():
    return render_template('index.html')

@app.route('/abc')         # url to redirect page to the template called
def student():
    return render_template('student.html')

if __name__=='__main__':           # closing 
    app.run(debug = True, port = 8000)
