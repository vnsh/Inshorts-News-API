#Coded by Sumanjay on 29th Feb 2020
from flask import Flask, request, jsonify
from inshorts import getNews
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "inshort_api_clone"
CORS(app)

@app.route('/')
def home():
    return 'News API is UP!<br><br>'

@app.route('/news')
def news():
    if request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
