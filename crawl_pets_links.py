from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from urllib import parse


real_crawl = False
file_name = 'pets_links_from_tables'
base_url = 'https://theunderminejournal.com'

if real_crawl:
    url = 'https://theunderminejournal.com/#eu/defias-brotherhood/category/battlepets'  # pets full list page

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
    with open(file_name+'.txt', 'w', encoding="utf-8") as f:
        f.write(source_code)

    driver.close()
else:
    # read source code to txt
    with open(file_name+'.txt', 'r', encoding="utf8") as f:
        source_code = f.read()

    # convert txt to bs object
    soup = BeautifulSoup(source_code, features="lxml")

    usefuls = soup.findAll("td", {"rowspan": "1", 'class': 'name'})

    for useful in usefuls:
        link = useful.a['href']
        pet_url = parse.urljoin(base_url, link)
        print(pet_url)

        # # create a new Chrome session and get source code
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(3000)
        # driver.get(pet_url)
        # driver.close()

    # # get data from table, (https://towardsdatascience.com/scrape-tabular-data-with-python-b1dd1aeadfad)
    # tables = soup.find_all("table")
    # # save tables to files
    # indexes = range(3, 13)  # table that are for pets
    # for index in indexes:
    #     table = tables[index]
    #     # get all tag attributes in the table
    #     tab_data = [[cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")]
    #     # onvert table to pandas DataFrame object
    #     df = pd.DataFrame(tab_data)
    #     # remove first useless row
    #     df.columns = df.iloc[0, :]
    #     df.drop(index=0, inplace=True)
    #     # save and visualise DataFrame as html file (https://stackoverflow.com/questions/18528533/pretty-printing-a-pandas-dataframe)
    #     df.to_html('tests/test_'+str(index)+'.html')


