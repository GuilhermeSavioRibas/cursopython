from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    pesquisa = input('O que deseja pesquisar? ')
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    # pesquisa python
    browser.get('https://docs.python.org/pt-br/3/')
    input_element = browser.find_element(By.XPATH, '/html/body/div[2]/ul/li[9]/div/form/input[1]')
    input_element.send_keys(pesquisa)
    input_element.send_keys(Keys.ENTER)



    # google
    # browser.get('https://google.com/')
    # input_element = browser.find_element(By.NAME, 'q')
    # input_element.send_keys(pesquisa)
    # input_element.send_keys(Keys.ENTER)
    # try:
    #     if browser.find_element(By.XPATH, '//*[@id="rhs"]'):
    #         print(browser.find_element(By.XPATH, '// *[ @ id = "kp-wp-tab-overview"] / div[1] / div / div / div / div / div / div[1] / div / div / div / span[1]').text)
    #     else:
    #         print('Nenhum retorno.')
    # except:
    #     print('Retorno diferente do esperado. Tente outra pesquisa.')

    # browser.close()






