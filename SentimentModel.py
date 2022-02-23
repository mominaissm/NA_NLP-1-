from transformers import pipeline


class SentimentClass:
    
    def __init__(self):
        self.pipeline_var = pipeline(task="text-classification", model='nlptown/bert-base-multilingual-uncased-sentiment')

    def sentiment_analysis(self, seq1):
        
        self.sentiment = str(self.pipeline_var(seq1))
        return self.sentiment

    def value_to_mood(self):
        mood = ''
        one = self.sentiment.find("1 star")
        two = self.sentiment.find("2 star")
        three = self.sentiment.find("3 star")
        four = self.sentiment.find("4 star")
        five = self.sentiment.find("5 star")
        if (one!=-1):
            mood = "very negative"
        if (two!=-1):
            mood = "negative"
        if (three!=-1):
            mood = "neutral"
        if (four!=-1):
            mood = "positive"
        if (five!=-1):
            mood = "very positive"
        return mood
