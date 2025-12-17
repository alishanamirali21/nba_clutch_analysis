import sqlite3
import pandas as pd
from scipy import stats

def run_significance_test():
    print("--- Running Statistical Significance Test (Welch's T-Test) ---")
    conn = sqlite3.connect("data/nba_stats.db")
    
    # 1. Get the data using the same Logic as before
    query = """
    WITH Game_Sequence AS (
        SELECT 
            PLUS_MINUS,
            julianday(GAME_DATE) - julianday(LAG(GAME_DATE) OVER (
                PARTITION BY TEAM_ID ORDER BY GAME_DATE
            )) AS days_rest
        FROM games
    )
    SELECT PLUS_MINUS, days_rest FROM Game_Sequence
    WHERE days_rest IS NOT NULL
    """
    df = pd.read_sql(query, conn)
    conn.close()
    
    # 2. Split into two groups
    # Note: A date difference of 1.0 means consecutive days (Back-to-Back)
    b2b_group = df[df['days_rest'] == 1]['PLUS_MINUS']
    rested_group = df[df['days_rest'] > 1]['PLUS_MINUS']
    
    # 3. Print Summary Stats
    print(f"\nGroup 1: Back-to-Back (N={len(b2b_group)})")
    print(f"Mean Plus/Minus: {b2b_group.mean():.2f}")
    
    print(f"\nGroup 2: Rested (N={len(rested_group)})")
    print(f"Mean Plus/Minus: {rested_group.mean():.2f}")
    
    # 4. Run the T-Test
    # equal_var=False performs Welch's t-test (does not assume equal variance)
    # alternative='two-sided' checks for ANY difference (positive or negative)
    t_stat, p_value = stats.ttest_ind(rested_group, b2b_group, equal_var=False)
    
    print("\n--- INFERENCE RESULTS ---")
    print(f"T-Statistic: {t_stat:.4f}")
    print(f"P-Value:     {p_value:.5f}") # 5 decimal places for precision
    
    # 5. Interpret the P-Value
    alpha = 0.05
    if p_value < alpha:
        print(f"\nCONCLUSION: REJECT the Null Hypothesis (p < {alpha}).")
        print("There is a statistically significant difference in performance due to fatigue.")
    else:
        print(f"\nCONCLUSION: FAIL TO REJECT the Null Hypothesis (p >= {alpha}).")
        print("The difference observed is likely due to random chance.")

if __name__ == "__main__":
    run_significance_test()