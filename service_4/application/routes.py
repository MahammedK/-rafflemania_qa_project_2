from application import app
from flask import Flask, request, jsonify, Response
import requests, json

@app.route('/secondround', methods=['POST'])
def secondround():
    raffle_letters = request.get_json()['Letters']
    get_prizes = request.get_json()['Prizes']

    
    if raffle_letters=='A':
        extra_prize = "Airpods"

    elif raffle_letters=='E':
        extra_prize = "Airpods"

    elif raffle_letters=='I':
        extra_prize = "Airpods"

    elif raffle_letters=='O':
        extra_prize = "Airpods"

    elif raffle_letters=='U':
        extra_prize = "Airpods"

    elif get_prizes.startswith('A'):
        extra_prize = "Airpods"

    else:
        extra_prize = "QA CloudAcademy free demo"

    return Response(f"{extra_prize}", mimetype='text/plain')

