from bs4 import BeautifulSoup
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib
import numpy as np 
from collections import Counter

def read_dates(filename):
    """
    Function below will take a HTML file and parse the dates into a list of datetime objects
    """
    with open(filename,'rb') as fp:
        soup = BeautifulSoup(fp,'lxml')
        dates_finder = soup.findAll("div",{'class':'_3-94 _2lem'})
        dates = []
        datetime_object = []
        for element in dates_finder:
            element = element.text.strip().encode('utf-8')
            element = element.decode('utf-8').splitlines()
            dates.append(element)
        #flatten dates list 
        dates = [item for items in dates for item in items]
        #generate the datetime object
        for index, value in enumerate(dates):
            datetime_object.append(datetime.strptime(dates[index], '%b %d, %Y, %I:%M %p'))
        return datetime_object

def remove_times(dates):
    date_no_time = []
    for index, value in enumerate(dates):
        date_no_time.append(dates[index].date())
    return date_no_time


dates = read_dates("message_18.html")
only_dates = remove_times(dates)
frequency = dict(Counter(only_dates))
values = []
unique_dates = []
for key in frequency.keys():
    values.append(frequency[key])
    unique_dates.append(key)
#figure out how to count the number of times per day 
















# values = range(len(dates))








#code to plot once you figure out values statement
dates = matplotlib.dates.date2num(only_dates)
# plt.plot_date(unique_dates, values, 'x', markersize=5)
plt.bar(unique_dates, values)
plt.show()