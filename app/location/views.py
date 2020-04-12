from .actions import LocationActions
# from .covid_tracking import pull_recent
from . import location

@location.route('/get_location', methods=['GET'])
def all_location():
    return LocationActions.get_all_users()

@location.route('/get_all_states_positive', methods=['GET'])
def get_all_states():
    return LocationActions.get_all_states_positive()