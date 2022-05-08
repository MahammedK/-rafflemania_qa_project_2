from application import app 
from flask import Flask, request, Response, jsonify, render_template
import requests

@app.route('/')
def home():
    letter_drawn = requests.get('http://service_2:5000/letters')
    prize_drawn = requests.get('http://service_3:5000/prizes')

    # fields = {'letter_drawn': letter_drawn, 'prize_drawn': prize_drawn}

    final_draw = requests.get('http://service_4:5000/secondround')

    raffle_prize = f"Raffle letter '{letter_drawn.text}', gets the prize of '{prize_drawn.text}' and also '{final_draw.text}'" 
    return render_template('index.html', raffle_prize=raffle_prize)

    # return render_template('main.html', final_draw=final_draw.json())