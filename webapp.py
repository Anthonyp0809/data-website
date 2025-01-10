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
    return render_template('decades.html')
def get_years():
    """Return a list of state abbreviations from the demographic data."""
    with open('skyscrapers.json') as skyscrapers_data:
        years = json.load(skyscrapers_data)
    skyscrapers=[]
    for y in years:
        if y["status"]["completed"]["year"] not in skyscrapers:
            skyscrapers.append(y["status"]["completed"]["year"])
    #a more concise but less flexible and less easy to read version is below.
    # skyscrapers=list(set([y["Skyscraper"] for y in years])) #sets do not allow duplicates and the set function is optimized for removing duplicates
    return skyscrapers


def skyscraper_built_in(inputYear):
    """Return the name of a county in the given state with the highest percent of under 18 year olds."""
    with open('skyscrapers.json') as skyscrapers_data:
        years = json.load(skyscrapers_data)
    
    
    for y in years:
        print(y)
        if int(y["status"]["completed"]["year"]) == int(inputYear):
            return y["name"]
    
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=False) # change to False when running in productio