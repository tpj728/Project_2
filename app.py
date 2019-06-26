import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, json
from flask_sqlalchemy import SQLAlchemy

import itertools

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
    plot_results = db.session.query(Cars.Make, Cars.Model, Cars.Manufacturer_Suggested_Retail_Price, Cars.Used_Car_Value).all()

    car_info = []
    plot_info = [['Car', 'MSRP', 'Used Car Value']]

    for result in plot_results:
        car_info.append(f'{result[0]} {result[1]}')
        car_info.append(int(result[2].replace('$','').replace(',','')))
        car_info.append(int(result[3].replace('$','').replace(',','')))
        plot_info.append(car_info)
        car_info = []

    plot_info.sort()
    plot_info = list(plot_info for plot_info,_ in itertools.groupby(plot_info))    

    """Return plot data."""
    return render_template('plots.html', prices=json.dumps(plot_info))


if __name__ == "__main__":
    app.run()
