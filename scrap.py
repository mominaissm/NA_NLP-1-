import time
from typing import Dict
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import cfg
connection_time = 0
special_char = []

class Scrapper:
    def __init__(self, keyword: str, header: Dict = cfg.browser_header, news_cfg: Dict = cfg.NEWSPAPER,
                 article_length: int = cfg.ARTICLE_LENGTH):
        self.key = keyword
        self.headers = header
        self.news_cfg = news_cfg
        self.article_length = article_length

    def scrap_articles(self, news: str):
        result = requests.get(self.news_cfg.get(news).get("url"), headers=self.headers)
        doc = BeautifulSoup(result.text, "html.parser")
        if self.news_cfg.get(news).get("html_links").get("class"):
            html_links = doc.find_all(self.news_cfg.get(news).get("html_links").get("h"),
                                      class_=self.news_cfg.get(news).get("html_links").get("class"))
        else:
            html_links = doc.find_all(self.news_cfg.get(news).get("html_links").get("h"))

        # EXTRACTING ONLY THE URL FROM THE HTML TAGS.
        urls = list()
        for link in html_links:
            if news == "dawn" or news == "india_today" or news == "the_quint":
                urls.append(link['href'])
            else:
                if link.a:
                    each_article = link.a.get('href')
                    if len(str(each_article)) > self.article_length:
                        urls.append(f'{self.news_cfg.get(news).get("pre_url")}{each_article}')


        # GOING THROUGH EACH OF THOSE URLS EXTRACTED
        all_content = list()
        for url in urls[:15]:
            current_article = dict()
            article = requests.get(url, headers=self.headers)
            document = BeautifulSoup(article.text, "html.parser")

            # SEARCHING FOR THE KEYWORD
            if document.find(self.news_cfg.get(news).get("main").get("div"),
                             class_=self.news_cfg.get(news).get("main").get("identifier")):
                main_story = document(self.news_cfg.get(news).get("main").get("div"),
                                      class_=self.news_cfg.get(news).get("main").get("identifier"))
            elif document.find(self.news_cfg.get(news).get("main").get("div"),
                               id=self.news_cfg.get(news).get("main").get("identifier")):
                main_story = document.find(self.news_cfg.get(news).get("main").get("div"),
                                           id=self.news_cfg.get(news).get("main").get("identifier"))
            else:
                main_story = document.find(self.news_cfg.get(news).get("main").get("div"),
                                           itemprop=self.news_cfg.get(news).get("main").get("identifier"))

            if main_story and any([self.key in i.text for i in main_story if not isinstance(i, str)]):
                if self.news_cfg.get(news).get("heading").get("class"):
                    current_article["heading"] = document.find(self.news_cfg.get(news).get("heading").get("h1"),
                                                           class_=self.news_cfg.get(news).get("heading").
                                                           get("class")).text
                else:
                    current_article["heading"] = document.find(self.news_cfg.get(news).get("heading").get("h1")).text

                # IMAGES
                if news == "indian_express" and self.news_cfg.get(news).get("media").get("class"):
                    media = document.find_all(self.news_cfg.get(news).get("media").get("img_tag"),
                                              class_=self.news_cfg.get(news).get("media").get("class"))

                if news == "dawn" and self.news_cfg.get(news).get("media").get("class"):
                    media = document.find(self.news_cfg.get(news).get("media").get("img_tag"),
                                          class_=self.news_cfg.get(news).get("media").get("class"))

                elif self.news_cfg.get(news).get("media").get("class"):
                    media = document.find_all(self.news_cfg.get(news).get("media").get("img_tag"),
                                              class_=self.news_cfg.get(news).get("media").get("class"))
                else:
                    media = document.find_all(self.news_cfg.get(news).get("media").get("img_tag"))

                if media:
                    if news == "al_jazeera":
                        images = [f'{self.news_cfg.get(news).get("img_url")}{pic.img.get("src")}' for pic in media
                                  if pic.img]

                    elif news == "indian_express":
                        images = [pic.img.get("data-lazy-src") for pic in media if pic.img]

                    else:
                        images = [pic.img.get("src") for pic in media if pic.img]
                    current_article["image"] = images

                # if news == 'dawn' or news == "indian_express" or news == "times_of_india":
                current_article["content"] = "".join(each.text for each in main_story)
                # else:
                #     current_article["content"] = " ".join([each.text for each in main_story.find_all('p')])

            if current_article:
                all_content.append(current_article)

        return all_content

    def scrap_all_sites(self):
        articles = dict()
        for key, value in tqdm(self.news_cfg.items()):
            try:
                articles[key] = self.scrap_articles(key)

            except ConnectionError or ConnectionResetError or ConnectionRefusedError:
                continue
            except AttributeError:
                print(f"There was an attribute error with {key}.")

        return articles

