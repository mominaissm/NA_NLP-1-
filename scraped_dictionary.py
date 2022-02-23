from scrap import Scrapper
from SummaryModel import SummaryClass
from SentimentModel import SentimentClass
obj_scrap = Scrapper("Kashmir")
#obj_summary = SummaryClass()
obj_Sentiment = SentimentClass()

class SummaryModelApplication(Scrapper,SummaryClass):
        
    def NewsDict(self,news: str):
        nested_dict = obj_scrap.scrap_all_sites()
        dictionary = nested_dict.get(news)  #returrns a dictionary that contains news from a specific (defined) site
        loop_var = len(dictionary)
        for i in range (loop_var):
            #creating a temp dictionary that takes the value of dict[i]
            temp_dict = dictionary[i]
            obj_SummaryClass = SummaryClass()
            sum = obj_SummaryClass.sum_ext(temp_dict['content'])
            temp_dict['content']  = sum
            obj_Sentiment.sentiment_analysis(sum)
            temp_dict['sentiment'] = obj_Sentiment.value_to_mood() 
            nested_dict.update(temp_dict)
        return nested_dict

