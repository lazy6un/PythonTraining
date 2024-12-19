import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyser=SentimentIntensityAnalyzer()

while True :
    next_message=input('Message: ')
    scores=analyser.polarity_scores(next_message)
    compound=scores['compound']
    if compound > 0.1:
        print('Positive comment')
    elif compound < -0.1:
        print('Negative comment')
    else :
        print('Neutral comment')

