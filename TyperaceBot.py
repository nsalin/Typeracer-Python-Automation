import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class TyperaceBot:
    def __init__(self):
        # Opening the Typeracer website
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://play.typeracer.com/")
        time.sleep(2)


        # Clicking on the "Enter a typing race"
        enter_race = self.driver.find_element_by_xpath("//a[text()='Enter a typing race']")
        enter_race.click()

        # Wait till the countdown is zero and start typing the text in the answer box
        time.sleep(5)
        while True:
            try:
                countdown_box = self.driver.find_element_by_css_selector("[class='trafficLight']")
                if countdown_box.is_displayed():
                    time.sleep(1)
            except (NoSuchElementException, StaleElementReferenceException):
                break

        # Get the text from the website
        full_text = self.driver.find_element_by_css_selector(
            "table[class='gameView'] table[class='inputPanel'] tbody tr:nth-child(1) tbody tr div").text
        print(full_text)

        # Start typing in the answer box
        answer_box = self.driver.find_element_by_css_selector(
            "table[class='gameView'] table[class='inputPanel'] input[class='txtInput']")
        answer_box.click()
        print('click')
        for words in full_text:
            for letter in words:
                if (letter == ""):
                    answer_box.send_keys(Keys.SPACE)
                else:
                    answer_box.send_keys(letter)
                    print(letter)


my_typing_bot = TyperaceBot()
