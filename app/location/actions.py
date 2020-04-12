from flask import request, jsonify
from app import db
from datetime import datetime
from .covid_tracking import pull_recent
import uuid
import sqlalchemy
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

    def get_all_states():
        """
        return all users
        """
        try:
            query_parameters = request.args
            payload = [i.as_json for i in StateResults.query.all()]

            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"

