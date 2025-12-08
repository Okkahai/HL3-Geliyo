from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    chrome_options = Options()
    # Şimdilik ek argüman YOK

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.get("https://www.google.com")
    input("Pencereyi kapatmak için Enter'a bas...")

if __name__ == "__main__":
    main()
