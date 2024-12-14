from selenium import webdriver
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

break_program = False
sequence = []
initial_state = ["square", "square", "square", "square", "square", "square", "square", "square", "square"]
level = 0

def on_press(key):
    global break_program
    if key == keyboard.Key.f13:
        break_program = True

browser = webdriver.Firefox()
browser.get("https://humanbenchmark.com/tests/sequence")

start_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "css-de05nr e19owgy710"))
)

with keyboard.Listener(on_press=on_press) as listener:
    start_button.click()
    while not break_program:
        sequence.clear()
        try:
            level += 1
            for i in range(level):
                current_active = WebDriverWait(browser, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='square active']" | "//div[@class='square']"))
                )
                