import requests
from bs4 import BeautifulSoup

def get_dolar_kuru():
    url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"  # Bigpara'nın dolar sayfası
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Sayfa içeriğini al
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Hata durumu varsa istisna fırlatır
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Dolar kurunu çek (HTML yapısını kontrol edin, sınıf isimleri değişebilir)
        dolar_kuru = soup.find("span", {"class": "value"}).text
        return dolar_kuru
    
    except Exception as e:
        return f"Hata oluştu: {e}"

if __name__ == "__main__":  # Bu satır doğru yazılmalı
    dolar_kuru = get_dolar_kuru()
    print(f"Güncel Dolar Kuru: {dolar_kuru}")
