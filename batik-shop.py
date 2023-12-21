from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def scraping_batik(search_query, required_keywords=None, collection_name='batik_shop'):
    if required_keywords is None:
        required_keywords = []

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    search_link = f"https://www.google.com/search?tbm=shop&hl=en-US&psb=1&ved=2ahUKEwi_jOHH9daCAxUinUsFHVFgCSAQu-kFegQIABAJ&q={search_query} Ori"
    driver.set_window_size(1400, 800)
    driver.get(search_link)

    data = BeautifulSoup(driver.page_source, 'html.parser')
    i = 1

    for area in data.find_all('div', class_="sh-dgr__content"):
        print("Menyimpan data ke-" + str(i))
        nama_element = area.find('h3', class_="tAxDx")

        if nama_element:
            nama = nama_element.get_text()

            if all(keyword.lower() in nama.lower() for keyword in required_keywords) and not any(exclude_word.lower() in nama.lower() for exclude_word in ['print', 'baju', 'pewarna', 'printing', 'souvenir', 'pajangan', 'patung', 'kayu', 'magnet']):
                gambar = area.find('img')['src']
                harga = area.find('span', class_="a8Pemb OFFNJ").get_text()
                link_element = area.find('a', class_="shntl")
                link_href = link_element.get('href') if link_element else None

                parsed_link = urlparse(link_href)
                url_params = parse_qs(parsed_link.query)
                final_link = url_params.get('url', [])[0] if 'url' in url_params else None

                # Membuat dictionary dari data yang diambil
                data_dict = {'Gambar': gambar, 'Nama': nama, 'Harga': harga, 'Link': final_link}

                # Mengubah search_query menjadi lowercase dan mengganti spasi dengan underscore
                search_query_lowercase = search_query.lower().replace(' ', '_')

                # Menambahkan satu data ke dalam satu dokumen di dalam koleksi 'jenis_batik' di dalam koleksi 'batik_shop'
                jenis_batik_ref = db.collection(collection_name).document('jenis_batik')
                jenis_batik_ref.collection(search_query_lowercase).document(f'data_{i}').set(data_dict)
                i += 1

    driver.quit()

scraping_batik('Batik Bali', required_keywords=['batik', 'bali'])
scraping_batik('Batik Betawi', required_keywords=['batik', 'betawi'])
scraping_batik('Batik Celup', required_keywords=['batik', 'celup'])
scraping_batik('Batik Cendrawasih', required_keywords=['batik', 'cendrawasih'])
scraping_batik('Batik Ceplok', required_keywords=['batik', 'ceplok'])
scraping_batik('Batik Ciamis', required_keywords=['batik', 'ciamis'])
scraping_batik('Batik Garutan', required_keywords=['batik', 'garutan'])
scraping_batik('Batik Gentongan', required_keywords=['batik', 'gentongan'])
scraping_batik('Batik Kawung', required_keywords=['batik', 'kawung'])
scraping_batik('Batik Keraton', required_keywords=['batik', 'keraton'])
scraping_batik('Batik Lasem', required_keywords=['batik', 'lasem'])
scraping_batik('Batik Megamendung', required_keywords=['batik', 'megamendung'])
scraping_batik('Batik Parang', required_keywords=['batik', 'parang'])
scraping_batik('Batik Pekalongan', required_keywords=['batik', 'pekalongan'])
scraping_batik('Batik Priangan', required_keywords=['batik', 'priangan'])
scraping_batik('Batik Sekar', required_keywords=['batik', 'sekar'])
scraping_batik('Batik Sidoluhur', required_keywords=['batik', 'sidoluhur'])
scraping_batik('Batik Sidomukti', required_keywords=['batik', 'sidomukti'])
scraping_batik('Batik Tambal', required_keywords=['batik', 'tambal'])
scraping_batik('Batik Wayang', required_keywords=['batik', 'wayang'])
