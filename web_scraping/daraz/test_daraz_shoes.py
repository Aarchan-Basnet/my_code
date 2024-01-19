from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import os

current_dir = os.getcwd()
try:
    screenshot_dir = os.path.join(current_dir, 'screenshots')
    os.makedirs(screenshot_dir)
except FileExistsError:
    print("'screenshots' folder already exixts.")

# open browser
browser = webdriver.Firefox()

# load webpage
browser.get('https://www.daraz.com.np')
browser.maximize_window()

# get input elements
search_input = browser.find_element(By.CLASS_NAME,
                                    'search-box__input--O34g')
search_button = browser.find_element(By.CLASS_NAME,
                                     'search-box__button--1oH7')

# execute search
search_input.send_keys('shoes')
sleep(2)
search_button.click()

# get product title
products = []
for i in range(10):
    print(f'Scraping page', i+1)
    browser.save_full_page_screenshot(f'screenshots/daraz_shoes_{i+1}.png')
    product_elements = browser.find_elements(By.CLASS_NAME,
                                             'info--ifj7U')
    for element in product_elements:
        # get title, price, landing link
        title = element.find_element(By.CLASS_NAME, 'title--wFj93').text
        price = element.find_element(By.CLASS_NAME, 'price--NVB62').text
        landing_link = element.find_element(
            By.TAG_NAME, 'a').get_attribute('href')

        # append to products list
        products.append({'Title': title,
                         'Price': price,
                         'LandingLink': landing_link})

    next_button = browser.find_element(By.CLASS_NAME,
                                       'ant-pagination-item-link')
    next_button.click()
    sleep(2)

browser.quit()

df = pd.DataFrame(products)
print(df)
df.to_csv('products_daraz_shoes.csv', index=False)
