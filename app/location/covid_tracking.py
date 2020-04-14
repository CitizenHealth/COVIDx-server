import requests as rq
import csv
import os
import uuid
import MySQLdb 
from dateutil.parser import parse


def pull_recent():
    """
    get recent data from covidtracking.com
    """

    covid_tracking = rq.get("https://covidtracking.com/api/v1/states/current.json").json()
    states_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_experiment", "states_coords.csv")

    with open(states_csv, "r") as f:
        csv_file = csv.reader(f, delimiter=",")
        csv_unpacked = [row for row in csv_file]
        states_coords = [{csv_unpacked[0][i]: row[i] for i in range(len(row))} for row in csv_unpacked]

    for covid_row in covid_tracking:
        for coords_row in states_coords:
            if covid_row['state']==coords_row['state']:
                covid_row['longitude']=coords_row['longitude']
                covid_row['latitude']=coords_row['latitude']
                covid_row['name']=coords_row['name']
                # covid_row['dateModified'] = parse(covid_row['dateModified']).strftime('%Y-%m-%d %H:%M:%S')
                # covid_row['dateChecked'] = parse(covid_row['dateChecked']).strftime('%Y-%m-%d %H:%M:%S')

    return covid_tracking

# def covid_tracking_to_db(environ="prod"):
#     """
#     put api results into the db
#     """
#     # DB_URI = 
#     try: 
#         recent_data = pull_recent()
#         if environ=="prod":
#             host = "aa19bixxzoxyunw.cxnedy40wg8c.us-west-2.rds.amazonaws.com"
#             username = "admin"
#             password = "^zT_UIsJ5Au1(v6e"
#             db_name = "covidx_db"
#         db = MySQLdb.connect(host, username, password, db_name)
#         cur = db.cursor()
#         for state in recent_data:
#             placeholders = ", ".join(["%s"] * len(state))
#             columns = ', '.join(state.keys())
#             query = "INSERT INTO state_results (%s) VALUES (%s)" % (columns, placeholders)
#             cur.execute(query, state.values())

#         db.commit()

#     except Exception as e:
#         return f"An Error Occured: {e}"
