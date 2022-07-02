from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

class PlayerStatisticTable:
    base_url = 'https://pleagueofficial.com'
    player_stat_folder = 'stat-player'
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        self.__browser_driver = webdriver.Chrome(executable_path='webdriver/chromedriver', options=option)

        # get connect with website
        self.__browser_driver.get(f'{self.base_url}/{self.player_stat_folder}')
        # get all options in website
        self.season_option, self.game_type_option, self.team_option, self.stat_type_option = self.get_options()
        self.show_options()

    def get_options(self):
        season_option = [season.text for season in self.__browser_driver.find_elements(by=By.CSS_SELECTOR, value='select#season_name>option')]
        game_type_option = [game_type.text for game_type in self.__browser_driver.find_elements(by=By.CSS_SELECTOR, value='select#stage_sn>option')]
        team_option = [team_type.text for team_type in self.__browser_driver.find_elements(by=By.CSS_SELECTOR, value='select#team-name>option')]
        stat_type_option = self.__browser_driver.find_elements(by=By.CSS_SELECTOR, value='select.bg-deepblue.p-2.text-light.col-12.fs14.border-0')[3].find_elements(by=By.CSS_SELECTOR, value='option')
        stat_type_option = [stat_type.text for stat_type in stat_type_option]
        return season_option, game_type_option, team_option, stat_type_option
    
    def show_options(self):
        print("season : ", self.season_option)
        print("game_type : ", self.game_type_option)
        print("team : ", self.team_option)
        print("stat_type : ", self.stat_type_option)

    def __page_number_converter(self,season, game_type):
        season_start = {'2020-21' : 2, '2021-22':6}
        return season_start[season] + self.game_type_option.index(game_type)

    def get_table(self, season = '2021-22', game_type = '例行賽', team = '全部隊伍', stat_type = '平均'):
        # reconnect to web
        # cause when selecting 'season' and 'game_type' options will refresh website, thus they should be specify in URL rather using Selenium select
        page_number = self.__page_number_converter(season, game_type)
        self.__browser_driver.get(f'{self.base_url}/{self.player_stat_folder}/{season}/{page_number}#record')

        team_selecter = Select(self.__browser_driver.find_element(by=By.CSS_SELECTOR, value='select#team-name'))
        team_selecter.select_by_visible_text(team)
        stat_type_selecter = Select(self.__browser_driver.find_elements(by=By.CSS_SELECTOR, value='select.bg-deepblue.p-2.text-light.col-12.fs14.border-0')[3])
        stat_type_selecter.select_by_visible_text(stat_type)
        
        table_element = self.__browser_driver.find_element(by=By.CSS_SELECTOR, value='table#main-table')
        try:
            # get table header
            header = list()
            for header_th in table_element.find_elements(by=By.CSS_SELECTOR, value='thead>tr>th'):
                header.append(header_th.text)

            # get player stat
            player_stats = list()
            for player_row in table_element.find_elements(by=By.CSS_SELECTOR, value='tbody>tr'):
                player_stat = list()
                player_stat.append(player_row.find_element(by=By.CSS_SELECTOR, value='th>a').text) # player's name
                for value in player_row.find_elements(by=By.CSS_SELECTOR, value='td'):  # player's stat value
                    player_stat.append(value.text)
                player_stats.append(player_stat)
        except:
            print('Warning : This table is not available')

        return pd.DataFrame(player_stats, columns=header)