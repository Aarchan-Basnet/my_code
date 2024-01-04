from selenium import webdriver
from time import sleep

def get_url_and_save_page():
    urls = [
        "https://www.google.com/search?q=Guitar+Center&start=0&hl=en",
        "https://www.google.com/search?q=Sweetwater&start=0&hl=en",
        "https://www.google.com/search?q=acoustic+guitars&start=0&hl=en",
        "https://www.google.com/search?q=dj+equipment&start=0&hl=en",
        "https://www.google.com/search?q=drums&start=0&hl=en",
        "https://www.google.com/search?q=headphones&start=0&hl=en",
        "https://www.google.com/search?q=live+sound+gear&start=0&hl=en"
    ]

    for i, url in enumerate(urls, 1):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        sleep(100)

        with open(f'data/page{i}.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

        driver.quit()

def main():
    get_url_and_save_page()

if __name__ == "__main__":
    main()