import time
import os
import random
from selenium import webdriver
from dotenv import load_dotenv
from pynput.mouse import Button, Controller
import screeninfo

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

mouse = Controller()
#mouse.position = (500, 500)  # Define a posição do mouse para (x=500, y=500)
#mouse.click(Button.left)

driver.fullscreen_window()

screen = screeninfo.get_monitors()[0]  
screen_width = screen.width
screen_height = screen.height
mouse_position_x, mouse_position_y = mouse.position
mouse_position_y /= screen_height
mouse_position_x /= screen_width

time.sleep(5)

while True:

    mouse_position_x, mouse_position_y = mouse.position
    mouse_position_y /= screen_height
    mouse_position_x /= screen_width
    print(mouse_position_x, mouse_position_y)
    print (screen_width, screen_height)

    mouse_position_x = 0.5 * screen_width
    mouse_position_y = 0.95 * screen_height
    mouse.position = (mouse_position_x, mouse_position_y)

    mouse_position_x, mouse_position_y = mouse.position
    mouse_position_y /= screen_height
    mouse_position_x /= screen_width
    print(mouse_position_x, mouse_position_y)
    print('-----')

    mouse.click(Button.left)
    time.sleep(random.randrange(10.0, 100.0))

