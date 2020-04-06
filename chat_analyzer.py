from bs4 import BeautifulSoup
import datetime

def read_dates(filename):
    """
    Function below will take a HTML file and parse the dates into a list of lists. 
    """
    with open(filename,'rb') as fp:
        soup = BeautifulSoup(fp,'lxml')
        dates_finder = soup.findAll("div",{'class':'_3-94 _2lem'})
        list_dates = []
        dates = []
        for element in dates_finder:
            element = element.text.strip().encode('utf-8')
            element = element.decode('utf-8').splitlines()
            list_dates.append(element)
        for index, value in enumerate(list_dates):
            dates.append(list_dates[index][0].split(","))
        return dates

















dates = read_dates("message_18.html")

