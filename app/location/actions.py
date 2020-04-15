from flask import request, jsonify
from app import db
from datetime import datetime
import uuid
import sqlalchemy
from .covid_tracking import get_counties, get_states, get_state_counties
# from firebase_admin import credentials, firestore, initialize_app, auth

from models.location import Location, StateResults


class LocationActions:

    def __init__(self, testing=False):
        return

    def get_all_users():
        """
        return all users
        """
        try:
            query_parameters = request.args
            payload = [i.as_json for i in Location.query.all()]

            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"

    def get_county_results():
        """
        return all users
        """
        try:
            payload = get_counties()


            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"

    def get_state_results():
        """
        return all users
        """
        try:
            payload = get_states()


            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"

    def get_state_county_results():
        """
        return all users by state name
        """
        try:
            payload = get_state_counties()


            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"


