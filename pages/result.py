"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    SEARCH_INPUT = (By.ID, "search_form_input")

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title
