from lxml import html
import json

def sponsored_ads_to_json(tree):
    print("Parsing sponsored ads ...")
    my_list = []
    for i in range(1,8):
        sponsored_ads = tree.xpath("//div[@id='bGmlqc']")
        #print(type(sponsored_ads))
        #print(sponsored_ads)
        for num, element in enumerate(sponsored_ads, 1):
            # my_dict = {}
            cards = element.xpath(".//div[@class='mnr-c c3mZkd pla-unit']")
            #print(cards)
            # my_list = []
            for id, card in enumerate(cards, 1):
                data = {}
                name_list = card.xpath(".//div[@class='pla-unit-container']//span[@class='pymv4e']//text()")
                #print(name_list)
                price_list = card.xpath(".//div[@class='pla-unit-container']//div[@class='T4OwTb']//text()")
                #print(price_list)
                vendor_list = card.xpath(".//div[@class='pla-unit-container']//div[@class='LbUacb']//text()")
                #print(vendor_list)
                total_reviews_list = card.xpath(".//div[@class='pla-unit-container']//div[@class='pla-extensions-container']//span[@class='fl pbAs0b']//text()")
                #print(total_reviews_list)
                ratings_list = card.xpath(".//div[@class='pla-unit-container']//div[@class='pla-extensions-container']//span[@class='z3HNkc']")
                #print(ratings[0].get('aria-label'))
                #print(ratings_list)

                name = name_list[0].strip() if name_list else None
                vendor = vendor_list[0].strip() if vendor_list else None
                if price_list:
                    discounted_price = price_list[0].strip() if len(price_list)==2 else None
                    retail_price = price_list[1].strip() if len(price_list)==2 else price_list[0].strip()
                else:
                    discounted_price = None
                    retail_price = None
                total_reviews = total_reviews_list[0].strip() if total_reviews_list else None
                ratings = ratings_list[0].get('aria-label').strip() if ratings_list else None

                # print(name)
                # print(vendor)
                # print(discounted_price)
                # print(retail_price)
                # print(total_reviews)
                # print(ratings)

                data = {
                    "item_name": name,
                    "vendor": vendor,
                    "discounted_price": discounted_price,
                    "retail_price": retail_price,
                    "ratings": ratings,
                    "total_reviews": total_reviews
                }
                my_list.append(data)

    print(my_list)

    with open('data/sponsored_ads.json', 'w', encoding='utf-8') as file:
        json.dump(my_list, file)
    print("Json saved successfully.")

    return my_list

def organic_ads_to_json(tree):
    print("Parsing organic ads ...")
    my_list = []
    for i in range(1,8):
        organic_ads = tree.xpath("//div[@id='rcnt']//div[@class='srKDX cvP2Ce']")
        # print(organic_ads)

        for element in organic_ads:
            data = {}
            vendor_list = element.xpath(".//div[@class='GTRloc']//span[@class='VuuXrf']//text()")
            # print(vendor_list[0])
            landing_link = element.xpath(".//div[@class='yuRUbf']//a")[0].get('href')
            # print(landing_link)
            title_list = element.xpath(".//div[@class='yuRUbf']//a//text()")
            # print(title_list[0])

            vendor = vendor_list[0] if vendor_list else None
            landing_link = landing_link if landing_link else None
            title = title_list[0] if title_list else None

            data = {
                "title": title,
                "vendor": vendor,
                "landing_link": landing_link
            }

            my_list.append(data)
    print(my_list)

    with open("data/organic_ads.json", "w", encoding='utf-8') as file:
        json.dump(my_list, file)
    print("Json saved successfully.")

    return my_list


def main():
    with open('data/headphone.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    tree = html.fromstring(html_content)

    sponsored_ads = sponsored_ads_to_json(tree)
    organic_ads = organic_ads_to_json(tree)

if __name__ == "__main__":
    main()