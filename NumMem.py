from selenium import webdriver
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

break_program = False

def on_press(key):
    global break_program
    if key == keyboard.Key.f13:
        break_program = True

browser = webdriver.Firefox()
browser.get("https://humanbenchmark.com/tests/number-memory")

start_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "css-de05nr.e19owgy710"))
)

with keyboard.Listener(on_press=on_press) as listener:
    start_button.click()
    wait_time = 5
    while not break_program:
        try:
            number_element = WebDriverWait(browser, wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, "big-number"))
            )
            number = number_element.text
        except TimeoutException:
            print("Nunmber not found")
            break

        try:
            input_field = WebDriverWait(browser, wait_time).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @pattern='[0-9]*']"))
            )
        except TimeoutException:
            print("Input field not found")
            break
        input_field.send_keys(number)

        try: 
            submit = WebDriverWait(browser, wait_time).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "css-de05nr.e19owgy710"))
            )
        except TimeoutException:
            print("Submit button not found")
            break
        submit.click()

        try: 
            next_button = WebDriverWait(browser, wait_time).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "css-de05nr.e19owgy710"))
            )
        except TimeoutException:
            print("Next button not found")
            break
        next_button.click()

        wait_time += 1

listener.join()
print("Program ended")