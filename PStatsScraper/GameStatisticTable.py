import requests
import pandas as pd

class GameStatisticTable:
    column_name = ['#','先發','球員','時間','二分','二分%','三分','三分%','罰球','罰球%',
                '得分','籃板','攻板','防板','助攻','抄截','阻攻','失誤','犯規','EFF','+/-',
                'TS%','USG%','EFG%']
    team_sides = ['home','away']
    game_file_number_starts = {
        "2020-21":{
            'regular-season' : 13,
            'playoffs' : 61,
            'finals' : 66
        },
        "2021-22":{
            'regular-season' : 73,
            'playoffs' : 174,
            'finals' : 184
        }
    }
    gmae_types = ['regular-season','playoffs','finals']
    supported_season = ['2021-22']

    def __init__(self, season:str, game_type:str, game_number:str):
        assert season in self.supported_season
        assert game_type in self.gmae_types

        game_file_number = self.convert_to_game_file_name(season, game_type, game_number)
        params = {'id': game_file_number,'away_tab':'total','home_tab':'total'}
        self.json_data = requests.get('https://pleagueofficial.com/api/boxscore.php',params = params).json()
        self.home_table, self.away_table = self.__parse_table(team_side = 'home'), self.__parse_table(team_side = 'away')
    
    def convert_to_game_file_name(self, season:str, game_type:str, game_number:str) -> str:
        file_starts = self.game_file_number_starts[season][game_type]
        if game_type == 'regular-season':
            return int(game_number[1:]) + file_starts -1
        elif game_type == 'playoffs':
            if game_number[0] == 'B':
                return int(game_number[-1]) * 2 +  file_starts -1
            else:
                return int(game_number[-1]) +  file_starts -1
        elif game_type == 'finals':
            int(game_number[-1]) + file_starts -1


    def __parse_table(self, team_side):
        assert team_side in self.team_sides
        stat_table = pd.DataFrame([],columns=self.column_name)

        # parse every player
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
        # parse total statistic 
        total_stat = self.json_data['data'][f'{team_side}_total']
        total_stat_row = pd.DataFrame(
            [[
                '','','Total',
                total_stat['mins'],
                f"{total_stat['two_m']}-{total_stat['two']}",
                f"{total_stat['twop']}%",
                f"{total_stat['trey_m']}-{total_stat['trey']}",
                f"{total_stat['treyp']}%",
                f"{total_stat['ft_m']}-{total_stat['ft']}",
                f"{total_stat['ftp']}%",
                total_stat['points'],
                total_stat['reb'],
                total_stat['reb_o'],
                total_stat['reb_d'],
                total_stat['ast'],
                total_stat['stl'],
                total_stat['blk'],
                total_stat['turnover'],
                total_stat['pfoul'],
                '','','','',''
            ]],
            columns=self.column_name
        )
        stat_table = pd.concat([stat_table, total_stat_row])
        return stat_table
    
    def get_table(self, team_side):
        assert team_side in self.team_sides

        if team_side == 'home':
            return self.home_table
        elif team_side == 'away':
            return self.away_table 
    
    def download_table(self, team_side, format, output_path):
        assert team_side in self.team_sides
        assert format in ['csv','xlsx']
        
        if team_side == 'home':
            output_table = self.home_table
        elif team_side == 'away':
            output_table = self.away_table
        
        if format == 'csv':
            output_table.to_csv(output_path, index=False)
        elif format == 'xlsx':
            output_table.to_excel(output_path, index=False)
    
        
        
        
