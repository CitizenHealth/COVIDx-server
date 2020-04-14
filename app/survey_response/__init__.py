from flask import Blueprint

survey_response = Blueprint("survey_response", __name__)

from . import views
