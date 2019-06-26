import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/cars.sqlite"
db = SQLAlchemy(app)

class Cars(db.Model):
    __tablename__ = 'car_stats'
    id = db.Column(db.Integer, primary_key = True)
    State = db.Column(db.String(30))
    Model = db.Column(db.String(30))  
    Make = db.Column(db.String(30))
    Manufacturer_Suggested_Retail_Price = db.Column(db.String(30))
    Used_Car_Value = db.Column(db.String(30))
    Engine_Name = db.Column(db.String(100))
    Transmission_Name = db.Column(db.String(50))
    Trim = db.Column(db.String(30))
    Class = db.Column(db.String(50))
    Horsepower = db.Column((db.String(100)))
    Standard_MPG = db.Column(db.String(50))
    Body_Style = db.Column(db.String(30))
    Drivetrain = db.Column(db.String(50))
    Fuel_Type = db.Column(db.String(50))
    Seating_Capacity = db.Column(db.String(30))

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/map")
def map():
    """Return the map page."""
    return render_template("map.html")    

@app.route("/data")
def data():

    results = db.session.query(Cars.State, Cars.Model, Cars.Make, Cars.Manufacturer_Suggested_Retail_Price, Cars.Used_Car_Value, \
        Cars.Engine_Name, Cars.Transmission_Name, Cars.Trim, Cars.Class, Cars.Horsepower, Cars.Standard_MPG, Cars.Body_Style, \
            Cars.Drivetrain, Cars.Fuel_Type, Cars.Seating_Capacity).all()

    """Return table data."""
    return render_template('data.html', items=results)

@app.route("/plots")
def plots():
    plot_results = db.session.query(Cars.Make, Cars.Model, Cars.Manufacturer_Suggested_Retail_Price, Cars.Used_Car_Value).distinct()

    car_info = []
    plot_info = [['Car', 'MSRP', 'Used Car Value']]

    for result in plot_results:
        car_info.append(f'{result[0]} {result[1]}')
        car_info.append(int(result[2].replace('$','').replace(',','')))
        car_info.append(int(result[3].replace('$','').replace(',','')))
        plot_info.append(car_info)
        car_info = []

    plot_info.sort()


    model_group = db.session.query(Cars.Model, func.count(Cars.State)).group_by(Cars.Model)

    model = []
    model_count = []

    for mod in model_group:
        model.append(mod[0])
        model_count.append(mod[1])

    make_group = db.session.query(Cars.Make, func.count(Cars.State)).group_by(Cars.Make)

    make = []
    make_count = []

    for mak in make_group:
        make.append(mak[0])
        make_count.append(mak[1])

    body_group = db.session.query(Cars.Body_Style, func.count(Cars.State)).group_by(Cars.Body_Style)

    body = []
    body_count = []

    for bod in body_group:
        body.append(bod[0])
        body_count.append(bod[1])    

    """Return plot data."""
    return render_template('plots.html', prices=json.dumps(plot_info), model=json.dumps(model), model_count=json.dumps(model_count), \
        make=json.dumps(make), make_count=json.dumps(make_count), body=json.dumps(body), body_count=json.dumps(body_count))


if __name__ == "__main__":
    app.run()
