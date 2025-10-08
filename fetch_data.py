import requests, pandas as pd

# Get player stats from Sleeper
stats = requests.get("https://api.sleeper.app/v1/stats/nfl/2025").json()

# Get player injuries from Sleeper
injuries = requests.get("https://api.sleeper.app/v1/players/nfl/injuries").json()

# Get betting lines from TheOddsAPI
odds = requests.get("https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds",
                    params={"apiKey": "YOUR_API_KEY", "regions": "us"}).json()

# Transform into dataframes and save as CSVs
df_stats = pd.DataFrame(stats)
df_stats.to_csv("weekly_data_stats.csv", index=False)

df_odds = pd.DataFrame(odds)
df_odds.to_csv("weekly_data_odds.csv", index=False)

df_injuries = pd.DataFrame(injuries)
df_injuries.to_csv("weekly_data_injuries.csv", index=False)