import sqlite3
import pandas as pd

def analyze_back_to_backs():
    # Connect to your database
    conn = sqlite3.connect("data/nba_stats.db")
    
    # --- THE SQL QUERY ---
    # This query calculates "Days Rest" and "Travel"
    query = """
    WITH Game_Sequence AS (
        SELECT 
            TEAM_NAME,
            GAME_ID,
            GAME_DATE,
            MATCHUP,
            PLUS_MINUS,
            -- Calculate days since previous game for this specific team
            -- julianday converts the date to a number so we can do math
            julianday(GAME_DATE) - julianday(LAG(GAME_DATE) OVER (
                PARTITION BY TEAM_ID ORDER BY GAME_DATE
            )) AS days_rest,
            
            -- Check if they were Home or Away
            CASE WHEN MATCHUP LIKE '%@%' THEN 'Away' ELSE 'Home' END AS location
        FROM games
    )
    SELECT 
        TEAM_NAME,
        GAME_DATE,
        location,
        days_rest,
        PLUS_MINUS,
        -- Create a label for the rest type
        CASE 
            WHEN days_rest = 1 THEN 'Back-to-Back (0 Days Rest)'
            WHEN days_rest = 2 THEN '1 Day Rest'
            WHEN days_rest >= 3 THEN '2+ Days Rest'
            ELSE 'First Game of Season' 
        END as rest_type
    FROM Game_Sequence
    WHERE days_rest = 1 -- Let's just look at Back-to-Backs for now
    ORDER BY TEAM_NAME, GAME_DATE
    LIMIT 20;
    """
    
    print("--- Executing SQL Query for Back-to-Back Analysis ---")
    df = pd.read_sql(query, conn)
    
    print(df)
    
    conn.close()

if __name__ == "__main__":
    analyze_back_to_backs()