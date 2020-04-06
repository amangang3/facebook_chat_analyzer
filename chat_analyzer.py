from bs4 import BeautifulSoup
from datetime import datetime

def read_dates(filename):
    """
    Function below will take a HTML file and parse the dates into a list of lists. 
    """
    with open(filename,'rb') as fp:
        soup = BeautifulSoup(fp,'lxml')
        dates_finder = soup.findAll("div",{'class':'_3-94 _2lem'})
        dates = []
        for element in dates_finder:
            element = element.text.strip().encode('utf-8')
            element = element.decode('utf-8').splitlines()
            dates.append(element)
        #flatten dates list 
        dates = [item for items in dates for item in items]
        return dates

#def gen_datetime_object(dates):
    


dates = read_dates("message_18.html")
print(dates[0])
datetime_object = datetime.strptime(dates[0], '%b %d, %Y, %I:%M %p')
print(datetime_object)
