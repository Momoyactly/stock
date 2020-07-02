import requests
from flask import render_template, url_for, flash, redirect
from app import app, db
from datetime import datetime
from app.models import btc_mxn





@app.route("/")
def home(): 
    respuesta = requests.get("https://api.bitso.com/v3/ticker/?book=btc_mxn").json()
    if respuesta["success"]:
        datos = respuesta["payload"]
        print(datos["created_at"])
        fecha,horario =  datos["created_at"].split("T")
        ano,mes,dia = fecha.split("-")
        hora,minuto,segundo = horario.split("+")[0].split(":")
        registro = btc_mxn(last = datos["last"],volume = datos["volume"] ,created_at = datetime(int(ano),int(mes),int(dia),int(hora),int(minuto)).strftime('%s'))
        db.session.add(registro)
        db.session.commit()
        print(respuesta)
        return str(respuesta)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

