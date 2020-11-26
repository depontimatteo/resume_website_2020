import pytest
import time
import logging
from selenium import webdriver

@pytest.mark.usefixtures("browser")
class TestBrowser:

    def test_browser(self):
        logger = self.logging.getLogger()
        self.driver.refresh()
        self.driver.find_element_by_xpath("//a[contains(text(),'Esperienza')]").click()
        textMatch = self.driver.find_element_by_xpath("//h2[contains(text(),'Esperienza professionale')]").text
        logger.info("Text received from application is "+textMatch)
        assert ("ESPERIENZA PROFESSIONALE" in textMatch)