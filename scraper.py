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

    # datetime to string (param type string/datetime okay)
    def __dateToStr(self, date, s_format='%Y-%m-%d'):
        if type(date) is datetime:
            return datetime.strptime(date, s_format).date()  
        else:
            return date

    # string to datetime (param type string/datetime okay)
    def __strToDate(self, date, s_format='%Y/%m/%d'):        
        if type(date) is not datetime:
            return date.strftime(s_format)            
        else:
            return date
            
    # update _from _to dates of class, returns Success/Fail 
    def update_dates(self, s_date, e_date):       
        if self.__check_dates(s_date, e_date) is True:
            self._from = self.__strToDate(s_date)
            self._to = self.__strToDate(e_date)
            return True
        else:
            return False
            

    def search(self, query, _from=None, _to=None):
        if _from is not None and _to is not None:   
            self.update_dates(_from, _to)          
            
            s_str = self.__dateToStr(self._from)
            e_str = self.__dateToStr(self._to)   
            
            self.cur_search = self.news.search(query, from_=s_str, to_=e_str)

        else:
            self.cur_search = self.news.search(query)
            

        
    



  