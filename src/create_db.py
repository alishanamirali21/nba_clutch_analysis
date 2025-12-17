import pandas as pd
import sqlite3
import os

def create_database():
    print("--- Starting Database Creation ---")
    
    # 1. Define paths
    csv_path = "data/nba_games_2023_24.csv"
    db_path = "data/nba_stats.db"
    
    # Check if CSV exists first
    if not os.path.exists(csv_path):
        print(f"Error: Could not find {csv_path}. Did you run ingest_data.py?")
        return

    # 2. Load the CSV into Pandas
    print("Reading CSV...")
    df = pd.read_csv(csv_path)
    
    # 3. Clean up the date column
    # SQL needs dates in YYYY-MM-DD format to sort correctly
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE']).dt.date
    
    # 4. Connect to SQLite (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    
    # 5. Write data to SQL Table
    # 'if_exists="replace"' means if we run this twice, it overwrites the old table
    table_name = "games"
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"Success! Database created at {db_path}")
    print(f"Table '{table_name}' contains {len(df)} rows.")
    
    conn.close()

if __name__ == "__main__":
    create_database()