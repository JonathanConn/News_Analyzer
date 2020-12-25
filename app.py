from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for, abort
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
    
    text = text.lower()
    
    try:
        s_date = datetime.strptime(s_str, '%Y-%m-%d').date()  
        e_date = datetime.strptime(e_str, '%Y-%m-%d').date()  

    except ValueError as e:
        app.log_exception(e)
        redirect(url_for('fsailure'))

    if news.update_dates(s_date, e_date) is False:
        app.log_exception('failed news update dates in app.py')
        return render_template('failure_alert.html'), 404      
        
    

    return 'test'
    # found_news = news.get_news(processed_text)
    # pos, neg = nlp.run_analysis(found_news)

    # result  = processed_text + '\tPOS: ' + str(pos) + '\tNEG: ' + str(neg)

    # return result

@app.route('/failure')
def failure():
    return render_template('failure_alert.html')


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app