from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import os
class Scrape:

    def __init__(self, game_link):
        self.file_path = None
        self.game_link = game_link
        self.scrape()

    def scrape(self):
        # Set the download directory
        download_dir = "/Users/wuuchriss/Downloads/"

        # Create Chrome options
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

        # Initialize the Chrome driver with options
        driver = webdriver.Chrome(options=chrome_options)

        assert "pokernow.club/games" in self.game_link

        actions = ActionChains(driver)


        """try:
            driver.get(game_link)
            
            log_ledger_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.show-log-button.small-button.dark-gray"))
            )
            log_ledger_button.click()

            download_full_log_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.green-2.small-button.log-download-button"))
            )
            
            # List files in the download directory before downloading
            before_download = set(os.listdir(download_dir))
            
            download_full_log_button.click()

            # Wait for the iframe containing the reCAPTCHA checkbox to be present
            recaptcha_iframe = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
            )
            
            # Switch to the reCAPTCHA iframe
            driver.switch_to.frame(recaptcha_iframe)
            
            # Wait for the reCAPTCHA checkbox to be clickable
            recaptcha_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox"))
            )
            
            # Click the reCAPTCHA checkbox using JavaScript
            driver.execute_script("arguments[0].click();", recaptcha_checkbox)
            
            # Switch back to the main content
            driver.switch_to.default_content() """
        try:
            driver.get(self.game_link)
            
            # Random delay to mimic human reading time
            time.sleep(random.uniform(.5, 1))
            
            log_ledger_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.show-log-button.small-button.dark-gray"))
            )
            actions.move_to_element(log_ledger_button).perform()
            time.sleep(random.uniform(.5, 1))
            log_ledger_button.click()
            
            # Random delay
            time.sleep(random.uniform(.5, 1))

            download_full_log_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.green-2.small-button.log-download-button"))
            )
            
            # List files in the download directory before downloading
            before_download = set(os.listdir(download_dir))
            
            actions.move_to_element(download_full_log_button).perform()
            time.sleep(random.uniform(.5, 1))
            download_full_log_button.click()

            # Random delay
            time.sleep(random.uniform(.5, 1))

            # Wait for the iframe containing the reCAPTCHA checkbox to be present
            recaptcha_iframe = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
            )
            
            # Switch to the reCAPTCHA iframe
            driver.switch_to.frame(recaptcha_iframe)
            
            # Wait for the reCAPTCHA checkbox to be clickable
            recaptcha_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox"))
            )
            
            actions.move_to_element(recaptcha_checkbox).perform()
            time.sleep(random.uniform(.5, 1))
            recaptcha_checkbox.click()

            # Switch back to the main content
            driver.switch_to.default_content()
            
            # Wait for the file to be downloaded by checking for new files
            while True:
                after_download = set(os.listdir(download_dir))
                new_files = after_download - before_download
                if len(new_files) == 1:
                    downloaded_file = new_files.pop()
                    if not downloaded_file.endswith('.crdownload'):
                        break
                time.sleep(1)
            file_path = os.path.join(download_dir, downloaded_file)
            self.file_path = file_path
            print(f"Downloaded file path: {file_path}")


        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            driver.quit()