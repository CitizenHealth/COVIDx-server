from .actions import LocationActions
# from .covid_tracking import pull_recent
from . import location

@location.route('/get_location', methods=['GET'])
def all_location():
    return LocationActions.get_all_users()

@location.route('/get_county_results', methods=['GET'])
def get_results_county():
    return LocationActions.get_county_results()

@location.route('/get_state_results', methods=['GET'])
def get_results_state():
    return LocationActions.get_state_results()

@location.route('/get_state_county_results', methods=['GET'])
def get_results_state():
    return LocationActions.get_state_county_results()