from .actions import SurveyResponseActions
from . import survey_response


@survey_response.route("/create_survey_response", methods=["POST"])
def create_survey_response():
    return SurveyResponseActions.create()
