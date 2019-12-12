
#################################################### Article Scraping
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page. Telling our browser to wait a second before searching for components:
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Set up the HTML parser
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# Scraping : assign the title and summary text to variables we’ll reference later.
# In other words, identify the parent element and create a variable to hold it
slide_elem.find("div", class_='content_title')

# Search within the element for the title.And stripe the additional HTML attributes and tags with the use of .get_text().
## Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Next add the summary text. Use the unique class associated with the summary ie “article_teaser_body.”
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


################################################### Image Scraping
# Set up the URL to visit the site
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button, Use the id in our code
full_image_elem = browser.find_by_id('full_image')      # the browser frinds an element with its id and hplds it in a var
full_image_elem.click()                                 # splinter will "click" the image to view its full size


# Use Splinter’s functionality ability to find elements using text.
# Find the "more info" button using only text and "click" that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()

# Scrape the full-size image URL. Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Tags used to find the most recent image :  <figure /> and <a /> tags have the image link nested within them.
# Use (<figure />, <a />, and <img />) to build the URL to the full-size image.  Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Add the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# Scraping an entire table with Pandas’ .read_html() function.
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# Adding the DataFrame to a web application
# Using Pandas convert DataFrame back into HTML-ready code using the .to_html()
df.to_html()


# Deactivating/Turning Off the automated browser session
browser.quit()