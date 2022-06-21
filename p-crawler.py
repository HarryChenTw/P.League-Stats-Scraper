from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_argument('--headless')
#option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

# can use below method to automatically install driver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)


base_url = 'https://pleagueofficial.com/'
year = '2021-22'


# print('Regular Season Games')
# game_type = 'schedule-regular-season'
# driver.get(f'{base_url}/{game_type}/{year}')
# driver.find_element(by=By.CSS_SELECTOR, value='label.future>input').click()  # uncheck the 'upcoming' option
# driver.find_element(by=By.CSS_SELECTOR, value='button.btn.btn-square.btn-sm.active').click() # select 'display all month'
# elements = driver.find_elements(by=By.CSS_SELECTOR, value=f"div.bg-white.text-dark.border-bottom.border-top.matches>div")
# for element in elements:
#     game = element.find_element(by=By.CSS_SELECTOR,value='h5.fs14.mb-2').text
#     date_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs16.mt-2.mb-1').text
#     weekday_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs12.mb-2').text
#     time_ = element.find_element(by=By.CSS_SELECTOR, value='h6.fs12').text
#     teams = element.find_elements(by=By.CSS_SELECTOR, value='span.PC_only.fs14')
#     quest_team, home_team = teams[0].text, teams[1].text
#     print(game, date_, weekday_, time_, f'{quest_team} v.s. {home_team}')


# print('Play-offs')
# game_type = 'schedule-playoffs'
# driver.get(f'{base_url}/{game_type}/{year}')
# driver.find_element(by=By.CSS_SELECTOR, value='button.btn.btn-square.btn-sm.active').click()
# elements = driver.find_elements(by=By.CSS_SELECTOR, value="div.bg-white.text-dark.border-bottom.border-top.matches>div")
# for element in elements:
#     game = element.find_element(by=By.CSS_SELECTOR,value='h5.fs14.mb-2').text
#     date_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs16.mt-2.mb-1').text
#     weekday_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs12.mb-2').text
#     time_ = element.find_element(by=By.CSS_SELECTOR, value='h6.fs12').text
#     teams = element.find_elements(by=By.CSS_SELECTOR, value='span.PC_only.fs14')
#     teams = element.find_elements(by=By.CSS_SELECTOR, value='span.PC_only.fs14')
#     quest_team, home_team = teams[0].text, teams[1].text
#     print(game, date_, weekday_, time_, f'{quest_team} v.s. {home_team}')


print('Finals')
game_type = 'schedule-finals'
driver.get(f'{base_url}/{game_type}/{year}')
driver.find_element(by=By.CSS_SELECTOR, value='button.btn.btn-square.btn-sm.active').click()
elements = driver.find_elements(by=By.CSS_SELECTOR, value="div.bg-white.text-dark.border-bottom.border-top.matches>div")
for element in elements:
    game = element.find_element(by=By.CSS_SELECTOR,value='h5.fs14.mb-2').text.split('\n')[1]
    date_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs16.mt-2.mb-1').text
    weekday_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs12.mb-2').text
    time_ = element.find_element(by=By.CSS_SELECTOR, value='h6.fs12').text
    teams = element.find_elements(by=By.CSS_SELECTOR, value='span.PC_only.fs14')
    teams = element.find_elements(by=By.CSS_SELECTOR, value='span.PC_only.fs14')
    quest_team, home_team = teams[0].text, teams[1].text
    print(game, date_, weekday_, time_, f'{quest_team} v.s. {home_team}')