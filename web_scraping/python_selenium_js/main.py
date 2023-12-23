from selenium import webdriver
from selenium.webdriver.common.by import By

def download_json(jsFilePath):
    print("Downloading json...")
    with open(jsFilePath, 'r', encoding='utf-8') as file:
        script = file.read()
    driver.execute_script(script)

if __name__ == "__main__":
    #create selenium driver for firefox
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    
    #goto url website
    url = "https://www.nepalstock.com/today-price"
    driver.get(url)
    driver.maximize_window()
    

    download_json('myscript.js')
    
    driver.quit()
