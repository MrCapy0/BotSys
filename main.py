import time
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

profile_path = os.getenv("FIREFOX_PROFILE_DIRECTORY")
firefox_path = os.getenv("FIREFOX_EXECUTABLE_DIRECTORY")

if firefox_path == '':
    firefox_path = None

service = webdriver.FirefoxService(executable_path=firefox_path)
options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
driver = webdriver.Firefox(options=options)

driver.get("https://www.youtube.com")


time.sleep(100)