# Import Dependency Tools
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# Set up flask
app = Flask(__name__)

############################################## This commented out block is for the module ########################
# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

# Set Up Flask App Routes
# (1.for the main HTML page everyone will visit   2.for scraping new data using the code we’ve written. )

# Define the route for the HTML page
# @app.route("/")
# def index():
#    mars = mongo.db.mars.find_one()
#    return render_template("index.html", mars=mars)

# Set up our scraping route.
#  It create's a "button" of the web app that will run the code, to scrape for updated data, when clicked
# @app.route("/scrape")                   # route flask will be using
# def scrape():
#    mars = mongo.db.mars
#    mars_data = scraping.scrape_all()
#    mars.update({}, mars_data, upsert=True)
#    return "Scraping Successful!"


###################################### Challenge #########################################
app.config["MONGO_URI"] = "mongodb://localhost:27017/hem_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   hem =  mongo.db.hem.find_one()
   return render_template("index.html", hem=hem)


@app.route("/scrape")                   # route flask will be using
def scrape_hem():
   hem = mongo.db.hem
   hem_data = scraping.scrape_all()
   hem.update({},hem_data, upsert=True)
   return "Scraping Complete!"

# Tell flask to run
if __name__ == "__main__":
   app.run()