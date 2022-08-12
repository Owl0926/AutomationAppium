from time import sleep

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

appium_service = AppiumService()
appium_service.start()
desired_caps = {
  "appium:deviceName": "Pixel 5 API 30",
  "browserName": "Chrome",
  "platformName": "Android",
  "appium:automationName": "UIAutomator2"

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.get("https://www.amazon.com")

sleep(5)
driver.quit()

appium_service.stop()