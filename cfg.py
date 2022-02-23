browser_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/98.0.4758.81 Safari/537.36'
}

NEWSPAPER = {
    "indian_express": {"url": "https://indianexpress.com/page/1/?s=Kashmir", "html_links": {"h": "h3"},
                       "pre_url": "",
                       "main": {"div": "div", "identifier": "pcl-full-content"},
                       "heading": {"h": "h1", "class": "native_story_title"},
                       "media": {"img_tag": "span", "class": "custom-caption"}},

    "hindustan_times": {"url": "https://www.hindustantimes.com/search?q=kashmir",
                        "pre_url": "https://www.hindustantimes.com",
                        "html_links": {"h": "h3", "class": "hdg3"},  # added class in html_links
                        "main": {"div": "div", "identifier": "storyDetails"},
                        "heading": {"h": "h1", "class": "hdg1"},
                        "media": {"img_tag": "picture"}},  # added class to media

    # # "daily_mail": {"url": "https://www.dailymail.co.uk/home/search.html?sel=site&searchPhrase=Kashmir",
    # #                "pre_url": "https://www.dailymail.co.uk",
    # #                "html_links": {"h": "h3", "class": "sch-res-title"},  # added class to html links
    # #                "main": {"div": "div", "identifier": "articleBody"},
    # #                "heading": {"h": "h2"},
    # #                "media": {"img_tag": "div", "class": "cursor: pointer;"}},  # added style to media
    #
    "al_jazeera": {"url": "https://www.aljazeera.com/search/kashmir?sort=relevance",
                   "pre_url": "",
                   "img_url": "https://www.aljazeera.com",
                   "html_links": {"h": "div", "class": "gc__header-wrap"},  # added class to html links
                   "main": {"div": "div", "identifier": "wysiwyg wysiwyg--all-content css-1ck9wyi"},
                   "heading": {"h": "h1"},
                   "media": {"img_tag": "figure", "class": "article-featured-image"}},  # added class

    "dawn": {"url": "https://www.dawn.com/", "html_links": {"h": "a", "class": "story__link"},
             "pre_url": "", # added class to html links
             "main": {"div": "div", "identifier": "story__content overflow-hidden text-4 sm:text-4.5 pt-1 mt-1"},
             "heading": {"h": "h2",
                         "class": "story__title text-7.5 font-bold font-playfair-display mt-1 pb-3 border-b "
                                  "border-gray-300 border-solid"}, # added class
             "media": {"img_tag": "div", "class": "media__item"}},  # added class
    #
    # # "india_today": {"url": "https://www.indiatoday.in/topic/kashmir",
    # #                 "pre_url": "",
    # #                 "html_links": {"h": "a", "class": "_blank"},  # added class to html links
    # #                 "main": {"div": "div", "identifier": "articleBody"},
    # #                 "heading": {"h": "h1", "class": "headline"},  # added class to heading
    # #                 "media": {"img_tag": "div", "class": "stryimg"}},  # added class
    #
    "ndtv": {"url": "https://www.ndtv.com/search?searchtext=kashmir",
             "pre_url": "",
             "html_links": {"h": "div", "class": "src_itm-ttl"},  # added class to html links
             "main": {"div": "div", "identifier": "sp-cn ins_storybody"},
             "heading": {"h": "h1", "class": "sp-ttl"},  # added class to heading
             "media": {"img_tag": "div", "class": "ins_instory_dv_cont"}},  # added class

    "times_of_india": {"url": "https://timesofindia.indiatimes.com/india/jammu-and-kashmir",
                       "pre_url": "https://timesofindia.indiatimes.com",
                       "html_links": {"h": "span", "class": "w_tle"},  # added class to html links
                       "main": {"div": "div", "identifier": "_3YYSt clearfix"},
                       "heading": {"h": "h1", "class": "_1Y-96"},  # added class to heading
                       "media": {"img_tag": "div", "class": "_3gupn"}},  # added class

    "ap_news": {"url": "https://apnews.com/hub/kashmir",
                       "pre_url": "https://apnews.com",
                       "html_links": {"h": "div", "class": "CardHeadline"},  # added class to html links
                       "main": {"div": "div", "identifier": "Article"},
                       "heading": {"h": "h1"},  # added class to heading
                       "media": {"img_tag": "img", "class": "image-0-2-44"}},  # added class

    "the_quint": {"url": "https://www.thequint.com/search?q=kashmir",
                 "pre_url": "",
                 "html_links": {"h": "a", "class": "headline-link"},  # added class to html links
                 "main": {"div": "div", "identifier": "story-body-wrapper"},
                 "heading": {"h": "h1", "class": "ieh5X RXXC0"},  # added class to heading
                 "media": {"img_tag": "picture", "class": "qt-image"}},  # added class

    "vice": {"url": "https://www.vice.com/en/search?q=kashmir",
             "pre_url": "",
             "html_links": {"h": "h3", "class": "vice-card-hed vice-card-hed--light vice-card__vice-card-hed"},
             # added class to html links
             "main": {"div": "div", "identifier": "article__body-components article__body-components--longform"},
             "heading": {"h": "h1", "class": "smart-header__hed smart-header__hed--size-2"},  # added class to heading
             "media": {"img_tag": "picture",
                       "class": "responsive-image responsive-image--loaded lazyloader--loaded"}},  # added class

    "free_press_journal": {"url": "https://www.freepressjournal.in/search?q=kashmir",
                           "pre_url": "",
                           "html_links": {"h": "li", "class": ""},
                           "main": {"div": "article", "identifier": "storyMainRoot"},
                           "heading": {"h": "h3", "class": "mainTitle"},
                           "media": {"img_tag": "div",
                                     "class": "imageBox"}},

}

ARTICLE_LENGTH = 60
