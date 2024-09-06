from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bot import send_msg
from datetime import datetime
import os
import sys
import schedule
import time
import csv
import codecs
import shutil

app_path = os.path.dirname(sys.executable)
now = datetime.now()
day_month_year = now.strftime("%d%m%Y")

#def filter_new_updates(previous, new, output_file):
    # Load the data from the CSV files
    #previous_updates = pd.read_csv(previous)
    #new_updates = pd.read_csv(new)
    #diff = previous_updates.compare(new_updates)


def filter_new_updates(previous, output_file):
    print("Program Run")
    # Load the data from the CSV files
    previous_updates = pd.read_csv(previous)
    get_newest()
    new_updates = pd.read_csv(previous)

    # Compare the two DataFrames
    diff = new_updates.merge(previous_updates, indicator=True, how='outer').loc[lambda x: x['_merge'] != 'both']

    if not diff.empty:
        # Save the differences to a new CSV file
        diff.to_csv(output_file, index=False)
        send_msg(u"difference.csv")


def get_newest():
    website = 'https://eng.cu.edu.eg/ar/credit-hour-system/'
    path = "D:\Yousef\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"  # introduce path here

    # add headless mode
    options = Options()
    options.headless = True
    options.add_argument("--headless=new")

    driver_service = Service(executable_path=path)
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.get(website)

    containers = driver.find_elements(by='xpath', value='/html/body/div[1]/div/div/div/div')
    titles = []
    subtitles = []
    links = []
    links2 = []
    links3 = []
    links4 = []
    images = []

    for container in containers[1:]:
        try:
            title = container.find_element(by='xpath', value='./p/b').text
        except:
            title = container.find_element(by='xpath', value='./p/span/b').text
        subtitle = container.find_element(by='xpath', value='./div/div/p[1]/strong/span').text
        link = container.find_element(by='xpath', value='./div/div/p[2]/strong/a[1]').get_attribute('href')
        try:
            link2 = container.find_element(by='xpath', value='./div/div/p[2]/strong/a[2]').get_attribute('href')
        except:
            link2 = None

        try:
            link3 = container.find_element(by='xpath', value='./div/div/p[2]/strong/a[3]').get_attribute('href')
        except:
            link3 = None

        try:
            link4 = container.find_element(by='xpath', value='./div/div/p[2]/strong/a[4]').get_attribute('href')
        except:
            link4 = None

        try:
            image = container.find_element(by='xpath', value='./p[1]/a/img').get_attribute('src')
        except:
            image = None

        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
        links2.append(link2)
        links3.append(link3)
        links4.append(link4)
        images.append(image)
    driver.quit()
    my_dict = {'title': titles, 'subtitle': subtitles, 'link': links, 'link2': links2, 'link3': links3, 'image': images}
    df_headlines = pd.DataFrame(my_dict)
    file_name = 'previous_announcement.csv'

    #final_path = os.path.join(app_path, file_name) #exe
    #df_headlines.to_csv(final_path, index=False) #exe

    df_headlines.to_csv(file_name, index=False)

def job():
    filter_new_updates("previous_announcement.csv", "difference.csv")

schedule.every(20).seconds.do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)


