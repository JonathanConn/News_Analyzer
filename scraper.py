from pygooglenews import GoogleNews
import enum
from datetime import datetime

class Topics(enum.Enum):
    WORLD = 0 
    NATION = 1
    BUSINESS = 2 
    TECHNOLOGY = 3
    ENTERTAINMENT = 4
    SCIENCE = 5
    SPORTS = 6
    HEALTH = 7

class News():

    def __init__(self):
        self.news = GoogleNews()
        
        self.cur_search = None
        self._from = None
        self._to = None

    

    # check if dates are valid
    def __check_dates(self, s_date, e_date):
        return self.__dateToStr(s_date) < self.__dateToStr(e_date)

    # datetime to string
    def __dateToStr(self, date, format=None):
        if type(date) is datetime:
            return datetime.strptime(date, '%Y-%m-%d').date()  
        return date

    # string to datetime
    def __strToDate(self, date, format=None):        
        if type(date) is not datetime:
            return date.strftime('%Y/%m/%d')            
        return date
            

    def update_dates(self, s_date, e_date):        
        if self.__check_dates(s_date, e_date) is True:
            self._from = self.__strToDate(s_date)
            self._to = self.__strToDate(e_date)
            return True
            
        return False
            

    def search(self, query, _from=None, _to=None):
        if _from is not None and _to is not None:                
            self.cur_search = self.news.search(query)

        else:
            self.cur_search = self.news.search(query)
            

        
    



  