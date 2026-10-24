from flask import Flask
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import json
import os
app = Flask("Sentiment Analyzer")

# Use the bundled VADER lexicon when the service runs on a cloud platform.
nltk.data.path.append(os.path.dirname(__file__))
sia = SentimentIntensityAnalyzer()


@app.get('/')
def home():
    return "Welcome to the Sentiment Analyzer. \
    Use /analyze/text to get the sentiment"


@app.get('/analyze/<input_txt>')
def analyze_sentiment(input_txt):

    scores = sia.polarity_scores(input_txt)
    print(scores)
    pos = float(scores['pos'])
    neg = float(scores['neg'])
    neu = float(scores['neu'])
    res = "positive"
    print("pos neg nue ", pos, neg, neu)
    if (neg > pos and neg > neu):
        res = "negative"
    elif (neu > neg and neu > pos):
        res = "neutral"
    res = json.dumps({"sentiment": res})
    print(res)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5050")), debug=False)
