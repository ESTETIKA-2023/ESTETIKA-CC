from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright
from rich import print
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("tes-project-1-c64c0-firebase-adminsdk-ard2g-e66bf333bf.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def find_batik_villages():
    url_batik_villages = 'https://jadesta.kemenparekraf.go.id/atraksi/jenis/60'
    word_batik = 'Batik'

    processed_titles = set()
    processed_location = set()

    def saved_db():
        data = {
            "Nama Atraksi": title_atraksi,
            "Location": location_batik,
            "Price": price_abstraksi,
            "More Info": url_detail_village,
            "Image": url_detail_image
            }

        def save(collection_id, docuent_id, data):
            db.collection(collection_id).document(docuent_id).set(data)

        save(
            collection_id= "Batik Villages",
            docuent_id= (f"{index} | {title_atraksi}"),
            data= data
        )


    def scroll_click_more(page):
        # Scroll to the "Load More" button
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Wait for the button to become visible
        page.wait_for_selector('a#loadmore')

        # Click the "Load More" button
        page.click('a#loadmore')

        # Wait for a short time to allow content to load
        time.sleep(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # # biar bowser ga keliatan
        # browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_batik_villages)
        # time.sleep(2)

        while True:
            scroll_click_more(page)

            # Get the updated HTML content after clicking "Load More"
            html_content = page.content()
            soup = BeautifulSoup(html_content, 'html.parser')
            jobs = soup.find_all('div', class_='col-lg-4 col-md-6')
            
            for index, job in enumerate(jobs):
                item_list = job.find('div', class_ = 'listing-item')
                image_batik = item_list.img['src']
                price_abstraksi = item_list.find('div', class_ = 'listing-badge rank2')

                if price_abstraksi != None:
                    price_abstraksi = item_list.find('div', class_ = 'listing-badge rank2').text
                else:
                    price_abstraksi = ('Rp.0')

                item_content = item_list.find('div', class_ = 'listing-item-content')
                title_atraksi = item_content.find('h3').text
                location_batik = item_content.find('span', class_ = '').text


                # Ambil data more detail artikel
                url_detail_village = job.a['href']

                url_detail_image = (f'https://jadesta.kemenparekraf.go.id/{image_batik}')

                if title_atraksi not in processed_titles and word_batik in title_atraksi:
                    processed_titles.add(title_atraksi)
                    processed_location.add(location_batik)

                    saved_db()


                        # print(index)
                        # print(f'Nama Atraksi: {title_atraksi}')
                        # print(f'Lcation: {location_batik}')
                        # print(f'Harga: {price_abstraksi}')
                        # print(f'More Info: {url_detail_village}')
                        # print(f'Image: {url_detail_image}\n')
                        
                # to check jika kondisi judul nya sama tetapi lokasinya harus beda
                elif title_atraksi in processed_titles and word_batik in title_atraksi and location_batik not in processed_location:
                    processed_location.add(location_batik)
                    saved_db()
                else:
                    continue

            # Check if there is no more "Load More" button
            load_more_button = page.query_selector('a#loadmore')
            if not load_more_button:
                break

    browser.close()

if __name__ == '__main__':
    find_batik_villages()