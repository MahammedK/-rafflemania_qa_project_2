from application import app
from flask import Flask, request, jsonify, Response

extra_prize = {0: "AirPods", 1: "QA CloudAcademy free demo"}
vowels = "AEIOUaeiou"

@app.route('/secondround', methods=['POST'])
def secondround():
    get_letter = (request.get_json()['service_2'])

    for vowels in get_letter:
        if vowels in get_letter:
            return Response(f"{extra_prize[0]}", mimetype = 'text/plain')
        else:
            return Response(f"{extra_prize[1]}", mimetype = 'text/plain')