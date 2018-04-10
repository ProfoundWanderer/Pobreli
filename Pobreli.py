#!/usr/bin/python3.6


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime as dt
import os
import smtplib


# Gets the full day (ie Wednesday instead of Wed)
day = time.strftime('%A')
# Gets the current date and time and formats it
time = dt.now().strftime('%B %d, %Y at %I:%M %p')
now = (day + ", " + time)


# Running firefox headless will make program run slow so you may want to remove this section
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options)

current_conditions_url = 'https://weather.com/weather/today/l/Dallas+TX+75230:4:US'
browser.get(current_conditions_url)
current_conditions = browser.find_element_by_id('dp0-details-narrative').text
current = f"Current Weather Conditions as of {now}: {current_conditions}"


# add date and time  above ^ then add date below
weather_url = 'https://weather.com/weather/today/l/Dallas+TX+75230:4:US'
browser.get(weather_url)
next_day = browser.find_element_by_id('daypart-1')
next_day.click()
weather = browser.find_element_by_id('dp1-details-narrative').text
tomorrow = f"Tomorrows Weather: {weather}"


pollen_url = 'https://www.pollen.com/forecast/current/pollen/75230'
browser.get(pollen_url)
pollen = browser.find_element_by_css_selector('div.forecast-day:nth-child(3) > div:nth-child(1) > div:nth-child(1) > '
                                              'div:nth-child(3) > p:nth-child(5)').text
pollen_level = f"Pollen Level: {pollen.title()}"


asthma_url = 'http://www.asthmaforecast.com/Asthma-Forecast.aspx?zip=75230'
browser.get(asthma_url)
asthma = browser.find_element_by_xpath('//*[@id="ctl00_mainBody_imgLevel"]').get_attribute('alt')
air = browser.find_element_by_css_selector('#ctl00_mainBody_AirQualityToday').text
asthma_level = f"The asthma level is {asthma} and the air quality is {air.lower()}."

conditions = (current + "\n" + tomorrow + "\n" + pollen_level + "\n" + asthma_level)


# Below code needs to just be updated to send text and/or email with information from above
from_addr = os.environ.get('from_addr')
to_addr = os.environ.get('to_addr')
password = os.environ.get('password')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(from_addr, password)
body = conditions
server.sendmail(from_addr, to_addr, body)


browser.quit()
server.quit()

