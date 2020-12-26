from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for, abort, Markup
from flask.logging import default_handler

from scraper import News
from nlp import NLP

news = News()
nlp = NLP()


# create an app instance
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['query']
    s_str = request.form['query_start']
    e_str = request.form['query_end']
    
    processed_text = text.lower()
    
    try:
        s_date = datetime.strptime(s_str, '%Y-%m-%d').date()  
        e_date = datetime.strptime(e_str, '%Y-%m-%d').date()  

    except ValueError as e:
        app.log_exception('failed date conversion' + str(s_str) + ' ' + str(e_str) + '\t' + e)
        redirect(url_for('fsailure'))
    
    if news.update_dates(s_date, e_date) is False:
        app.log_exception('failed news update dates in app.py')
        return render_template('failure_alert.html'), 404      
        
    news.search(processed_text, s_date, e_date)

    headlines = []
    for i in news.cur_search['entries']:
        headlines.append(str(i.title))
    
    pos, neg = nlp.run_analysis(headlines)

    result_headlines = Markup('<br>'.join(headlines))

    return render_template('result.html', query=text, pos=str(pos), neg=str(neg), headlines=result_headlines)

@app.route('/failure')
def failure():
    return render_template('failure_alert.html')


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app