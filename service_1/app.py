from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    letter_drawn = requests.get('http://service_2:5000/letters')
    prize_drawn = requests.get('http://service_3:5000/prizes')
    return Response(f"{letter_drawn.text} {prize_drawn.text}", mimetype="text/plain")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)