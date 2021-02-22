from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import logging as logger


def initiateLatestNewsEngine(url, targetClass,isNormal):
    logger.debug("getting news....")
    page = req.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    article  = soup.find_all(class_=targetClass)
    logger.debug("processing news....")
    return processLatestNews(article, isNormal)


def processLatestNews(article, isNormal):
    news=""
    str=""

    if(isNormal):
        for i in article:
            news = news+ i.get_text()+"\n"
    else:
        for i in article:
            news = news + i.get_text() + "\n"    
    return news
    


def downloadNews(articleName):
    logger.debug("creating local copy......")
    f = open("thehindulatest.txt","w")
    f.write(articleName)
    f.close()
    logger.debug("finished.....")

logger.basicConfig(level=logger.DEBUG)
logger.debug("Welcome to Renegade inc. news portal")
article1 = initiateLatestNewsEngine("https://www.thehindu.com/latest-news/", "latest-news", True)
article2 = initiateLatestNewsEngine("https://www.mygov.in/covid-19", "iblock_text", True)
finalArticle = "Coronavirus Update\n"+article2+"\n"+"Latest News \n"+article1
downloadNews(finalArticle)
