# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

browser = webdriver.Chrome()
login = 'AuthTest00'
password = 'AuthTest00AuthTest00'
person_name = 'Гамов Петр'
sbis_link = 'https://fix-online.sbis.ru/'
message = 'Приветствую себя'

try:
    browser.maximize_window()
    browser.get(sbis_link)
    sleep(2)
    login_input = browser.find_element(By.CSS_SELECTOR, "[name='Login']")
    login_input.send_keys(login)
    next_btns = browser.find_elements(By.CSS_SELECTOR, ".auth-AdaptiveLoginForm__loginButtonImage")
    next_btns[0].click()
    sleep(1)
    password_input = browser.find_element(By.CSS_SELECTOR, "[name='Password']")
    password_input.send_keys(password)
    next_btns[1].click()
    sleep(6)
    contacts = browser.find_element(By.XPATH, "//span[contains(@class, 'NavigationPanels-Accordion__title') and "
                                               "contains(text(), 'Контакты')]")
    contacts.click()
    sleep(1)
    contacts = browser.find_element(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle")
    contacts.click()
    sleep(2)
    new_message = browser.find_element(By.CSS_SELECTOR, ".icon-RoundPlus")
    new_message.click()
    sleep(1)
    search = browser.find_element(By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content "
                                                   ".controls-Search__nativeField_caretEmpty")
    search.send_keys(person_name)
    sleep(1)
    find_person = browser.find_element(By.CSS_SELECTOR, ".msg-addressee-item [title='Гамов Петр']")
    find_person.click()
    sleep(1)
    msg_box = browser.find_element(By.CSS_SELECTOR, "[role='textbox']")
    msg_box.send_keys(message)
    sleep(1)
    send_btn = browser.find_element(By.CSS_SELECTOR, ".icon-BtArrow")
    send_btn.click()
    sleep(2)
    sent_messages = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text == message, 'Отправленное сообщение отсутствует в реестре!'
    action_chain = ActionChains(browser)
    action_chain.move_to_element(sent_messages[0])
    action_chain.perform()
    delete_btn = browser.find_element(By.CSS_SELECTOR, ".controls-icon_style-danger")
    delete_btn.click()
    sleep(1)
    assert browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')[0] != message, 'Сообщение не удалено!'
    sleep(2)
finally:
    browser.quit()
