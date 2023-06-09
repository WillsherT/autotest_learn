# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from time import sleep
from selenium.webdriver.chrome.options import Options


path = Path.cwd()

options = Options()
options.add_experimental_option("prefs", {'download.default_directory': str(path), 'safebrowsing.enabled': 'false'})

sbis_link = 'https://sbis.ru/'

browser = webdriver.Chrome(options=options)

try:
    browser.maximize_window()
    browser.get(sbis_link)
    sleep(3)
    footer = browser.find_element(By.CSS_SELECTOR, ".sbisru-Footer__container")
    browser.execute_script("return arguments[0].scrollIntoView(true);", footer)
    footer_links = browser.find_elements(By.CSS_SELECTOR, ".sbisru-Footer__link")
    sleep(2)
    for link in range(len(footer_links)):
        if footer_links[link].text == 'Скачать СБИС':
            footer_links[link].click()
            break
    sleep(3)
    plugin = browser.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    plugin.click()
    sleep(2)
    download_links = browser.find_elements(By.CSS_SELECTOR, '[data-for="plugin"] .sbis_ru-DownloadNew-loadLink')
    download_links[0].click()
    sleep(3)
    plugin_file = Path(path, 'sbisplugin-setup-web.exe')
    if not plugin_file.exists():
        raise Exception('Плагин не скачался!')
    for file in path.glob('sbisplugin-setup-web.exe'):
        print(f'Размер скачанного файла: {round(int(file.stat().st_size) / 1048576, 2)} мб')
finally:
    browser.quit()
