from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

print("""
ZynpBus
ZynpBus
ZynpBus
ZynpBus
ZynpBus
Hos Geldin
                           -sekerlipencere      
""")


# WebDriver'ı başlat
driver = webdriver.Chrome()

try:
    # Siteye git
    driver.get("https://www.bursakart.com.tr/cardoperations/cardLoad")

    # Sayfanın tam yüklenmesini bekleyin
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="card-price"]'))
    )

    # Form 1'i doldur (XPATH: //*[@id="card-price"])
    card_price_input = driver.find_element(By.XPATH, '//*[@id="card-price"]')
    card_price_input.send_keys("ogrenci isen 6 yaz degilsen 12 yaz buraya")

    # Form 2'yi doldur (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input)
    form_2_input = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input')
    form_2_input.send_keys("kart_id")
    
    # Form 3'ü doldur (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/input)
    form_3_input = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/input')
    form_3_input.send_keys("tel_no")
    
    # Form 4'ü doldur (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/input)
    form_4_input = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/input')
    form_4_input.send_keys("isim_soyisim")


     # Butona tıkla (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div)
    buttton = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div')
    
    buttton.click()

    time.sleep(1)  # Programı 2 saniye beklet


    # Form 5'i doldur (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input)
    form_5_input = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input')
    form_5_input.send_keys("kredi_kart_no")

    # Form 6'yı doldur (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/input)
    form_6_input = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/input')
    form_6_input.send_keys("kredi_kart_sahibi")

   

    # Dropdown menüsünden seçim yap (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/select)
    select_element_1 = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/select')
    select_element_1.send_keys("kredi_kart_ay")

    # Bir sonraki dropdown menüsünden seçim yap (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/select)
    select_element_2 = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/select')
    select_element_2.send_keys("kredi_kart_year")

    # Form 7'yi doldur (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/input)
    form_7_input = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/input')
    form_7_input.send_keys("ccv")

    # İşaret kutularını işaretle (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/label[1]/span ve /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/label[2]/span)
    checkbox_1 = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/label[1]/span')
    checkbox_1.click()
    checkbox_2 = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/label[2]/span')
    checkbox_2.click()

    # Butona tıkla (XPATH: /html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[4]/button)
    button = driver.find_element(By.XPATH, '/html/body/app-root/app-cardoperations/div[1]/section/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[4]/button')
    button.click()

    time.sleep(10)

    file_url = 'https://web_adresiniz/post_verileri.txt'
    file_name = 'post_verileri.txt'


    # İnternetten dosyayı indir
    response = requests.get(file_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)


# Form 8'i doldur (XPATH: //*[@id="otpCode"])
    form_8_input = driver.find_element(By.XPATH, '//*[@id="otpCode"]')
    with open('post_verileri.txt', 'r') as file:
        content = file.read()
    form_8_input.send_keys(content)

    time.sleep(1)

    # Butona tıkla (XPATH: //*[@id="send"])
    send_button = driver.find_element(By.XPATH, '//*[@id="send"]')
    

except Exception as e:
    print("Hata:", e)

# WebDriver'ı kapatmadan işlem tamamlandıktan sonra sayfanın açık kalmasını sağlamak için bekleme
input("İşlem tamamlandı, çıkmak için Enter'a basın...")

print("""
ZynpBus
ZynpBus
ZynpBus
ZynpBus
ZynpBus
Allaha Emanet
                           -sekerlipencere      
""")


# WebDriver'ı kapat
driver.quit()
