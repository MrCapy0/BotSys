import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import screeninfo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui


load_dotenv()

profile_path = os.getenv("FIREFOX_PROFILE_DIRECTORY")
binary_location = os.getenv("FIREFOX_EXECUTABLE_DIRECTORY")

if binary_location == '':
    binary_location = None

options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
options.binary_location = binary_location
driver = webdriver.Firefox(options=options)

time.sleep(5)

driver.get("https://open.spotify.com/collection/tracks")

time.sleep(5)

screen = screeninfo.get_monitors()[0]  
screen_width = screen.width
screen_height = screen.height

time.sleep(5)

is_first_play = True


time.sleep(3)

while True:

    if driver.current_url != 'https://open.spotify.com/collection/tracks':
        time.sleep(4)

        is_first_play = True
        driver.get("https://open.spotify.com/collection/tracks")
    else:

        random_action = random.randint(0, 10)
        if random_action < 5:
            pyautogui.press('space')
            print('pause/continue')
        else:
            pyautogui.press('right')
            print('skip')

    time.sleep(random.uniform(5.0, 10.0))

