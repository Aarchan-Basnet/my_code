# goto nepse website ; save html ; parse html ; extract table into json file
# please create a 'htmls' folder to store html files

from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import html
from time import sleep
import pandas as pd
import json


def fetch_url_and_save_html():
    print("Fetching data ......")
    driver = webdriver.Firefox()

    # Open the webpage using Selenium
    url = "https://www.nepalstock.com/today-price"
    driver.get(url)
    driver.maximize_window()
    sleep(5)

    # get pagination list
    with open('nepalstock_today_price.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    with open('nepalstock_today_price.html', 'rb') as f:
        html_content = f.read()
    tree = html.fromstring(html_content)
    pagination_list = tree.xpath(
        "//pagination-template//li[last() - 1]//span[last()]/text()")
    today_date = tree.xpath(
        "//div[@class='ticker__date']//strong//text()")

    global pages
    global today
    pages = int(pagination_list[0])
    today = str(today_date[-1])

    # Save the webpage content as an HTML file
    for i in range(pages):
        print(f"Scraping page {i+1}")
        filename = f'nepalstock_today_price{i+1}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        next_button = driver.find_element(By.CLASS_NAME,
                                          'pagination-next')
        next_button.click()
        sleep(5)

    driver.quit()


def parse_columns():
    print("Parsing columns ...")
    with open('nepalstock_today_price1.html', 'rb') as f:
        html_content = f.read()

    # Parse the HTML using lxml
    tree = html.fromstring(html_content)

    # Extract all columns using xpath
    columns = tree.xpath("//div[@class='table-responsive']//th//text()")
    return columns


def parse_data():
    print("Parsing data ...")
    cell_data = []
    for i in range(pages):
        filename = f'nepalstock_today_price{i+1}.html'
        with open(filename, 'rb') as f:
            html_content = f.read()

        tree = html.fromstring(html_content)

        # extract data rowwise
        data_rows = tree.xpath("//div[@class='table-responsive']//tbody/tr")
        for row in data_rows:
            data = row.xpath("td//text()")
            cell_data.append(data)

    return cell_data


def clean_data(data):
    print("Cleaning data ...")
    df = pd.DataFrame(data)

    df.iloc[:, 9] = df.iloc[:, 9].astype(str) + df.iloc[:, 10].astype(str)
    df.drop(df.columns[10], axis=1, inplace=True)
    df.to_csv("nepalstock_today.csv")
    cleaned_data = df.values.tolist()

    return cleaned_data


def data_to_json(data_list, columns):
    print("Getting json file ...")

    def create_nested_dict(row):
        columns = df.columns
        Name = columns[1]  # change here for main key
        name = row[Name]
        other_columns = columns[2:]  # change here for inner key
        nested_dict = {column: row[column] for column in other_columns}
        return {name: nested_dict}

    df = pd.DataFrame(data_list, columns=columns)
    # Apply the function to each row
    nested_dicts = df.apply(create_nested_dict, axis=1)

    # Convert the list of dictionaries to a single dictionary
    result_dict = {}
    for nested_dict in nested_dicts:
        result_dict.update(nested_dict)

    # convert dict to json string
    json_string = json.dumps(result_dict, indent=4)
    print(json_string)

    # write to json file
    with open('nepalstock_json.json', 'w') as file:
        json.dump(result_dict, file)


if __name__ == "__main__":
    fetch_url_and_save_html()
    columns = parse_columns()
    cell_data = parse_data()
    cleaned_data = clean_data(cell_data)
    data_to_json(cleaned_data, columns)
