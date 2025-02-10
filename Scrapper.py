from bs4 import BeautifulSoup
import requests as rq
import pandas as pd

BASE_URL = "https://riyasewana.com/search/cars?page="
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
           'Accept-Language': 'en-US,en;q=0.5'}
ITEM_URLS_BY_PAGE = []

Vehicle_data_frame = pd.DataFrame()
page_urls = [BASE_URL + str(page_number) for page_number in range(251, 301)]


def item_link_extract(PAGE_URL, HEADERS):
    item_links = []
    try:
        web_content = rq.get(PAGE_URL, headers=HEADERS)
        structured_web_content = BeautifulSoup(web_content.content, 'html.parser')
        items = structured_web_content.find_all('li', attrs={'class': 'item round'})

        for item in items:
            try:
                item_header = item.find('h2', attrs={'class': 'more'})
                item_link_anker = item_header.find('a')
                item_link = item_link_anker.get('href') if item_link_anker else None
                item_links.append(item_link)
            except Exception as e:
                print(f"Error extracting item link: {e}")
    except Exception as err:
        print(f"ERROR: {err}>>> PAGE : {PAGE_URL}")
    finally:
        return item_links



def extract_item_data(Item_URL, HEADERS):
    global Vehicle_data_frame
    try:
        web_content = rq.get(Item_URL, headers=HEADERS)
        structured_web_content = BeautifulSoup(web_content.content, 'html.parser')

        caption = structured_web_content.find('h1').text
        date_time = structured_web_content.find('h2').text

        detail_table = structured_web_content.find('table', attrs={'class': 'moret'})
        if detail_table:
            details = [td.text for td in detail_table.find_all('td', attrs={'class': 'aleft'})]
            column_names = [details[pos] for pos in range(0, len(details), 2)]
            data_points = [details[pos] for pos in range(1, len(details), 2)]

            column_names.extend(["Caption","DateTime"])
            data_points.extend([caption,date_time])

            if len(column_names) == len(data_points):  
                extracted_df = pd.DataFrame([data_points], columns=column_names)
                Vehicle_data_frame = pd.concat([Vehicle_data_frame, extracted_df], axis=0, ignore_index=True)
                print("Item Extracted Successfully...")

    except Exception as e:
        print(f"Error extracting data from item: {e}")


print("\nPage Urls ...\n")
for page_url in page_urls:
    print(page_url)
    ITEM_URLS_BY_PAGE.extend(item_link_extract(page_url, HEADERS))

print("\nItem Extracting Started...\n")

for item_urls in ITEM_URLS_BY_PAGE:
    if item_urls:
        extract_item_data(item_urls, HEADERS)

print(Vehicle_data_frame)
Vehicle_data_frame.to_excel("vehicle5.xlsx", index=False)

print("\n>>>>Process Done ...")
