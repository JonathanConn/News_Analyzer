import nltk
from textblob import TextBlob


class NLP():

  # def __init__(self):


  # returns tuple (positve, negative) count in str_list
  def run_analysis(self, str_list): 

    feedbacks = str_list
    positive_feedbacks = []
    negative_feedbacks = []

    # polarity -1 < i < 1 indicates negative emotions
    # subjectivity -1 < j < 1 indicates positive emotions 
    for feedback in feedbacks:
      feedback_polarity = TextBlob(feedback).sentiment.polarity
    
      if feedback_polarity > 0:
        positive_feedbacks.append(feedback)
        continue
    
      negative_feedbacks.append(feedback)

    return (len(positive_feedbacks), len(negative_feedbacks))

    # print('Positive_feebacks Count : {}'.format(len(positive_feedbacks)))
    # print(positive_feedbacks)
    # print('Negative_feedback Count : {}'.format(len(negative_feedbacks)))
    # print(negative_feedbacks)
