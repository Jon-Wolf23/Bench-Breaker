from selenium import webdriver
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


break_program = False
scores = []

def on_press(key):
    global break_program
    if key == keyboard.Key.f13:
        break_program = True

browser = webdriver.Firefox()
browser.get("https://humanbenchmark.com/tests/reactiontime")



with keyboard.Listener(on_press=on_press) as listener:

    while not break_program:
        try:
            start_text = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-test='true']"))
            )
            start_text.click()
        except TimeoutException as e:
            print(e)
            break
        try:
            click_text = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[not(@class) and text()='Click!']"))
            )
            click_text.click()
        except TimeoutException as e:
            print(e)
            break

        try:
            score_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ms')]"))
            )
            score_text = score_element.text.split(" ")[0]
            scores.append(int(score_text))
            print(scores[-1])
        except TimeoutException as e:
            print(e)
            break

        try:
            restart_text = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//h2[text()='Click to keep going']"))
            )
            restart_text.click()
        except TimeoutException as e:
            print(e)
            break

    listener.join()
    print('\n')
    print('\n')
    print(f'Highest score: {max(scores)}')
    print(f'Lowest score: {min(scores)}')
    print(f'Average score: {sum(scores) / len(scores)}')