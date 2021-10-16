import csv
from flask import Flask, jsonify, request
 
app = Flask(__name__)

data=[
    {
        'name': 'saumya',
        'class': 8,
        'age': 13
    },
    {
        'city': 'faridabad',
        'school': 'mdps',
        'friend': 'tanisha'
    }
]

@app.route("/")
def func():
    return "this is my first API and data in it"


@app.route("/getdata")
def fun():
    return jsonify({
        'data': data
    })


@app.route("/uploaddata", methods=["POST"])
def funct():
    data2={
        'hobby': 'kickboxing',
        'pet': 'oggy',
        'state': 'haryana'
    }
    data.append(data2)
    return jsonify({
        'data': data,
        'message': 'data successfully uploaded'
    })


if __name__ == "__main__":
    app.run()
 