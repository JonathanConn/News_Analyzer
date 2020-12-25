from GoogleNews import GoogleNews

class News():

    def __init__(self):
        self.news = GoogleNews()    

        # set news to default    
        self.news.set_lang('en')
        self.news.set_period('7d')
        self.news.set_time_range('1/01/2020','1/02/2020')
        self.news.set_encode('utf-8')

    def update_dates(self, s_date, e_date):
        if s_date < e_date:

            new_s = s_date.strftime('%m/%d/%Y')
            new_e = e_date.strftime('%m/%d/%Y')

            self.news.set_time_range(new_s, new_e)
            return True
        
        else:
            return False

    def get_news(self, query):
        self.news.get_news(query)
        self.news.search(query)
        
        return self.news.get_texts()
        
        # headlines = googlenews.get_texts()


    