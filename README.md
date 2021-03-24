# covid-wellness-bot
A web bot that fills out a daily survey reporting your Covid-19 infection status. 

This bot uses the library [splinter](https://splinter.readthedocs.io/en/latest/) for the web automation. It is primarily built on top of Selenium, and seems easier to use for more basic tasks while still being just as capable.

This bot is entirely specific to a survey that was, at one point in time, required for my place of employment. Although it could likely be adapted to a similar type of survey if desired.

Although I may have saved a few hours of time over the span this bot was used, its main benefit was not missing any days of filling out the required survey, thanks to automation. 

## Usage

It's recommended that you create a new python environment for the bot using your manager of choice (conda, pip, etc.) and install the necessary dependencies defined in *Requirements.txt*. The packages needed are *schedule* and *spliter*, the others should be included in the default python installation.

You will also need Google Chrome installed, along with the corresponding web driver for your version, which can be found [here](https://chromedriver.chromium.org/downloads). The Chrome web driver must be installed in the expected location, refer to [the docs](https://chromedriver.chromium.org/downloads) about how to install it. On linux, this will either be /usr/local/bin or /opt/google/chrome.

**settings.ini**

There are two settings that you can change in the settings.ini file. The link to the survey and the time at which you want the script to run.

Assuming the environment and settings file are configured correctly, all you should need to do is run the **wellness-bot.py** from a terminal that is using your environment.
