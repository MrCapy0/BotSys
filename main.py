import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from pynput.mouse import Button, Controller
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

driver.fullscreen_window()

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

    # if is_first_play:
    #     first_play_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Button-sc-qlcn5g-0.iPAIAO.e-9541-button-primary.e-9541-button")))
    #     first_play_button.click()
    #     is_first_play = False

    # play_button = driver.find_element(By.CSS_SELECTOR, ".Button-sc-qlcn5g-0.iPAIAO.e-9541-button-primary.e-9541-button")
    # next_button = driver.find_element(By.CSS_SELECTOR, ".Button-sc-1dqy6lx-0.ijaVit.e-9541-overflow-wrap-anywhere")

    # random_action = random.randint(0, 10)
    # if random_action < 5:
    #     play_button.click()
    # else:
    #     next_button.click()
    #     time.sleep(5)
    #     play_button.click()

    #     print("click")

    time.sleep(1)
    mouse_position_x = 0.5 * screen_width
    mouse_position_y = 0.95 * screen_height

    pyautogui.moveTo(mouse_position_x, mouse_position_y)
    

    # mouse_position_x, mouse_position_y = 0, 0
    # mouse_position_y /= screen_height
    # mouse_position_x /= screen_width
    # print(mouse_position_x, mouse_position_y)
    # print('-----')

    pyautogui.click()
    time.sleep(random.uniform(5.0, 10.0))

