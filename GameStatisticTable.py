
import requests
import pandas as pd

class GameStatisticTable:
    column_name = ['#','先發','球員','時間','二分','二分%','三分','三分%','罰球','罰球%',
                '得分','籃板','攻板','防板','助攻','抄截','阻攻','失誤','犯規','EFF','+/-',
                'TS%','USG%','EFG%']
    
    def __init__(self, game_file_number:str):
        params = {'id': game_file_number,'away_tab':'total','home_tab':'total'}
        try:
            self.json_data = requests.get('https://pleagueofficial.com/api/boxscore.php',params = params).json()
            try:
                self.home_table, self.away_table = self.__parse_table(team_side = 'home'), self.__parse_table(team_side = 'away')
            except:
                print('Parsing statistic table error!')
        except:
            print('Cannot get stastistic data from the p-league website!')
        
    def __parse_table(self, team_side):
        assert team_side in ['home','away']
        stat_table = pd.DataFrame([],columns=self.column_name)
        for player_stat in self.json_data['data'][team_side]:
            player_stat_row = pd.DataFrame(
                [[
                    player_stat['jersey'],
                    player_stat['starter'],
                    player_stat['name_alt'],
                    player_stat['mins'],
                    player_stat['two_m_two'],
                    player_stat['twop'],
                    player_stat['trey_m_trey'],
                    player_stat['treyp'],
                    player_stat['ft_m_ft'],
                    player_stat['ftp'],
                    player_stat['points'],
                    player_stat['reb'],
                    player_stat['reb_o'],
                    player_stat['reb_d'],
                    player_stat['ast'],
                    player_stat['stl'],
                    player_stat['blk'],
                    player_stat['turnover'],
                    player_stat['pfoul'],
                    player_stat['eff'],
                    player_stat['positive'],
                    player_stat['tsp'],
                    player_stat['ugp'],
                    player_stat['efgp']
                ]],
                columns=self.column_name
            )
            stat_table = pd.concat([stat_table, player_stat_row]) 
        return stat_table
    
    def get_table(self, team_side):
        assert team_side in ['home','away']
        try:
            if team_side == 'home':
                return self.home_table
            elif team_side == 'away':
                return self.away_table 
        except:
            print('Cannot get the statistic table!')
    
    def download_table(self, team_side, format, output_path):
        assert team_side in ['home','away']
        assert format in ['csv','xlsx']

        try:
            if team_side == 'home':
                output_table = self.home_table
            elif team_side == 'away':
                output_table = self.away_table
            
            if format == 'csv':
                output_table.to_csv(output_path, index=False)
            elif format == 'xlsx':
                output_table.to_excel(output_path, index=False)
        except:
            print('Cannot get the statistic table!')
    
        
        
        
