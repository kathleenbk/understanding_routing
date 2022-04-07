from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output=""
    for i in range (0, num):
        output = output + f"{word}"

    return output




if __name__=="__main__":
    app.run(debug=True)