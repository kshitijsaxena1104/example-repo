from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time


def UXO11OnPremDatageneration():
    # UXOURL1 APP URL FOR UXO PROD ENV
    uxourl1 = 'https://staging-xo.korebots.com/xo-webclient/273f5bd35ae342f79475875a1606f251f7e38680e97d437aaf148bfa04297773sta5?lang=en'
    driver = webdriver.Chrome()
    driver.get(uxourl1)
    time.sleep(9)
    InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Type a message"]')
    time.sleep(9)
    InputBox.send_keys("Cheat lang en", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("ContentVariableValidation", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Dialog Script Node", Keys.ENTER)
    time.sleep(9)
    # KG-Can you please display Get time service url from Environment variables?
    InputBox.send_keys('Can you please display Get time service url from Environment variables?', Keys.ENTER)
    time.sleep(9)
# WebhookNodeValidation-
    InputBox.send_keys('WebhookNodeValidation', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys('WebhookSync', Keys.ENTER)
    time.sleep(9)
    # npssurvey with 0 rating
    InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("0", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Python selenium feedback", Keys.ENTER)

    # npssurvey with 5 rating
    InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("0", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # npssurvey with 9 rating
    InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("9", Keys.ENTER)
    time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # CSAT -Highly unsatisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Highly unsatisfied", Keys.ENTER)
    time.sleep(9)

    # CSAT - unsatisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("unsatisfied", Keys.ENTER)
    time.sleep(9)

    # CSAT - Average
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Average", Keys.ENTER)
    time.sleep(9)

    # CSAT - Satisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Satisfied", Keys.ENTER)
    time.sleep(9)

    # CSAT - Highly Satisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Highly Satisfied", Keys.ENTER)
    time.sleep(9)

    # LikeDislike - Extremely likely
    InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Extremely likely", Keys.ENTER)
    time.sleep(9)

    # LikeDislike - Extremely Unlikely
    InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Extremely Unlikely", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Python selenium disliked the task", Keys.ENTER)
    time.sleep(9)
    # Small talk
    InputBox.send_keys("HEY", Keys.ENTER)
    time.sleep(9)

    # Discard task-
    InputBox.send_keys("Discard task", Keys.ENTER)
    time.sleep(9)

    # ContextValuesClearingValidation
    InputBox.send_keys("ContextValuesClearingValidation", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Google",Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Google", Keys.ENTER)
    time.sleep(9)
    # AttachmentEntityValidation
    InputBox.send_keys("AttachmentEntityValidation", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)

    # AgentTransferEventforBotkit
    InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)



def xo10prodregionstest():
    url1 = 'https://staging-bots.korebots.com/webclient/dd13d41ba27b4ac69461abb60ac8f831f4cb04a466c4469cb4d50316a8b199a5steb'
    driver = webdriver.Chrome()
    driver.get(url1)
    time.sleep(9)
    InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Message..."]')
    time.sleep(9)
    InputBox.send_keys("Cheat lang en", Keys.ENTER)
    time.sleep(9)
    # assert 'Language switched to English1'
    # ContentVariableValidation
    InputBox.send_keys("ContentVariableValidation", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Dialog Script Node", Keys.ENTER)
    time.sleep(9)
    # assert 'This message is from content variables'
    # KG-Can you please display Get time service url from Environment variables?
    InputBox.send_keys('Can you please display Get time service url from Environment variables?', Keys.ENTER)
    time.sleep(9)
    assert 'https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata'
    # WebhookNodeValidation-
    InputBox.send_keys('WebhookNodeValidation', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys('WebhookSync', Keys.ENTER)
    time.sleep(9)
    # npssurvey with 0 rating
    InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("0", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Python selenium feedback", Keys.ENTER)

    # npssurvey with 5 rating
    InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("0", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # npssurvey with 9 rating
    InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("9", Keys.ENTER)
    time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # CSAT -Highly unsatisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Highly unsatisfied", Keys.ENTER)
    time.sleep(9)

    # CSAT - unsatisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("unsatisfied", Keys.ENTER)
    time.sleep(9)

    # CSAT - Average
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Average", Keys.ENTER)
    time.sleep(9)

    # CSAT - Satisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Satisfied", Keys.ENTER)
    time.sleep(9)

    # CSAT - Highly Satisfied
    InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Highly Satisfied", Keys.ENTER)
    time.sleep(9)

    # LikeDislike - Extremely likely
    InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Extremely likely", Keys.ENTER)
    time.sleep(9)

    # LikeDislike - Extremely Unlikely
    InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Extremely Unlikely", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Python selenium disliked the task", Keys.ENTER)
    time.sleep(9)
    # Small talk
    InputBox.send_keys("HEY", Keys.ENTER)
    time.sleep(9)

    # Discard task-
    InputBox.send_keys("Discard task", Keys.ENTER)
    time.sleep(9)

    # ContextValuesClearingValidation
    InputBox.send_keys("ContextValuesClearingValidation", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Google", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("yes", Keys.ENTER)
    time.sleep(9)
    # AgentTransferEventforBotkit
    InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)

    InputBox.send_keys('KoreDebuggerValdiation', Keys.ENTER)
    time.sleep(9)
    # InputBox.send_keys("0", Keys.ENTER)
    # time.sleep(9)

    InputBox.send_keys('cheat lang en', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys('contentvariablevalidation', Keys.ENTER)
    InputBox.send_keys('Dialog script node', Keys.ENTER)
    time.sleep(9)

    InputBox.send_keys('EntityNodeConnectionsValidation', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys('Entity', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys('Exists', Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys('Hyderabad', Keys.ENTER)
    time.sleep(9)


UXO11OnPremDatageneration=threading.Thread(target=UXO11OnPremDatageneration)
UXO11OnPremDatageneration.start()

xo10prodregionstest=threading.Thread(target=xo10prodregionstest)
xo10prodregionstest.start()
