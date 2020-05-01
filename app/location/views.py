from flask import request, jsonify
from app import db
from datetime import datetime
import uuid
import sqlalchemy
from .actions import get_counties, get_states, get_state_counties

from models.location import Location, StateResults
from . import location


@location.route('/get_location', methods=['GET'])
def all_location():
    try:
        query_parameters = request.args
        payload = [i.as_json for i in Location.query.all()]

        if payload:
            return jsonify(payload=payload, ok=True), 200

        else:
            return jsonify(payload=None, ok=False), 200

    except Exception as e:
        return f"An Error Occured: {e}"


@location.route('/get_county_results', methods=['GET'])
def get_results_county():
    try:
        payload = get_counties()


        if payload:
            return jsonify(payload=payload, ok=True), 200

        else:
            return jsonify(payload=None, ok=False), 200

    except Exception as e:
        return f"An Error Occured: {e}"


@location.route('/get_state_results', methods=['GET'])
def get_results_state():
    try:
        payload = get_states()


        if payload:
            return jsonify(payload=payload, ok=True), 200

        else:
            return jsonify(payload=None, ok=False), 200

    except Exception as e:
        return f"An Error Occured: {e}"


@location.route('/get_state_county_results', methods=['GET'])
def get_results_state_county():
    try:
        payload = get_state_counties()


        if payload:
            return jsonify(payload=payload, ok=True), 200

        else:
            return jsonify(payload=None, ok=False), 200

    except Exception as e:
        return f"An Error Occured: {e}"


