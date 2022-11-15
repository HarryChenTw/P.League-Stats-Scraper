from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class SeasonGameList:
    base_url = 'https://pleagueofficial.com'
    supported_gmae_types = ['regular-season','playoffs','finals']
    supported_season = ['2021-22', '2022-23']
    game_list_table_column = ['game','date','weekday','time','away_team','home_team']

    def __init__(self, season:str='2021-22'):
        assert season in self.supported_season

        # connect with website
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        #self.__browser_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.__browser_driver = webdriver.Chrome(executable_path='webdriver/chromedriver', options=option)
        
        self.__game_list_table = dict()
        self.season = season
        for gmae_type in self.supported_gmae_types:
            self.__game_list_table[gmae_type] = self.__crawl_game_list(gmae_type)

    def __crawl_game_list(self, game_type, up_to_now:bool=True):
        game_type_uri_name = f'schedule-{game_type}' 
        self.__browser_driver.get(f'{self.base_url}/{game_type_uri_name}/{self.season}')

        # preform some clicking before getting all content
        if game_type == 'regular-season':
            self.__browser_driver.find_element(by=By.CSS_SELECTOR, value='label.future>input').click()  # uncheck the 'upcoming' option
        self.__browser_driver.find_element(by=By.CSS_SELECTOR, value='button.btn.btn-square.btn-sm.active').click() # select 'display all month'

        # get all content
        game_list = list()
        elements = self.__browser_driver.find_elements(by=By.CSS_SELECTOR, value=f"div.bg-white.text-dark.border-bottom.border-top.matches>div")
        for element in elements:
            if game_type == 'finals':
                game = element.find_element(by=By.CSS_SELECTOR,value='h5.fs14.mb-2').text.replace('\n',' ') # finals game number have new line
            else:
                game = element.find_element(by=By.CSS_SELECTOR,value='h5.fs14.mb-2').text
            date_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs16.mt-2.mb-1').text
            weekday_ = element.find_element(by=By.CSS_SELECTOR, value='h5.fs12.mb-2').text
            time_ = element.find_element(by=By.CSS_SELECTOR, value='h6.fs12').text
            teams = element.find_elements(by=By.CSS_SELECTOR, value='span.PC_only.fs14')
            away_team, home_team = teams[0].text, teams[1].text
            game_list.append([game, date_, weekday_, time_, away_team, home_team])
        return pd.DataFrame(game_list, columns=self.game_list_table_column)

    def get_game_list(self, game_type:str):
        assert game_type in self.supported_gmae_types
        return self.__game_list_table[game_type]
