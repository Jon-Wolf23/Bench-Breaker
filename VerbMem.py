from selenium import webdriver
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

break_program = False
word_list = []

def on_press(key):
    global break_program
    if key == keyboard.Key.f13:
        break_program = True

browser = webdriver.Firefox()
browser.get("https://humanbenchmark.com/tests/verbal-memory")

start_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "css-de05nr.e19owgy710"))
)

with keyboard.Listener(on_press=on_press) as listener:
    start_button.click()

    while not break_program:
        try:
            word_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "word"))
            )
            word = word_element.text
            if word in word_list:
                print("SEEN")
                seen_button = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='SEEN']"))
                )
                seen_button.click()
            else:
                word_list.append(word)
                print("NEW")
                new_button = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='NEW']"))
                )
                new_button.click()
        except TimeoutException:
            print("Slow down checks")
            break

listener.join()
print("Program Ended")