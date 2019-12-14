# Import Dependency Tools
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping_Challenge

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
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars_info =  mongo.db.mars_data.find_one()
   return render_template("index1.html", mars_info = mars_info)



@app.route("/scrape")                   # route flask will be using
def scrape_hem():
   mars_info = mongo.db.mars_data
   mars_data = scraping_Challenge.scrape_all()
   mars_info.update({},mars_data, upsert=True)
   #return render_template("index_Challenge.html", hemispheres=hemispheres)
   return "Successful"

@app.route("/hemispheres")
def hemispheres():
   mars_info = mongo.db.mars_data.find_one()
   return render_template("index_Challenge.html", mars_info = mars_info)



# Tell flask to run
if __name__ == "__main__":
   app.run(debug= True)