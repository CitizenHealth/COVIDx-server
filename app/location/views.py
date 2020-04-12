from data_interface import LocationActions
from . import location

@location.route('/get_location', methods=['GET'])
def all_location():
    return LocationActions.get_all()
