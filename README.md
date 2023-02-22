# WebScrapingUsingSelenium
Scraping the details of an app from Google Playstore
This Python script uses Selenium to scrape app details from Google Play Store.<br>
It takes input via Google Sheets and outputs a CSV file containing app name, country, language, title, description, average rating, and total ratings.

<h2>Setup</h2>
Install Python 3.x <br>
Install the required packages using pip. <br>
Download and install ChromeDriver for your version of Chrome. <br>

<h2>Usage</h2>
Create a Google Sheet with the following columns: <br>

1. App Name <br>
2. Country <br>
3. Language

Fill in the sheet with the details of the apps you want to scrape. <br>
 
Update the config.json file with your Google API credentials and the sheet ID. <br>

Run the script. <br>

This will generate a CSV file with the app details in the same directory.

<h2>Notes</h2>
&nbsp;&nbsp; 1. This script uses Selenium to scrape data from Google Play Store.
&nbsp;&nbsp;&nbsp;Therefore, it requires an internet connection and may take some time to run depending on the number of apps being scraped.<br>

2. If the app details cannot be found, the corresponding fields in the CSV file will be left blank.<br>

3. The CSV file will be overwritten each time the script is run.<br>


