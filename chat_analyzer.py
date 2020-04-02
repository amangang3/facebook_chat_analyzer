from bs4 import BeautifulSoup


def read_dates(filename):
    with open(filename,'rb') as fp:
        soup = BeautifulSoup(fp,'lxml')
        dates_finder = soup.findAll("div",{'class':'_3-94 _2lem'})
        dates = []
        for element in dates_finder:
            element = element.text.strip().encode('utf-8')
            print(element)
            dates.append(element)
read_dates("message_18.html")
