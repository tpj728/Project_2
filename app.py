import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
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
    Value_Rating = db.Column(db.Integer)
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

    # Use Pandas to perform the sql query
    results = db.session.query(Cars.State, Cars.Model, Cars.Make, Cars.Manufacturer_Suggested_Retail_Price, Cars.Used_Car_Value, Cars.Value_Rating, \
        Cars.Engine_Name, Cars.Transmission_Name, Cars.Trim, Cars.Class, Cars.Horsepower, Cars.Standard_MPG, Cars.Body_Style, \
            Cars.Drivetrain, Cars.Fuel_Type, Cars.Seating_Capacity).all()

    """Return table data."""
    return render_template('data.html', items=results)

if __name__ == "__main__":
    app.run()
