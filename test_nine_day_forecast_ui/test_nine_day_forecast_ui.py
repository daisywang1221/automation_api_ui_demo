import time

from datetime import datetime, timedelta
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "SM-G9810",
    "appPackage": "hko.MyObservatory_v1_0",
    "appActivity": "hko.homepage3.HomepageActivity",
    "noReset": True,
    "appWaitForLaunch": True,
    "ignoreHiddenApiPolicyError": True
}

# 连接 Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

def test_9_day_forecast():
    # click "navigation" button
    driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageButton").click()
    time.sleep(1)

    # click “Forecast & Warnings services” menu
    driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/header_layout").click()
    driver.implicitly_wait(10)

    # click "9-Day Forecast" menu
    nine_day_forecast = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="9-Day Forecast"]')
    nine_day_forecast.click()

    # check if "9-Day Forecast " is displayed
    assert driver.find_element(AppiumBy.XPATH,'//*[@text="9-Day Forecast"]').is_displayed()
    # check if "Forecast for the next 9 days" text is displayed
    forecast_text: WebElement = driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit")
    assert forecast_text.text != ""
    # check if "Forecast for the next 9 days" table is displayed
    forecast_table: WebElement = driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/mainAppSevenDayView")
    assert forecast_table.is_displayed()

    # check the "Date" column displays the current date and the next date
    nine_day_forecast_date = driver.find_elements(AppiumBy.ID, "hko.MyObservatory_v1_0:id/sevenday_forecast_date")
    current_date = datetime.now().strftime("%d %b")
    assert nine_day_forecast_date[0].text == current_date
    assert nine_day_forecast_date[1].text == (datetime.now() + timedelta(days=1)).strftime("%d %b")

    scroll_to_bottom()
    nine_day_forecast_date = driver.find_elements(AppiumBy.ID, "hko.MyObservatory_v1_0:id/sevenday_forecast_date")
    assert nine_day_forecast_date[-1].text == (datetime.now() + timedelta(days=8)).strftime("%d %b")

    driver.quit()

def scroll_to_bottom():
    # get window size
    window_size = driver.get_window_size()
    start_x = window_size['width'] / 2  # start from the center of the screen
    start_y = window_size['height'] * 0.9  # start from 90% of the screen
    end_y = window_size['height'] * 0.1  # scroll to 10% of the screen

    driver.swipe(start_x, start_y, start_x, end_y, duration=1000)
    time.sleep(2)

if __name__ == '__main__':
    test_9_day_forecast()