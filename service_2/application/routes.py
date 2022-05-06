from application import app
from flask import Flask, Response, request
import random

raffle_letters = ["O", "L", "M", "K", "A", "U", "B", "N", "I", "D", "H", "V", "E"]

@app.route('/letters', methods=['GET'])
def letters():
    letter_selected = random.choice(raffle_letters)
    return Response(f"{letter_selected}", mimetype='text/plain')