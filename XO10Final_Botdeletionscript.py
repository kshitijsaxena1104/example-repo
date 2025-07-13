import threading
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Login to the staging env
def login_and_deleteBotswithQAAutotext():
    driver = webdriver.Chrome()
    try:
        env1 ='https://bots.kore.ai/botbuilder'
        env2='https://staging-bots.korebots.com/botbuilder'
        env3='https://de-bots.kore.ai/botbuilder'
        env4='https://jp-bots.kore.ai/botbuilder/login'
        env5='https://preprod-bots.korebots.com/botbuilder'
        env6='https://ebay-xo.kore.ai/botbuilder'
        usernamevalue ="uiautomation@vomoto.com"
        passwordvalue ="Autokore@123456"
        usernamevalue1='kfoldactn@spicysoda.com'
        passwordvalue1='Kore@12345678'
        driver.get(env2) #Just add env1 or env2 based on the env u want to delete the bot
        driver.implicitly_wait(170)
        driver.maximize_window()
        username = driver.find_element(by=By.XPATH, value='//input[@name="emailPhone"]')
        username.send_keys(usernamevalue)
        username.send_keys(Keys.ENTER)
        password = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
        password.send_keys(passwordvalue)
        password.send_keys(Keys.ENTER)
        time.sleep(20)

        while True:
            Searchbot = driver.find_element(by=By.XPATH, value='//span/input[@placeholder="Search"]')
            # Search for bots with QAAuto text
            text1 ='QAAuto_'
            text2='Advance'
            text3='Sentiment'
            text4='BatchTesting'
            text5='StandardBotActions'
            text6='BotVersions'
            text7='Password'
            text8="UBDesign"
            #botnames={'QAAuto','Advance','Sentiment','BatchTesting'}
            #for botname in botnames:
            Searchbot.send_keys(text1) #Just change the text in this line text1,text2,text3,text4 based on the bot name to delete the bot
            Nobotsfoundtext = driver.find_element(By.XPATH, value='//div[text()="No search results found"]')
            if Nobotsfoundtext.is_displayed():
                print('There are no bots matching the string')
                driver.quit()
            else:
                # Click on First entry
                SearchedEntry = driver.find_element(by=By.XPATH, value='(//div[@class="col-sm-4 ng-scope"])[1]')
                SearchedEntry.click()
                time.sleep(9)
                # Navigate to the Deploy section > Delete bot
                Deploysection = driver.find_element(by=By.XPATH, value="//li[@class='tabDiv ng-scope']//*[text()='Deploy']")
                Deploysection.click()
                time.sleep(6)
                BotManagement_Option = driver.find_element(by=By.XPATH, value="//div[@id='menuHeader_botManagement']")
                BotManagement_Option.click()
                time.sleep(6)
                DeleteBot_Option = driver.find_element(by=By.ID, value='popOverEvent_botManagementdeleteBot')
                DeleteBot_Option.is_displayed()
                DeleteBot_Option.click()
                time.sleep(6)
                Bot_Delete_Ok = driver.find_element(by=By.XPATH, value="// *[text() = 'OK']")
                Bot_Delete_Ok.click()
                time.sleep(6)
                driver.refresh()
                time.sleep(70)

                print('the bots matching the string are deleted successfully')
    except Exception as e:
        # Add log statements for possibly errors/exceptions and how to handle them
        traceback.print_exc()
        driver.quit()
    finally:
        driver.quit()
        # handles cases where all operations are done but the webdriver still is active.


# def login_and_deleteBotswithAdvancedNLU():
#     driver = webdriver.Chrome()
#     try:
#         driver.get('https://bots.kore.ai/botbuilder/')
#         driver.implicitly_wait(19)
#         driver.maximize_window()
#         username = driver.find_element(by=By.XPATH, value='//input[@name="emailPhone"]')
#         username.send_keys('uiautomation@vomoto.com')
#         username.send_keys(Keys.ENTER)
#         password = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
#         password.send_keys("Autokore@123456")
#         password.send_keys(Keys.ENTER)
#         time.sleep(20)
#
#         while True:
#             Searchbot = driver.find_element(by=By.XPATH, value='//span/input[@placeholder="Search"]')
#             # Search for bots with QAAuto text
#             Searchbot.send_keys('AdvancedNLU')
#             Nobotsfoundtext = driver.find_element(By.XPATH, value='//div[text()="No search results found"]')
#             if Nobotsfoundtext.is_displayed():
#                 print('There are no bots matching the string')
#                 driver.quit()
#             else:
#                 # Click on First entry
#                 SearchedEntry = driver.find_element(by=By.XPATH, value='(//div[@class="col-sm-4 ng-scope"])[1]')
#                 SearchedEntry.click()
#                 time.sleep(9)
#                 # Navigate to the Deploy section > Delete bot
#                 Deploysection = driver.find_element(by=By.XPATH,
#                                                     value="//li[@class='tabDiv ng-scope']//*[text()='Deploy']")
#                 Deploysection.click()
#                 time.sleep(6)
#                 BotManagement_Option = driver.find_element(by=By.XPATH, value="//div[@id='menuHeader_botManagement']")
#                 BotManagement_Option.click()
#                 time.sleep(6)
#                 DeleteBot_Option = driver.find_element(by=By.ID, value='popOverEvent_botManagementdeleteBot')
#                 DeleteBot_Option.is_displayed()
#                 DeleteBot_Option.click()
#                 time.sleep(6)
#                 Bot_Delete_Ok = driver.find_element(by=By.XPATH, value="// *[text() = 'OK']")
#                 Bot_Delete_Ok.click()
#                 time.sleep(6)
#                 driver.refresh()
#                 time.sleep(9)
#
#                 print('the bots matching the string are deleted successfully')
#     except Exception as e:
#         # Add log statements for possibly errors/exceptions and how to handle them
#         traceback.print_exc()
#         driver.quit()
#     finally:
#         driver.quit()
#         # handles cases where all operations are done but the webdriver still is active.


if __name__ == "__main__":
    login_and_deleteBotswithQAAutotext()
