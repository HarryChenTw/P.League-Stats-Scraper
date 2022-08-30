**P.League-Stats-Scraper**是一個工具可以得到 P.League 各類型統計資料。資料內容與 [P.League](https://pleagueofficial.com/) 網站提供的內容相同，但網站不提供下載的選項。因此P.League-Stats-Scraper透過爬蟲的技術，得到網站上的統計資料，提供給想要做資料分析的人可以有更快速的資料取得方式。

<em>**Jul. 02 2022 Updated (v1.2.1)**</em>

<img width="1436" alt="Screen Shot 2022-08-30 at 2 08 13 PM" src="https://user-images.githubusercontent.com/75982405/187362229-deb0f10d-cd85-49ae-899b-01f316e63130.png">

<br>

## 使用範例
參考 [usage-example.ipynb](https://github.com/HarryChenTw/P.League-Stats-Scraper/blob/main/usage-example.ipynb)

1. 取得賽季所有的比賽列表
      ```python
      from PStatsScraper.SeasonGameList import SeasonGameList
      season_game_list = SeasonGameList('2021-22')
      season_game_list.get_game_list('playoffs')
      ```
    <img width="392" alt="Screen Shot 2022-08-30 at 2 12 51 PM" src="https://user-images.githubusercontent.com/75982405/187362991-5a169aad-4417-4393-9da0-6269137b6196.png">

<br>

2. 取得一場比賽的所有球員數據
    ```python
    from PStatsScraper.GameStatisticTable import GameStatisticTable
    game_statistic_table = GameStatisticTable(season='2021-22',game_type='playoffs',game_number='AG1')
    game_statistic_table.get_table(team_side='home')
    ```
    <img width="879" alt="Screen Shot 2022-08-30 at 2 13 39 PM" src="https://user-images.githubusercontent.com/75982405/187363170-23fb7962-5f4b-4455-b3ff-e214dd8723a9.png">
    
<br>
    
3. 取得一個賽季(例行賽、季後賽、總冠軍賽)的球員數據
    ```python
    from PStatsScraper.PlayerStatisticTable import PlayerStatisticTable
    player_ststistic_table = PlayerStatisticTable()
    player_ststistic_table.get_table(season='2021-22',game_type='總冠軍賽',team='新竹街口攻城獅',stat_type='平均')
    ```
    <img width="1027" alt="Screen Shot 2022-08-30 at 2 14 39 PM" src="https://user-images.githubusercontent.com/75982405/187363284-ec9b820c-bf2f-495e-b61e-4bc09b5b575f.png">

<br>

## 限制
1. 有些功能只提供 2021-22 賽季
