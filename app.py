#app.py
from flask import jsonify # <- `jsonify` instead of `json`
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app


@app.route('/hello/<name>')
def json_example(name):
    return jsonify({'message': "Hola "+name+" From a6c9cbf549bd"}) 

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
