from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os
import re

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys("*******")
password_input.send_keys("*******")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5)

profile_name = "ozgeyagizz"
driver.get(f"https://www.instagram.com/{profile_name}/")
time.sleep(3)

scroll_pause_time = 2
scroll_count = 5

post_links = []
for _ in range(scroll_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    try:
        posts = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
        for post in posts:
            link = post.get_attribute("href")
            if link not in post_links:
                post_links.append(link)
        print(f"Toplam {len(post_links)} gönderi bulundu.")
    except Exception as e:
        print("Gönderi linklerini alma hatası:", e)

safe_profile_name = re.sub(r"\W+", "_", profile_name)

download_folder = os.path.join("downloaded_images", safe_profile_name)
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for index, post_link in enumerate(post_links):
    driver.get(post_link)
    time.sleep(3)

    try:
        img_element = driver.find_element(By.XPATH, "//article//img")
        img_url = img_element.get_attribute("src")
        print(f"Görsel URL'si alındı: {img_url}")

        if img_url:
            try:
                img_data = requests.get(img_url).content
                img_name = os.path.join(
                    download_folder, f"{safe_profile_name}_image_{index + 1}.jpg"
                )
                with open(img_name, "wb") as file:
                    file.write(img_data)
                print(f"Görsel indirildi: {img_name}")
            except Exception as e:
                print(f"Görsel indirme hatası: {e}")
        else:
            print("Görsel URL'si alınamadı.")

    except Exception as e:
        print(f"Görsel URL'sini alma hatası: {e}")

driver.quit()
