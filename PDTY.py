from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time


def datageneration():
    # Prod -UB XO10 URL
    #url1='https://bots.kore.ai/webclient/c1ee72ede3fe417eb318caedb0c7251a009741409e10487aad5228992cf8e7cbst86'
    url1 = 'https://mashreq-bots.korebots.com/webclient/d7459eb3b7634a499f2b8c02a7c21bad3a5c834f60794fa8bdb39ec14fec2721std2'
    driver = webdriver.Chrome()
    driver.get(url1)
    time.sleep(9)
    InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Message..."]')
    time.sleep(9)
    InputBox.send_keys("Cheat lang en", Keys.ENTER)
    time.sleep(9)
    #assert 'Language switched to English1'
    # ContentVariableValidation
    InputBox.send_keys("ContentVariableValidation", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Dialog Script Node", Keys.ENTER)
    time.sleep(9)
    #assert 'This message is from content variables'
    # KG-Can you please display Get time service url from Environment variables?
    InputBox.send_keys('Can you please display Get time service url from Environment variables?', Keys.ENTER)
    time.sleep(9)
   # assert 'https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata'
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
    # AgentTransferEventforBotkit
    InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)

    # Prod -std bot xo10 URL
    url2 = 'https://bots.kore.ai/webclient/0e07366caf994328be0a427c50c44904934e96923c2b4f428c927a3d217a9799st87'
    driver.get(url2)
    time.sleep(9)
    InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Message..."]')
    time.sleep(9)
    InputBox.send_keys("Cheat lang en", Keys.ENTER)
    time.sleep(9)
    # ContentVariableValidation
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
    InputBox.send_keys("Google", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("Google", Keys.ENTER)
    time.sleep(9)
    # AgentTransferEventforBotkit
    InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    time.sleep(9)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(9)

    InputBox.send_keys("AttachmentEntityValidation", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)
    InputBox.send_keys("test", Keys.ENTER)
    time.sleep(5)

    # # Staging UBbot xo10 url
    # url3 = 'https://staging-bots.korebots.com/webclient/67f62984207a4363b1d1fa90e180ec2ef269be8cf44a4e5e8ce73c3f8cbefd5bst4d'
    # driver.get(url3)
    # time.sleep(7)
    # InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Message..."]')
    # InputBox.send_keys("Cheat lang en", Keys.ENTER)
    # time.sleep(9)
    # # ContentVariableValidation
    # InputBox.send_keys("ContentVariableValidation", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Dialog Script Node", Keys.ENTER)
    # time.sleep(9)
    # # KG-Can you please display Get time service url from Environment variables?
    # InputBox.send_keys('Can you please display Get time service url from Environment variables?', Keys.ENTER)
    # time.sleep(9)
    # # WebhookNodeValidation-
    # InputBox.send_keys('WebhookNodeValidation', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys('WebhookSync', Keys.ENTER)
    # time.sleep(9)
    # # npssurvey with 0 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("0", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    #
    # # npssurvey with 5 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("5", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # # npssurvey with 9 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("9", Keys.ENTER)
    # time.sleep(9)
    # # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # # CSAT -Highly unsatisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Highly unsatisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - unsatisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("unsatisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Average
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Average", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Satisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Satisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Highly Satisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Highly Satisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # LikeDislike - Extremely likely
    # InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Extremely likely", Keys.ENTER)
    # time.sleep(9)
    #
    # # LikeDislike - Extremely Unlikely
    # InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Extremely Unlikely", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium disliked the task", Keys.ENTER)
    # time.sleep(9)
    # # Small talk
    # InputBox.send_keys("HEY", Keys.ENTER)
    # time.sleep(9)
    #
    # # Discard task-
    # InputBox.send_keys("Discard task", Keys.ENTER)
    # time.sleep(9)
    #
    # # ContextValuesClearingValidation
    # InputBox.send_keys("ContextValuesClearingValidation", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Google", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Google", Keys.ENTER)
    # time.sleep(9)
    # # AgentTransferEventforBotkit
    # InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("test", Keys.ENTER)
    # time.sleep(9)
    #
    # # Staging Std XO10 URL
    # url4 = 'https://staging-bots.korebots.com/webclient/dd13d41ba27b4ac69461abb60ac8f831f4cb04a466c4469cb4d50316a8b199a5steb'
    # driver.get(url4)
    # time.sleep(7)
    # InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Message..."]')
    # time.sleep(5)
    # InputBox.send_keys("Cheat lang en", Keys.ENTER)
    # InputBox.send_keys("Cheat lang en", Keys.ENTER)
    # time.sleep(9)
    # # ContentVariableValidation
    # InputBox.send_keys("ContentVariableValidation", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Dialog Script Node", Keys.ENTER)
    # time.sleep(9)
    # # KG-Can you please display Get time service url from Environment variables?
    # InputBox.send_keys('Can you please display Get time service url from Environment variables?', Keys.ENTER)
    # time.sleep(9)
    # # WebhookNodeValidation-
    # InputBox.send_keys('WebhookNodeValidation', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys('WebhookSync', Keys.ENTER)
    # time.sleep(9)
    # # npssurvey with 0 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("0", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    #
    # # npssurvey with 5 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("0", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # # npssurvey with 9 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("9", Keys.ENTER)
    # time.sleep(9)
    # # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # # CSAT -Highly unsatisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Highly unsatisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - unsatisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("unsatisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Average
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Average", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Satisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Satisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Highly Satisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Highly Satisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # LikeDislike - Extremely likely
    # InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Extremely likely", Keys.ENTER)
    # time.sleep(9)
    #
    # # LikeDislike - Extremely Unlikely
    # InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Extremely Unlikely", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium disliked the task", Keys.ENTER)
    # time.sleep(9)
    # # Small talk
    # InputBox.send_keys("HEY", Keys.ENTER)
    # time.sleep(9)
    #
    # # Discard task-
    # InputBox.send_keys("Discard task", Keys.ENTER)
    # time.sleep(9)
    #
    # # ContextValuesClearingValidation
    # InputBox.send_keys("ContextValuesClearingValidation", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Google", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Google", Keys.ENTER)
    # time.sleep(9)
    #
    # # AgentTransferEventforBotkit
    # InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("test", Keys.ENTER)
    # time.sleep(9)
    #
    # # Preprod Stdbot XO10 URL
    # url6 = 'https://preprod-bots.korebots.com/webclient/24ab38e1800d4582b5214ef146625b7e72d2d6affaa14d539ca5710101bc3619st92'
    # driver.get(url6)
    # time.sleep(15)
    # InputBox = driver.find_element(By.CSS_SELECTOR, '[placeholder="Message..."]')
    # time.sleep(5)
    # InputBox.send_keys("Cheat lang en", Keys.ENTER)
    # time.sleep(9)
    # # ContentVariableValidation
    # InputBox.send_keys("ContentVariableValidation", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Dialog Script Node", Keys.ENTER)
    # time.sleep(9)
    # # KG-Can you please display Get time service url from Environment variables?
    # InputBox.send_keys('Can you please display Get time service url from Environment variables?', Keys.ENTER)
    # time.sleep(9)
    # # WebhookNodeValidation-
    # InputBox.send_keys('WebhookNodeValidation', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys('WebhookSync', Keys.ENTER)
    # time.sleep(9)
    # # npssurvey with 0 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("0", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    #
    # # npssurvey with 5 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("0", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # # npssurvey with 9 rating
    # InputBox.send_keys('NPSSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("9", Keys.ENTER)
    # time.sleep(9)
    # # InputBox.send_keys("Python selenium feedback", Keys.ENTER)
    # # CSAT -Highly unsatisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Highly unsatisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - unsatisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("unsatisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Average
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Average", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Satisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Satisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # CSAT - Highly Satisfied
    # InputBox.send_keys('CSATSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Highly Satisfied", Keys.ENTER)
    # time.sleep(9)
    #
    # # LikeDislike - Extremely likely
    # InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Extremely likely", Keys.ENTER)
    # time.sleep(9)
    #
    # # LikeDislike - Extremely Unlikely
    # InputBox.send_keys('LikeDislikeSurveyValidationDialog', Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Extremely Unlikely", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Python selenium disliked the task", Keys.ENTER)
    # time.sleep(9)
    # # Small talk
    # InputBox.send_keys("HEY", Keys.ENTER)
    # time.sleep(9)
    #
    # # Discard task-
    # InputBox.send_keys("Discard task", Keys.ENTER)
    # time.sleep(9)
    #
    # # ContextValuesClearingValidation
    # InputBox.send_keys("ContextValuesClearingValidation", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Google", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("Yes", Keys.ENTER)
    # time.sleep(9)
    #
    # # AgentTransferEventforBotkit
    # InputBox.send_keys("AgentTransferEventforBotkit", Keys.ENTER)
    # time.sleep(9)
    # InputBox.send_keys("test", Keys.ENTER)
    # time.sleep(9)
    #
    # InputBox.send_keys('KoreDebuggerValidation', Keys.ENTER)
    # time.sleep(9)

datageneration()
