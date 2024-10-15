from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola 4°D del Andrés Bello!'
    return 'estoy cansado jefe'

@app.route('/menu')
 return 'hola mundo'
if __name__ == '__main__':
    app.run(debug=True)
