#!/usr/bin/env python
import configparser
import schedule
import time

from splinter import Browser

# read values from settings file
config = configparser.ConfigParser()
config.read('settings.ini')

# change these values in 'settings.ini', not here
SURVEY_LINK = config.get('settings', 'SURVEY_LINK')
TIME_TO_RUN = config.get('settings', 'TIME_TO_RUN')


def fill():
    """The routine that the bot follows to fill out the survey."""
    web = Browser('chrome')
    web.visit(SURVEY_LINK)

    # wait for page to load and click next
    time.sleep(2)
    web.find_by_text('Next').click()

    # wait for page to load and consent
    time.sleep(2)
    web.find_by_text('I agree and consent').click()
    web.find_by_text('Next').click()

    # wait for page to load and fill in 'No' for every option
    time.sleep(2)
    web.find_by_text('No')[0].click()
    web.find_by_text('No')[1].click()
    web.find_by_text('No')[2].click()
    web.find_by_text('No')[3].click()
    time.sleep(3)
    web.find_by_text('Next').click()

    # check for text indicating that 'No' was properly entered
    # on previous page and click 'OK'
    if web.find_by_text('Based on your response, you may return on-site.'):
        web.find_by_text('OK').click()
    else:
        web.quit()

    time.sleep(2)

    # final submission of form
    web.find_by_text('Next').click()

    # wait for submission to complete before exiting
    time.sleep(7)
    web.quit()


# change the time in 'settings.ini'
schedule.every().day.at(TIME_TO_RUN).do(fill)

while True:
    schedule.run_pending()
    time.sleep(5)
