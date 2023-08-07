from flask import Blueprint, request, jsonify, make_response, abort
from dotenv import load_dotenv
import os
import json
import pandas as pd
from app.spark.pipeline import filtered_df, max_base_df, get_max

analytics_bp = Blueprint("analytics_bp", __name__, url_prefix="/analytics")

# --------------------------ANALYTICS ROUTES--------------------------

@analytics_bp.route("/analytics", methods=["GET"])
def get_filtered_df():
    df = filtered_df()
    return jsonify(df.to_dict(orient='records'))

@analytics_bp.route("/base", methods=["GET"])
def get_base_df():
    df = max_base_df()
    return jsonify(df.to_dict(orient='records'))

@analytics_bp.route("/sweetness", methods=["GET"])
def get_sweetness_df():
    df = get_max('sweetness')
    return jsonify(df.to_dict(orient='records'))

@analytics_bp.route("/temp", methods=["GET"])
def get_temp_df():
    df = get_max('temp')
    return jsonify(df.to_dict(orient='records'))

@analytics_bp.route("/toppings", methods=["GET"])
def get_toppings_df():
    df = get_max('toppings')
    return jsonify(df.to_dict(orient='records'))