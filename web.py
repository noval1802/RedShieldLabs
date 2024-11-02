import requests
from bs4 import BeautifulSoup

# URL dari halaman yang ingin di-scrape
url = 'https://contohwebsite.com/artikel'

# Mengirim permintaan ke halaman
response = requests.get(url)

# Memeriksa status kode untuk memastikan halaman berhasil diakses
if response.status_code == 200:
    # Parsing konten halaman dengan BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Mengumpulkan judul artikel
    articles = soup.find_all('h2', class_='judul-artikel')  # Sesuaikan selector

    # Menampilkan hasil
    for idx, article in enumerate(articles, start=1):
        print(f"{idx}. {article.get_text(strip=True)}")
else:
    print("Gagal mengakses halaman:", response.status_code)
