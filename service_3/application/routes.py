from application import app
from flask import Flask, Response, request
import random

raffle_prizes = ["Day at 10 Downing Street", "CheeseStrings", "£50 Amazon Voucher", "PortaLoo", "Can of Tuna", "Sparkling Water", "3 Nights at Disneyland Paris", "Free London Marathon Entry", "Mouthwash", "Hand Sanitiser", "Toilet Roll", "A Sock", "Monica Geller's Turkey"]

@app.route('/prizes', methods=['GET'])
def prizes():
    prize_selected = random.choice(raffle_prizes)
    return Response(f"{prize_selected}", mimetype='text/plain')