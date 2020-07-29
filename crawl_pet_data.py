from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd


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

    # save source code to txt
    with open('text.txt', 'w', encoding="utf-8") as f:
        f.write(source_code)

    driver.close()
else:
    # read source code to txt
    with open('text.txt', 'r', encoding="utf8") as f:
        source_code = f.read()

# convert txt to html
soup = BeautifulSoup(source_code, features="lxml")

# get data from table, (https://towardsdatascience.com/scrape-tabular-data-with-python-b1dd1aeadfad)
tables = soup.find_all("table")
table = tables[4]
# get all tag attributes in the table
tab_data = [[cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")]
# onvert table to pandas DataFrame object
df = pd.DataFrame(tab_data)
# remove first useless row
df.columns = df.iloc[0, :]
df.drop(index=0, inplace=True)
# save and visualise DataFrame as html file (https://stackoverflow.com/questions/18528533/pretty-printing-a-pandas-dataframe)
df.to_html('temp.html')

# for tag in soup.find_all('span', {"class": "money-gold"}):
#     print(tag.string)


