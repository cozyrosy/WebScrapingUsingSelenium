from googleapiclient.discovery import build
from google.oauth2 import service_account
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1toIOJu4EQr1XWzOw2-3hwRi_2ZpQPzaOakKw9Z2T8f0'  

# SAMPLE_RANGE_NAME = 'Class Sheet1!A1:C2'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API   
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1").execute()
values = result.get('values', [])

# Converting the list of values to a dictionary.
data = {}
headers = values[0]
for row in values[1:]:
        row_data = dict(zip(headers,row))
        

# A function to scrape the webpage.
def scrape_app_details(app_name, country, language):
    url = f"https://play.google.com/store/apps/details?id={app_name}&gl={country}&hl={language}"
    driver = webdriver.Chrome()
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    try:
        title = soup.find("h1", class_="Fd93Bb ynrBgc xwcR9d")
        title = title.text

        description = soup.find("div", class_="SfzRHd ")
        # description = description.text
        
        avg_rating = soup.find("div", class_="jILTFe")
        avg_rating = avg_rating.text

        total_ratings = soup.find("div", class_="EHUI5b")
        total_ratings = total_ratings.text

        final_data = {"Title":title, "Description": description, "Average Ratings":avg_rating, "Total Ratings": total_ratings}
        print(final_data)

        # open a csv file in write mode
        with open('scraped_data.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)

                # write the header row
                writer.writerow(['Title', 'Description', 'Average Ratings' , 'Total Ratings'])
                
                # write the data rows
                writer.writerow([final_data['Title'], final_data['Description'], final_data['Average Ratings'], final_data['Total Ratings']])
        
    except AttributeError:
        print("description:- ")
    driver.quit()

app_details = scrape_app_details(app_name = row_data['name'], country = row_data['country'], language = row_data['language'])

#"https://appvector.io/aso-tool/23/reviews" #"https://appvector.io/aso-tool/api/reviews/?appId=23&page=23" #"https://appvector.io/aso-tool/23/reviews/?appId=23&page=78323" #"https://play.google.com/store/apps/details?id=com.whatsapp&reviewId=e592136e-3434-4475-9cd4-5b967b7fd700"