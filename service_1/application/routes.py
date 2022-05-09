from application import app 
from flask import Flask, request, Response, jsonify, render_template
import requests, json

@app.route('/', methods = ["GET", "POST"])
def home():
    letter_drawn = requests.get('http://service_2:5000/letters').text
    prize_drawn = requests.get('http://service_3:5000/prizes').text

    fields = {'Letters': letter_drawn, 'Prizes': prize_drawn}

    final_draw = requests.post('http://service_4:5000/secondround', json=fields)  #json=fields

    raffle_prize = f"Entrant with the raffle letter '{letter_drawn}', gets the prize of '{prize_drawn}', along with '{final_draw.text}'" 
    return render_template('index.html', raffle_prize=raffle_prize)

    # return render_template('main.html', final_draw=final_draw.json())