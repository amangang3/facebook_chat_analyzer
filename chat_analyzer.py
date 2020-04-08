from bs4 import BeautifulSoup
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib
import numpy as np 
from collections import Counter

def read_dates():
    """
    Function below will take a folder of HTML files and return the dates information
    """
    import os
    path = r"G:\Google Drive\Personal project\Chat log analyser\Fania"
    dates = []
    for filename in os.listdir(path):
        if filename.endswith(".html"):
            fullpath = os.path.join(path, filename)
            # Get single page and make soup
            soup = BeautifulSoup(open(fullpath, encoding='utf-8'), 'lxml')
            dates_finder = soup.findAll("div",{'class':'_3-94 _2lem'})
            for element in dates_finder:
                element = element.text.strip().encode('utf-8')
                element = element.decode('utf-8').splitlines()
                dates.append(element)
    return dates


def flatten_and_generate_datetime_object(dates):
    #flatten dates list 
    dates = [item for items in dates for item in items]
    #generate the datetime object
    datetime_object = []
    for index, value in enumerate(dates):
        datetime_object.append(datetime.strptime(dates[index], '%b %d, %Y, %I:%M %p'))
    return datetime_object

def remove_times(dates):
    date_no_time = []
    for index, value in enumerate(dates):
        date_no_time.append(dates[index].date())
    return date_no_time

def frequency_plot(only_dates):
    frequency = dict(Counter(only_dates))
    values = []
    unique_dates = []
    for key in frequency.keys():
        values.append(frequency[key])
        unique_dates.append(key)
    plt.bar(unique_dates, values)
    plt.show()


dates = read_dates()
dates = flatten_and_generate_datetime_object(dates)
only_dates = remove_times(dates)
frequency_plot(only_dates)