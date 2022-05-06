from application import app 
from flask import Flask, request, Response, jsonify
import requests

@app.route('/')
def home():
    letter_drawn = requests.get('http://service_2:5000/letters').json()
    prize_drawn = requests.get('http://service_3:5000/prizes').json()

    fields = {'letter_drawn': letter_drawn, 'prize_drawn': prize_drawn}

    final_draw = requests.get('http://service_4:5000/secondround', json=fields)

    return Response(f"{letter_drawn.text} {prize_drawn.text} {final_draw}", mimetype="text/plain") #change response for html and remove mimetype

    # return render_template('main.html', final_draw=final_draw.json())