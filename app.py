from SummaryModel import SummaryClass
from SentimentModel import SentimentClass
from scrap import Scrapper
from scraped_dictionary import SummaryModelApplication
from flask import Flask
from flask_mysqldb import MySQL
import json as js
    
obj_scrap = Scrapper("Kashmir")
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mypassword'
app.config['MYSQL_DB'] = 'NA_NLP'
mysql = MySQL(app)
obj_SummaryModelApplication = SummaryModelApplication(obj_scrap)
#making dictionaries of every news site
al_jazeera = obj_SummaryModelApplication.NewsDict("al_jazeera")
indian_express = obj_SummaryModelApplication.NewsDict("indian_express")
hindustan_times = obj_SummaryModelApplication.NewsDict("hindustan_times")
dawn = obj_SummaryModelApplication.NewsDict("dawn")
ndtv = obj_SummaryModelApplication.NewsDict("ndtv")
times_of_india = obj_SummaryModelApplication.NewsDict("times_of_india")
ap_news = obj_SummaryModelApplication.NewsDict("ap_news")
the_quint = obj_SummaryModelApplication.NewsDict("the_quint")
vice = obj_SummaryModelApplication.NewsDict("vice")
free_press_journal = obj_SummaryModelApplication.NewsDict("free_press_journal")
#Traversing through each dictionary to store data in db
loop_var = len(al_jazeera)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('al_jazeera', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(indian_express)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('indian_express', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(hindustan_times)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('hindustan_times', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(dawn)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('dawn', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(ndtv)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('ndtv', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(ap_news)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('ap_news', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(the_quint)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('the_quint', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(vice)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('vice', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close() 
      
loop_var = len(free_press_journal)
for i in range (loop_var):
   temp_dict = al_jazeera[i]
   cur = mysql.connection.cursor()  
   heading = temp_dict['heading']
   image = temp_dict['image']
   content = temp_dict['content']
   sentiment = temp_dict['sentiment']
   queryStr=f"INSERT INTO News (site, heading, image, content, sentiment) VALUES ('free_press_journal', '{heading}', '{image}', '{content}', '{sentiment}') "
   cur.execute(queryStr)
   mysql.connection.commit()
   cur.close()
   
@app.route("/", methods=['GET'])
def main():
   cur = mysql.connection.cursor() 
   cur.execute("SELECT * FROM News")
   results = cur.fetchall()
   cur.close()   
   return js.dump({"News Vendor": results})

@app.route("/negative", methods=['GET'])
def negative():
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM News WHERE sentiment = 'negative' || 'very negative' " )
   results = cur.fetchall()
   cur.close()   
   return js.dump({"Negative sentiment articles": results})

@app.route("/positive", methods=['GET'])
def negative():
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM News WHERE sentiment = 'positive' || 'very positive' || 'neutral' " )
   results = cur.fetchall()
   cur.close()   
   return js.dump({"Positive sentiment articles": results})
   
if __name__ == "__main__":
   app.run(debug=True)