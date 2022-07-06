from API.GameStatisticTable import GameStatisticTable
from API.SeasonGameList import SeasonGameList

print('Getting connection with the website...')
game_list = SeasonGameList()

# select game type
print(f'\nSelect a game type ( Enter number 1 ~ {len(SeasonGameList.gmae_types)} ) ')
for i, game_type in enumerate(SeasonGameList.gmae_types):
    print(f'[{i+1}]{game_type}')
selected_number = input(': ')
while not((int(selected_number)>=1) and int(selected_number)<=len(SeasonGameList.gmae_types)):
    selected_number = input('Invalid number, please select again : ')
selected_game_type = SeasonGameList.gmae_types[int(selected_number)-1]


# select game number
selecter_game_list = game_list.get_game_list(selected_game_type)
print(f'\nSelect a game ( Enter number 1 ~ {len(selecter_game_list)} )')
for i, game in enumerate(selecter_game_list):
    game_str = ' '.join(game[:-2]) + f' {game[-2]}(客/away) v.s. {game[-1]}(主/home)'
    print(f'[{i+1}] {game_str}')
selected_number = input(': ')
while not((int(selected_number)>=1) and int(selected_number)<=len(selecter_game_list)):
    selected_number = input('Invalid number, please select again : ')
selected_team_side = input("Home team or Away team ( Enter 'home' or 'away' ) : ")


# select game type and 
selected_format = input("Output format ( Enter 'xlsx' or 'csv' ) : ")
output_path = input('Output path : ')
print('Downloading...')
game_file_number = SeasonGameList.game_file_number_starts[selected_game_type] + int(selected_number) - 1
game_statistic_table = GameStatisticTable(game_file_number=game_file_number)
game_statistic_table.download_table(selected_team_side, format=selected_format, output_path=output_path)
print('Done!')
