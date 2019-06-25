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


# #################################################
# # Database Setup
# #################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/cars.sqlite"
# db = SQLAlchemy(app)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/map")
def map():
    """Return the map page."""
    return render_template("map.html")    

# @app.route("/data")
# def names():
#     """Return table data."""

#     # Use Pandas to perform the sql query
#     results = db.session.query(car_stats.State, car_stats.Make, car_stats.Manufacturer_Suggested_Retail_Price, car_stats.Used_Car_Value, car_stats.Value_Rating, \
#         car_stats.Engine_Name, car_stats.Transmission_Name, car_stats.Trim, car_stats.Class, car_stats.Horsepower, car_stats.Standard_MPG, car_stats.Body_Style, \
#             car_stats.Drivetrain, car_stats.Fuel_Type, car_stats.Seating_Capacity).all()

#     print(results)
#     print(type(results))

if __name__ == "__main__":
    app.run()
