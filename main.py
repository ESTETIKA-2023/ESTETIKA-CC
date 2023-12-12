from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright
from rich import print
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def find_batik_villages():
    url_batik_villages = 'https://jadesta.kemenparekraf.go.id/atraksi/jenis/60'
    word_batik = 'Batik'

    processed_titles = set()
    processed_location = set()

    location_jawa_timur = {
        ("Desa Wisata Simbatan Keren, Kabupaten Magetan"),
        ("Desa Wisata Budaya Sendang, Kabupaten Tulungagung"),
        ("Desa Wisata Kertosari Pasuruan, Kabupaten Pasuruan"),
        ("Desa Wisata Kampung Batik, Kabupaten Tuban"),
        ("Desa Wisata Kemirigede, Kabupaten Blitar"),
        ("Desa Wisata Duren Sari Sawahan, Kabupaten Trenggalek"),
        ("Desa Wisata Wonoagung, Kabupaten Malang"),
        ("Desa Wisata Simbatan Keren, Kabupaten Magetan"),
    }

    location_jawa_tengah = {
        ("Desa Wisata Makukuhan Kembang Madu, Kabupaten Temanggung"),
        ("Desa Wisata Karangturi, Kabupaten Rembang"),
        ("Desa Wisata Kampoeng Djadhoel, Kota Semarang"),
        ("Desa Wisata Bakaran Wetan, Kabupaten Pati"),
        ("Desa Wisata Mangrove Pandansari Kaliwlingi, Kabupaten Brebes"),
    }

    location_yogyakarta = {
        ("Desa Wisata Wukirsari, Kabupaten Bantul"),
        ("Desa Wisata Wukirsari, Kabupaten Bantul"),
        ("Desa Wisata Wukirsari, Kabupaten Bantul"),
        ("Desa Wisata Putat, Kabupaten Gunung Kidul"),
        ("Desa Wisata Jerukwudel, Kabupaten Gunung Kidul"),
        ("Desa Wisata Wukirsari, Kabupaten Bantul"),
        ("Desa Wisata Rejowinangun, Kota Yogyakarta"),
        ("Desa Wisata DEWI GUMI, Kabupaten Bantul"),
        ("Desa Wisata Hargorejo, Kabupaten Kulon Progo"),
        ("Desa Wisata Wisata Wayang, Kabupaten Bantul"),
        ("Desa Wisata Wisata Wayang, Kabupaten Bantul"),
        ("Desa Wisata Nglanggeran, Kabupaten Gunung Kidul"),
        ("Desa Wisata Nglanggeran, Kabupaten Gunung Kidul"),
        ("Desa Wisata Wukirsari, Kabupaten Bantul"),
    }

    location_sumatera_utara = {
        ("Desa Wisata Batik Sekar Najogi, Kabupaten Padang Lawas Utara"),
    }

    location_sumatera_selatan = {
        ("Desa Wisata Beji Manik Karang, Kabupaten Ogan Komering Ulu Timur")
    }

    location_kalimantan_barat = {
        ("Desa Wisata Kampong Melayu BML, Kota Pontianak"),
    }

    location_banten = {
        ("Desa Wisata Curuggoong, Kabupaten Serang")
    }

    location_lampung = {
        ("Desa Wisata Labuhan Ratu Vii, Kabupaten Lampung Timur")
    }

    def get_province(location_batik):
        if location_batik in location_jawa_timur:
            province = "Jawa Timur"
            return province
        elif location_batik in location_jawa_tengah:
            province = "Jawa Tengah"
            return province
        elif location_batik in location_yogyakarta:
            province = "Daerah Istimewa Yogyakarta"
            return province
        elif location_batik in location_sumatera_utara:
            province = "Sumatra Utara"
            return province
        elif location_batik in location_sumatera_selatan:
            province = "Sumatra Selatan"
            return province
        elif location_batik in location_kalimantan_barat:
            province = "Kalimantan Barat"
            return province
        elif location_batik in location_banten:
            province = "Banten"
            return province
        elif location_batik in location_lampung:
            province = "Lampung"
            return province
        return "Unknown"
        
    def saved_db():
        data = {
            "Nama Atraksi": title_atraksi,
            "Location": location_batik,
            "Price": price_abstraksi,
            "More Info": url_detail_village,
            "Image": url_detail_image,
            "Province": province
            }

        def save(collection_id, document_id, data):
            db.collection(collection_id).document(document_id).set(data)

        document_id = (f"{index}-{title_atraksi.replace(' ', '_').replace('[', '').replace(']', '')}")

        save(
            collection_id= "batik_tourist_attractions",
            document_id=document_id,
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
        # # browser keliatan
        # browser = p.chromium.launch(headless=False)

        # # biar bowser ga keliatan
        browser = p.chromium.launch(headless=True)

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

                province = get_province(location_batik)

                if title_atraksi not in processed_titles and word_batik in title_atraksi:
                    processed_titles.add(title_atraksi)
                    processed_location.add(location_batik)

                    saved_db()
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