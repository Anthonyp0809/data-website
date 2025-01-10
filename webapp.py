from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)


@app.route('/')
def home():
    years1 = get_years()
    return render_template('index.html', years=years1)


@app.route('/showFact')
def render_fact():
    years = get_years()
    year = request.args.get('yearDropdown')
    skyscraper = skyscraper_built_in(year)
    fact = str(skyscraper) + " was built in the year " + str(year) + "."
    return render_template('index.html', years=years, funFact=fact)

@app.route('/decades')
def render_decades():
    decades = get_building_decade_count()
    graph_points = format_dict_as_graph_points(decades)
    return render_template('decades.html', points=graph_points)
    
def get_building_decade_count():
    """return a dictionary with format 
    {"1850's":1...}"""
    years = get_years()
    decade_count = {}
    for year in years:
        decade = str (year)[:-1]  + "0's"
        if decade in decade_count:
            decade_count [decade] += 1
        else:
            decade_count [decade] = 1
    return decade_count
    
def format_dict_as_graph_points(data):
    graph_points = ""
    for key in data:
        graph_points += Markup('{y: ' + str(data[key]) + ', label: "' + key + '"}, ')
    graph_points = graph_points[:-2]
    print(graph_points)
    return graph_points
    
def get_years():
    """Return a list of state abbreviations from the demographic data."""
    with open('skyscrapers.json') as skyscrapers_data:
        buildings = json.load(skyscrapers_data)
    years=[]
    for building in buildings:
        year = building["status"]["completed"]["year"]
        if year != 0:
            years.append(year)
    #a more concise but less flexible and less easy to read version is below.
    # skyscrapers=list(set([y["Skyscraper"] for y in years])) #sets do not allow duplicates and the set function is optimized for removing duplicates
    years.sort()
    return years

def get_years_set():
    return list(set(get_years()))

def skyscraper_built_in(inputYear):
    """Return the name of a county in the given state with the highest percent of under 18 year olds."""
    with open('skyscrapers.json') as skyscrapers_data:
        buildings = json.load(skyscrapers_data)
    
    
    for building in buildings:
        if int(building["status"]["completed"]["year"]) == int(inputYear):
            return building["name"]
    
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=False) # change to False when running in productio