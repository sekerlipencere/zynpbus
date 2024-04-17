import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("""
ZynpBus
ZynpBus
ZynpBus
ZynpBus
ZynpBus
Hos Geldin
                           -sekerlipencere      
""")

def main():
    # WebDriver'ı başlat
    driver = webdriver.Chrome()

    while True:
        try:
            # Web sitesini aç
            driver.get("https://www.bursakart.com.tr/cardoperations/balanceInquiry")
            time.sleep(1)
            # Belirtilen XPath'e sahip butona tıkla
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div[2]"))).click()
            time.sleep(1)

            # Belirtilen XPath'e sahip forma 56 yaz
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/input"))).send_keys("kart_idniz")
            time.sleep(1)

            # Belirtilen XPath'e sahip butona tıkla
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div"))).click()
            time.sleep(1)

            # Belirtilen XPath'e sahip veriyi al
            veri = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]"))).text

            # Alınan veriyi konsola yazdır
            print("Alınan veri:", veri)

            # Eğer alınan veri "63,75 ₺" değilse bir python dosyası çalıştır
            if veri != "sizinbakiyeniz":
                subprocess.run(['python', 'bakiye.py'])

            time.sleep(60)  # 1 dakika bekleme
        except Exception as e:
            print("Hata:", e)

    # WebDriver'ı kapat
    driver.quit()

if __name__ == "__main__":
    main()
