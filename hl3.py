"""
WhatsApp Automated Message Sender
Sends scheduled messages to a WhatsApp group using Selenium WebDriver.
"""

import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
GROUP_NAME = "Fuckbody system"
MESSAGE = "Beyler hl3 bugün çikacakmiş"
SEND_TIME = "21:30"


def open_whatsapp():
    """
    Opens WhatsApp Web in Chrome with persistent user profile.
    
    Returns:
        webdriver.Chrome: Configured Chrome WebDriver instance
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./chrome-whatsapp-profile")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://web.whatsapp.com")

    print("Scan the QR code in the browser (only first time) ...")
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        )
    )
    print("WhatsApp Web loaded.")
    return driver


def send_message_to_group(driver, group_name, message):
    """
    Sends a message to a specified WhatsApp group.
    
    Args:
        driver: Chrome WebDriver instance
        group_name: Name of the WhatsApp group
        message: Message text to send
    """
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        )
    )

    search_box.click()
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)

    msg_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//footer//div[@contenteditable="true"]')
        )
    )

    msg_box.click()
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)
    print(f"Sent message to group: {group_name} at {datetime.now()}")


def main():
    """
    Main function that runs the scheduled message sender.
    Sends a message every day at the specified time.
    """
    driver = open_whatsapp()

    target_hour, target_minute = map(int, SEND_TIME.split(":"))
    sent_today = False

    print(f"Will send every day at {SEND_TIME}.")

    while True:
        now = datetime.now()

        if (
            now.hour == target_hour and
            now.minute == target_minute and
            not sent_today
        ):
            try:
                send_message_to_group(driver, GROUP_NAME, MESSAGE)
                sent_today = True
            except Exception as e:
                print("Error while sending message:", e)

        if now.hour == 0 and now.minute == 0:
            sent_today = False

        time.sleep(20)


if __name__ == "__main__":
    main()
