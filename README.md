Created this repo to learn web data crawling


https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/
very good beginner crawler tutorial that covers a lot, most important:
robots.txt
basic select_one usage
other things:
pulling 'static' data (from table), (cannot get data requires JS rendering)
i/o
use panda to analyse data
visualisation


requirements and libraries used:
chromedriver.exe
from bs4 import BeautifulSoup
from selenium import webdriver
import time