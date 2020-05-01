import requests as rq
import csv
import os
from flask import request
# import uuid
# import MySQLdb 
# from dateutil.parser import parse
import json
from datetime import datetime
import subprocess



def geojson_to_dict(path):
    with open(path, "r") as f:
        counties_coords = json.load(f)
    return counties_coords


def csv_to_dict(path):
    with rq.Session() as s:
        download = s.get(path)
        decoded = download.content.decode("utf-8")
        cr = csv.reader(decoded.splitlines(), delimiter=',')
        csv_unpacked = [row for row in list(cr)]
        states_coords = [{csv_unpacked[0][i]: row[i] for i in range(len(row))} for row in csv_unpacked][1:]
    return states_coords

def get_counties(): 
    PATH_COORDS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_experiment", "us_counties_coords.geojson")
    PATH_COVID = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

    counties_coords = geojson_to_dict(PATH_COORDS)
    counties_covid = csv_to_dict(PATH_COVID)
    
    counties_covid_recent = {}
    for county in counties_covid:
        curr_keys = counties_covid_recent.keys()
        this_fip = county['fips']
        this_deaths = int(county['deaths'])
        this_cases = int(county['cases'])
        this_date = datetime.strptime(county['date'], "%Y-%m-%d")

        if this_fip in curr_keys and this_date > counties_covid_recent[this_fip]['date']:
            counties_covid_recent[this_fip] = {'date':this_date, 'cases':this_cases, 'deaths':this_deaths}
        elif this_fip not in curr_keys:
            counties_covid_recent[this_fip] = {'date':this_date, 'cases':this_cases, 'deaths':this_deaths}

    for county_poly in counties_coords["features"]:
        for covid_key, covid_value in counties_covid_recent.items():
            if county_poly['properties']['FIPS']==covid_key:
                county_poly['properties']['cases']=covid_value['cases']
                county_poly['properties']['deaths']=covid_value['deaths']
                break
                
    return counties_coords

def get_state_counties(): 
    state = request.args.get("state", type=str)
    PATH_COORDS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_experiment", "us_counties_coords.geojson")
    PATH_COVID = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

    _counties_coords = geojson_to_dict(PATH_COORDS)
    counties_coords = {**_counties_coords, 'features':[feat for feat in _counties_coords['features'] if feat['properties']['STATE_NAME']==state]}
    _counties_covid = csv_to_dict(PATH_COVID)
    counties_covid = [county for county in _counties_covid if county['state']==state]
    
    counties_covid_recent = {}
    for county in counties_covid:
        curr_keys = counties_covid_recent.keys()
        this_fip = county['fips']
        this_deaths = int(county['deaths'])
        this_cases = int(county['cases'])
        this_date = datetime.strptime(county['date'], "%Y-%m-%d")

        if this_fip in curr_keys and this_date > counties_covid_recent[this_fip]['date']:
            counties_covid_recent[this_fip] = {'date':this_date, 'cases':this_cases, 'deaths':this_deaths}
        elif this_fip not in curr_keys:
            counties_covid_recent[this_fip] = {'date':this_date, 'cases':this_cases, 'deaths':this_deaths}

    for county_poly in counties_coords["features"]:
        for covid_key, covid_value in counties_covid_recent.items():
            if county_poly['properties']['FIPS']==covid_key:
                county_poly['properties']['cases']=covid_value['cases']
                county_poly['properties']['deaths']=covid_value['deaths']
                break
                
    return counties_coords


def get_states():
    """
    get recent data from covidtracking.com
    """

    covid_tracking = rq.get("https://covidtracking.com/api/v1/states/current.json").json()
    states_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_experiment", "states_coords.csv")
    state_poly = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_experiment", "state_poly.json")

    with open(states_csv, "r") as f:
        csv_file = csv.reader(f, delimiter=",")
        csv_unpacked = [row for row in csv_file]
        states_coords = [{csv_unpacked[0][i]: row[i] for i in range(len(row))} for row in csv_unpacked]

    with open(state_poly, "r") as f:
        jf=json.load(f)

    for covid_row in covid_tracking:
        for coords_row in states_coords:
            if covid_row['state']==coords_row['state']:
                covid_row['name']=coords_row['name']
                # covid_row['dateModified'] = parse(covid_row['dateModified']).strftime('%Y-%m-%d %H:%M:%S')
                # covid_row['dateChecked'] = parse(covid_row['dateChecked']).strftime('%Y-%m-%d %H:%M:%S')
    
    for state_poly in jf['features']:
        for state_covid in covid_tracking:
            if state_poly['properties']['STATE']==state_covid['fips']:
                state_poly['properties']['positive'] = state_covid['positive']
                break

    return jf

