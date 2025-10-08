import pandas as pd

# Load the data
df_stats = pd.read_csv("weekly_data_stats.csv")
df_odds = pd.read_csv("weekly_data_odds.csv")
df_injuries = pd.read_csv("weekly_data_injuries.csv")

# Example: merge stats and injuries on a common column, e.g., 'player_id'
# (You may need to adjust the column names based on your actual data)
df = pd.merge(df_stats, df_injuries, on="player_id", how="left")

# If you want to include odds, merge again (adjust the key as needed)
df = pd.merge(df, df_odds, on="team", how="left")

# Now you can analyze the combined DataFrame
# Example: calculate opportunity score only for healthy players
df_healthy = df[df["injury_status"].isnull() | (df["injury_status"] == "Healthy")]

df_healthy["opportunity_score"] = (
    0.5 * df_healthy["recent_points"] +
    0.3 * df_healthy["team_projected_points"] +
    0.2 * df_healthy["opponent_defense_weakness"]
)

top_players = df_healthy.sort_values("opportunity_score", ascending=False).head(10)
top_players.to_csv("recommendations.csv", index=False)