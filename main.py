import time
import os
import random
import screeninfo

import pyautogui
import webbrowser


time.sleep(5)

webbrowser.open("https://open.spotify.com/collection/tracks")

time.sleep(5)


pyautogui.press('f11')

screen = screeninfo.get_monitors()[0]  
screen_width = screen.width
screen_height = screen.height

time.sleep(5)

is_first_play = True



time.sleep(3)

while True:

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

