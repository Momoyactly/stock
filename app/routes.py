import requests
from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import btc_mxn





@app.route("/")
def home(): 
    respuesta = requests.get("https://api.bitso.com/v3/ticker/?book=btc_mxn").json()
    if respuesta["success"]:
        datos = respuesta["payload"]
        registro = btc_mxn(last = datos["last"],volume =datos["volume"] ,created_at =datos["created_at"])
        db.session.add(registro)
        db.session.commit()
        print(respuesta)
        return str(respuesta)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

