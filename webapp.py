from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    skyscrapers = get_skyscrapers()
    return render_template('index.html', skyscrapers=skyscrapers)


@app.route('/showFact')
def render_fact():
    skyscrapers = get_skyscrapers()
    skyscraper = request.args.get('skyscraper')
    year = skyscraper_built_in(skyscraper)
    fact = skyscraper + " was built in the year " + year + "."
    return render_template('index.html', skyscraperss=skyscrapers, funFact=fact)
    
    
def get_skyscrapers():
    """Return a list of state abbreviations from the demographic data."""
with open('skyscrapers.json') as skyscrapers_data:
    years = json.load(skyscrapers_data)
    #states=[]
    #for c in counties:
        #if c["State"] not in states:
            #states.append(c["State"])
    #a more concise but less flexible and less easy to read version is below.
    skyscrapers=list(set([y["Skyscraper"] for y in years])) #sets do not allow duplicates and the set function is optimized for removing duplicates
    return skyscrapers


def skyscraper_built_in(skyscraper):
    """Return the name of a county in the given state with the highest percent of under 18 year olds."""
with open('skyscrapers.json') as skyscrapers_data:
 years = json.load(skyscrapers_data)
 year = ""
 year = y["Year"]
 return year
    
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=False) # change to False when running in productio