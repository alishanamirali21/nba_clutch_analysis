import pandas as pd
import os
from nba_api.stats.endpoints import leaguegamefinder

def fetch_nba_data():
    print("--- Starting Data Ingestion ---")
    
    # 1. Fetch all games for the 2023-24 Season
    print("Fetching 2023-24 Game Logs...")
    # '00' is the ID for the NBA
    gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable='2023-24', league_id_nullable='00')
    games_df = gamefinder.get_data_frames()[0]
    
    # 2. Filter for Regular Season (Season ID starts with '2')
    regular_season_games = games_df[games_df['SEASON_ID'].str.startswith('2')]
    
    # 3. Create a 'data' folder if it doesn't exist yet
    # This prevents "Folder Not Found" errors
    os.makedirs('data', exist_ok=True)
    
    # 4. Save to CSV inside the data folder
    output_filename = "data/nba_games_2023_24.csv"
    regular_season_games.to_csv(output_filename, index=False)
    
    print(f"Success! Data saved to {output_filename}")
    print(f"Total games fetched: {len(regular_season_games)}")

if __name__ == "__main__":
    fetch_nba_data()