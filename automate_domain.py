from selenium import webdriver
import time, credentials
import pandas as pd
from rich import print as rprint

USERNAME = credentials.MY_DASHBOARD_USERNAME
PASSWORD = credentials.MY_DASHBOARD_PASSWORD
df = pd.read_excel('/home/roopchand/test/scrapyTest/Check_Point_Data.xlsx', sheet_name='Domains')
driver = webdriver.Chrome(executable_path="/home/shivam/scrapytut/chromedriver/chromedriver")


type = 0
if (type==0):
    driver.get('http://dashboard.newsdata.local/core/domain/add/')
else:
    driver.get('http://dash115.newsdata.io/core/domain/add/')


# driver.get('http://dashboard.newsdata.local/core/domain/add/')
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

    name_field = driver.find_element('xpath', '//div[@class="form-row field-name"]//input[@id="id_name"]')
    name_field.send_keys(entry['Name'])
    time.sleep(2)

    domain_field = driver.find_element("xpath", '//div[@class="form-row field-domain"]//input[@id="id_domain"]')
    domain_field.send_keys(entry['Domain'])

    display_name_field = driver.find_element("xpath", '//*[@id="id_display_name"]')
    display_name_field.send_keys(entry['Display_Name'])

    connection = driver.find_element("xpath", '//select[@name="connection"]/option[3]').click()

    priority_field = driver.find_element('xpath', "//div[@class='form-row field-priority']/div/input[@id='id_priority']")
    priority_field.send_keys(int(entry['Priority']))
    # time.sleep(4)

    desciption_field = driver.find_element('xpath', '//*[@id="id_description"]')
    desciption_field.send_keys(entry['Description'])

    Is_Full_Description_field = driver.find_element('xpath', "//select[@name='is_full_description']/option[1]").click()
    time.sleep(2)
    Save_Add_More = driver.find_element("xpath", '//*[@id="domain_form"]/div/div/input[2]').click()
    time.sleep(1)
    # Add_More = driver.find_element("xpath", '//*[@id="content-main"]/ul/li/a').click()
    # time.sleep(2)