# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
sbis_link = 'https://sbis.ru/'
tensor_link = 'https://tensor.ru/'

try:
    browser.maximize_window()
    browser.get(sbis_link)
    sleep(2)
    contacts = browser.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-link[href='/contacts']")
    contacts.click()
    sleep(2)
    tensor_banner = browser.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    tensor_banner.click()
    sleep(1)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    sleep(1)
    power_is_people = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content "
                                                            ".tensor_ru-Index__card-title")
    if power_is_people.text != 'Сила в людях':
        raise Exception('Отсутствует новость с заголовком "Сила в людях"')
    browser.execute_script("return arguments[0].scrollIntoView(true);", power_is_people)
    about = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    about.click()
    sleep(2)
finally:
    browser.quit()
