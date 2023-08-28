import requests
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)

CORS(app)


@app.route('/',methods=['GET'])
def home():
    return "hello world"


if( __name__ =='__main__'):
    app.run(debug=True)



