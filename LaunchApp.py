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
# appium_service = AppiumService()
# appium_service.start()
desired_caps = {'platformName': 'Android',
                'platformVersion': '11',
                'deviceName': 'Pixel 4 API 30',
                'automationName': 'UiAutomator2',
                'app': (
                    'C:\\Users\\dominik.sowa\\Documents\\Code2Lead\\Android_Demo_App.apk'),
                'appPackage': 'com.code2lead.kwad',
                'appActivity': 'com.code2lead.kwad.MainActivity', }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


def back_to_homepage():
    driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate "
                                        "up']").click()
    sleep(1)


def enter_some_value():
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.code2lead.kwad:id/Et1")))
    some_text = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1")
    some_text.send_keys("Hello Appium")
    btn_text = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
    btn_text.click()
    confirm_preview = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv1")

    assert some_text.text == confirm_preview.text
    print("Enter value - Done")
    back_to_homepage()
def contact_us():
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ContactUs")
    ele_id.click()
    sleep(1)
    name = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et2")
    email = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et3")
    address = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et6")
    mobile = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et7")
    submit = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn2")
    name.send_keys("Dominik Jaro")
    email.send_keys("ds@o2.pl")
    address.send_keys("Chopin 2, Green Mountain 65-213")
    mobile.send_keys("0123456789")
    submit.click()
    driver.hide_keyboard()
    check_name = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv2")
    check_email = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv7")
    check_address = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv5")
    check_mobile = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv6")
    assert name.text == check_name.text.split(": ")[1] \
           and email.text == check_email.text.split(": ")[1] \
           and address.text == check_address.text.split(": ")[1] \
           and mobile.text == check_mobile.text.split(": ")[1]
    print("Contact us - DONE")
    back_to_homepage()
def scroll_view():
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Btn3")
    el7.click()
    sleep(1)
    driver.swipe(1040, 2080,1040,280)
    el8 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.view"
                                                       ".ViewGroup/android.widget.FrameLayout["
                                                       "2]/android.widget.ScrollView/android.widget.LinearLayout"
                                                       "/android.widget.Button[10]")
    el8.click()
    sleep(1)
    el9 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
    el9.click()
    sleep(1)
    el10 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout"
                                                        "/android.widget.LinearLayout/android"
                                                        ".widget.FrameLayout/android.view.ViewGroup"
                                                        "/android.widget.FrameLayout["
                                                        "2]/android.widget.ScrollView/android"
                                                        ".widget.LinearLayout/android.widget"
                                                        ".Button[9]")
    el10.click()
    sleep(1)
    el11 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el11.click()
    sleep(1)
    assert el7.is_displayed()
    print("ScrollView - DONE")
def ne():
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Btn4")
    el3.click()
    sleep(1)
    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sport")
    el4.click()
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Movie")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
    el6.click()
    sleep(1)
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Btn5")
    el7.click()
    sleep(5)
    el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Btn6")
    el8.click()
    sleep(1)
    el9 = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Et5")
    el9.click()

    el9.send_keys("admin123")
    el10 = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Et4")
    el10.click()
    el10.send_keys("admin@gmail.com")
    el11 = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Btn3")
    el11.click()
    sleep(1)
    el12 = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Edt_admin")
    el12.click()
    el12.send_keys("admin123")
    el13 = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Btn_admin_sub")
    el13.click()
    el14 = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Tv_admin")
    assert el14.text == el12.text
    back_to_homepage()
    back_to_homepage()
    # driver.back()
    print("Ne - DONE")
def long_click():
    ele = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/LongClick")
    ele.click()
    sleep(2)
    TouchAction(driver).long_press(ele).perform()
    sleep(1)
    email_s = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/et_email")
    email_s.send_keys("Lopatologicznie@chybaslowotworstwo.com")
    driver.find_element(AppiumBy.ID, "android:id/button1").click()
    sleep(1)
    print("LongClick - DONE")
def time():
    driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Time").click()
    sleep(1)
    driver.find_element(AppiumBy.ID, "android:id/am_label").click()
    driver.find_element(AppiumBy.ID, "android:id/hours").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.RadialTimePickerView"
                                        ".RadialPickerTouchHelper[@content-desc='9']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.RadialTimePickerView"
                                        ".RadialPickerTouchHelper[@content-desc='40']").click()
    sleep(2)
    driver.back()
    print("after back")
    print("Time - DONE")
def date():
    driver.swipe(900,1900,900,1000)
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Btn9")
    el1.click()
    sleep(1)
    el2 = driver.find_element(by=AppiumBy.ID, value="android:id/date_picker_header_year")
    el2.click()
    sleep(1)
    el3 = driver.find_element(by=AppiumBy.XPATH,
                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                                    "2]/android.widget.LinearLayout/android.widget.DatePicker/android.widget"
                                    ".LinearLayout/android.widget.ScrollView/android.widget.ViewAnimator/android"
                                    ".widget.ListView/android.widget.TextView[6]")
    el3.click()
    sleep(1)
    el4 = driver.find_element(by=AppiumBy.ID, value="android:id/date_picker_header_date")
    el4.click()
    sleep(1)
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next month")
    el5.click()
    sleep(1)
    el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="19 September 2025")
    el6.click()
    assert el6.text == "19"
    driver.back()
    print("date - DONE")

def drag_n_drop():
    driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/drag").click()
    sleep(1)
    l3 = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/layout3")
    l2 = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/layout2")
    drag_button = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/btnDrag")
    drag_text = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/lbl")
    drag_img = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/ingvw")
    TouchAction(driver).long_press(drag_button).wait(500).move_to(l2).release().perform()
    TouchAction(driver).long_press(drag_text).wait(500).move_to(l2).release().perform()
    TouchAction(driver).long_press(drag_img).wait(500).move_to(l2).release().perform()
    TouchAction(driver).long_press(drag_button).wait(500).move_to(l3).release().perform()
    TouchAction(driver).long_press(drag_text).wait(500).move_to(l3).release().perform()
    TouchAction(driver).long_press(drag_img).wait(500).move_to(l3).release().perform()
    print("Dragndrop - DONE")
# enter_some_value()
# contact_us()
scroll_view()
# ne()
# long_click()
# time()
# date()
# drag_n_drop()

driver.quit()
# appium_service.stop()

print("END")
