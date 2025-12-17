import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_fatigue():
    print("--- Generatng Visualization ---")
    conn = sqlite3.connect("data/nba_stats.db")
    
    # SQL Query: Get performance metrics + calculated rest days
    query = """
    WITH Game_Sequence AS (
        SELECT 
            TEAM_NAME,
            GAME_DATE,
            PLUS_MINUS,
            julianday(GAME_DATE) - julianday(LAG(GAME_DATE) OVER (
                PARTITION BY TEAM_ID ORDER BY GAME_DATE
            )) AS days_rest
        FROM games
    )
    SELECT 
        PLUS_MINUS,
        CASE 
            WHEN days_rest = 1 THEN 'Back-to-Back (0 Days Rest)'
            ELSE 'Rested (1+ Days Rest)' 
        END as rest_category
    FROM Game_Sequence
    WHERE days_rest IS NOT NULL -- Remove first game of season
    """
    
    df = pd.read_sql(query, conn)
    conn.close()
    
    # --- The Plot ---
    # We use a Boxplot to show the spread of data, not just the mean.
    # This shows "variance," which is scientifically more rigorous.
    plt.figure(figsize=(10, 6))
    
    sns.boxplot(x='rest_category', y='PLUS_MINUS', data=df, showmeans=True, palette="Set2")
    
    plt.title('Impact of Fatigue: NBA Team Performance (2023-24)', fontsize=14)
    plt.ylabel('Point Differential (Plus/Minus)', fontsize=12)
    plt.xlabel('Rest Status', fontsize=12)
    plt.axhline(0, color='black', linestyle='--', alpha=0.5) # Zero line for reference
    
    # Save the plot
    output_path = "data/fatigue_analysis.png"
    plt.savefig(output_path)
    print(f"Graph saved to {output_path}")

if __name__ == "__main__":
    visualize_fatigue()