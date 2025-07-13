import time
import traceback

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_and_deleteApps():
    driver = webdriver.Chrome()
    try:
        env1 = 'https://staging-xo.korebots.com/builder/home'
        env2 = 'https://platform.kore.ai/auth/login?return_to=https:%2F%2Fplatform.kore.ai%2Fbuilder'
        env3='https://ind-platform.kore.ai/auth/login?return_to=https:%2F%2Find-platform.kore.ai%2Fbuilder'
        usernamevalue = "autostageone@vomoto.com"
        passwordvalue = "Care@1104"
        # usernamevalue="autostageone@vomoto.com"
        # passwordvalue="Martin@@1104"

        driver.get(env1)
        driver.implicitly_wait(20)
        driver.maximize_window()

        # Login
        username = driver.find_element(by=By.XPATH, value='//input[@name="emailPhone"]')
        username.send_keys(usernamevalue)
        username.send_keys(Keys.ENTER)
        time.sleep(2)

        password = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
        password.send_keys(passwordvalue)
        password.send_keys(Keys.ENTER)
        time.sleep(20)

        while True:
            # Search for app with specific text
            Searchbot = driver.find_element(by=By.XPATH, value='//input[@placeholder="Search"]')
            text1 = 'QAAuto_'  # change this text to match app to delete
            Searchbot.clear()
            Searchbot.send_keys(text1)

            time.sleep(4)

            try:
                Nobotsfoundtext = driver.find_element(By.XPATH, value='//h4[text()="No Apps found"]')
                if Nobotsfoundtext.is_displayed():
                    print('There are no Apps matching the string')
                    break
            except:
                pass  # No "No Apps found" message; continue

            # Wait for the hover element and click it
            hover_xpath = '//body[1]/app-root[1]/unified-app-home[1]/div[1]/main[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/kr-icon[1]/i[1]'
            hover_element = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, hover_xpath))
            )

            actions = ActionChains(driver)
            actions.move_to_element(hover_element).click().perform()
            time.sleep(3)

            # Click on App Settings
            AppSettings = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='appsettings']"))
            )
            AppSettings.click()
            time.sleep(3)

            # Click on Delete option
            DeleteApp_Option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='deletebot']"))
            )
            DeleteApp_Option.click()
            time.sleep(2)

            # Confirm deletion
            ConfirmOption = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Confirm"]'))
            )
            ConfirmOption.click()
            time.sleep(6)

            # Refresh to update bot list
            driver.refresh()
            time.sleep(10)

            print('App matching the string was deleted successfully')

    except Exception as e:
        traceback.print_exc()
    finally:
        driver.quit()


if __name__ == "__main__":
    login_and_deleteApps()
