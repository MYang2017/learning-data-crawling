from bs4 import BeautifulSoup
from selenium import webdriver
import time


real_crawl = False

if real_crawl:
    url = 'https://theunderminejournal.com/#eu/defias-brotherhood/category/battlepets'  # pets full list page
    url = 'https://theunderminejournal.com/#eu/defias-brotherhood/battlepet/2850'  # one pet detail page

    # create a new Chrome session and get source code
    driver = webdriver.Chrome()
    driver.implicitly_wait(3000)
    driver.get(url)
    src = driver.page_source

    # wait for page to load
    time.sleep(3)

    # get dynamic DOM
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("innerHTML")

    with open('text.txt', 'w', encoding="utf-8") as f:
        f.write(source_code)

    driver.close()
else:
    with open('text.txt', 'r', encoding="utf8") as f:
        source_code = f.read()

# convert txt? to html
soup = BeautifulSoup(source_code, features="lxml")

tables = soup.find_all("table")
print(len(tables))

for tag in soup.find_all('span', {"class": "money-gold"}):
    print(tag.string)


