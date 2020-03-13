# DESCRIPTION
Extracting data from an active website(webscraping) using Chrome Developer Tools to identify the HTML and CSS components attached to the data. Will also using a Python script that uses Beautiful Soup and Splinter to automate browser and gather the data identified. 
Splinter automates the web browser that navigates other websites on its own, and Beautiful Soup extracts the data. 
The data is then stored in a JSON data structure using MongoDB (a NoSQL Database).
Finally, build a web application using flask, which executes our scraping code and help update newest data on page.

### SITUATION/TASK
Automate a web browser that visits other different sites to extract data for analysis. In this task, extract data about the Mission to Mars from all over the web and store in a MongoDB database, and then render the data in a web application created with Flask.

### APPROACH
Before scraping the data, first understand how webpages are built. Next, write a Python script that can navigate the web for the correct data. Once the data is collected, a MongoDB is used to store the information. Here is why, MongoDB, a NOSQL document database allows web scraped data, which comes in different forms like paragraphs and images, and are neither neat or tidy, to be easily stored. Finally, to put it all together in a web application, utilize Flask a web framework that allows her to create a web application using Python and then customize it with HTML and CSS.


### RESULTS


### THINGS LEARNED
* Using HTML elements, as well as class and id attributes, to identify content for web scraping.
* Using BeautifulSoup and Splinter to automate a web browser and perform a web scrape.
* Storing data from web scraping in MongoDB database.
* Creating a web application with Flask to display the data from the web scrape.

### SOFTWARE/TOOLS
CSS, HTML, Python, JavaScript, BeautifulSoup, Splinter, MongoDB, Flask

### LIVE DEMO

