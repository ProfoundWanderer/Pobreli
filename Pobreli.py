#!/usr/bin/python3.6

# http://selenium-python.readthedocs.io/locating-elements.html


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime as dt


"""DONE
# Print the day and date (ie Tuesday, April 3, 2018)
# Gets the full day (ie Wednesday instead of Wed)
day = time.strftime('%A')
# Gets the current date and time and formats it
time = dt.now().strftime('%B %d, %Y at %I:%M %p')
print(day + ",", time)
"""


options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options)

"""DONE
# Get weather narrative
weather_url = 'https://weather.com/weather/today/l/Dallas+TX+75230:4:US'
browser.get(weather_url)
weather = browser.find_element_by_id('dp0-details-narrative').text
print(weather)
"""


# Get pollen count and say it is out of 12
# https://www.pollen.com/forecast/current/pollen/75230
pollen_url = ['https://www.pollen.com/forecast/current/pollen/75230']
browser.get(pollen_url)


"""
# Get asthma level and say it is out of 12
asthma_url = ['http://www.asthmaforecast.com/Asthma-Forecast.aspx?zip=75230']
browser.get(asthma_url)
"""


# Maybe add flu and cold forecast in the future


browser.quit()
