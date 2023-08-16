from selenium import webdriver
import time, credentials
import pandas as pd
from rich import print as rprint
from selenium.webdriver.support.select import Select

USERNAME = credentials.MY_DASHBOARD_USERNAME
PASSWORD = credentials.MY_DASHBOARD_PASSWORD
df = pd.read_excel('/home/roopchand/test/scrapyTest/Check_Point_Data.xlsx', sheet_name='Sources')
driver = webdriver.Chrome(executable_path="/home/shivam/scrapytut/chromedriver/chromedriver")

type = 0
if (type==0):
    driver.get('http://dashboard.newsdata.local/core/source/add/')
else:
    driver.get('http://dash115.newsdata.io/core/source/add/')
# driver.get('http://dashboard.newsdata.local/core/source/add/')
time.sleep(1)
Username = driver.find_element('xpath', '//*[@id="id_username"]')
Username.send_keys(USERNAME)
Password = driver.find_element("xpath", '//*[@id="id_password"]') 
Password.send_keys(PASSWORD)
Log_In = driver.find_element("xpath", '//*[@id="login-form"]/div[3]/input')
Log_In.click()
time.sleep(1)


for i in df.index:
    entry = df.loc[i]
    rprint(entry)
    # Select the domain field using a XPATH selector
    domain_field = Select(driver.find_element('xpath', '//select[@name="domain_id"]'))
    domain_field.select_by_visible_text(entry['Name'])
    # Find the source URL field using an ID selector
    source_url_field = driver.find_element("xpath", '//input[@id="id_url"]')
    source_url_field.send_keys(entry['Source_Link'])
    # Select the status field using a XPATH selector
    Status_field = driver.find_element('xpath', "//select[@name='feed_status']/option[1]").click()
    # Select the language field using a XPATH selector
    language_field = Select(driver.find_element("xpath", "//select[@name='language_id']"))
    language_field.select_by_visible_text(entry['Language'])
    # Select the country field using a CSS selector
    country_field = Select(driver.find_element("xpath", "//select[@name='country_id']"))
    country_field.select_by_visible_text(entry['Country'])
    # Select the category field using a CSS selector
    category_field = Select(driver.find_element("xpath", "//select[@name='category_id']"))
    category_field.select_by_visible_text(entry['Category'])
    #select custom collection 
    # custom_collection_field = driver.find_element('xpath', '//*[@id="id_custom_api_ids"]')
    # custom_collection_field.send_keys('13')
    time.sleep(1)
    Save_Add_More = driver.find_element("xpath", '//*[@id="source_form"]/div/div/input[2]').click()
    # Add_More = driver.find_element("xpath", '//*[@id="content-main"]/ul/li/a').click()
    # time.sleep(1)


