# NBA Fatigue Analysis: The Impact of "Back-to-Back" Games

## Project Overview
This project investigates the statistical impact of schedule fatigue on NBA team performance. By constructing a data pipeline from the NBA API to a local SQLite database, I engineered features to identify "Back-to-Back" games (0 days rest) and compared point differentials against rested games.

## Methodology
* **Data Ingestion:** Automated extraction of 2023-24 Season logs using `nba_api`.
* **Data Engineering:** Built a local SQLite database to simulate a production environment.
* **SQL Logic:** Utilized Window Functions (`LAG`, `OVER PARTITION`) to calculate `days_rest` for every team dynamically.
* **Analysis:** Python (Pandas/Seaborn) for statistical visualization.

## Key Findings
* **Performance Dip:** Teams playing on 0 days rest ("Back-to-Back") show a median Point Differential (Plus/Minus) below zero, compared to a positive median for rested teams.
* **Variance:** The performance variability remains similar across both groups, suggesting that while the *average* performance drops, the volatility of the game outcome remains consistent.
* **Visual Evidence:** See `data/fatigue_analysis.png` for the boxplot comparison.

## How to Run
1. Install requirements: `pip install pandas nba_api matplotlib seaborn`
2. Run pipeline:
   * `python src/ingest_data.py`
   * `python src/create_db.py`
   * `python src/visualize_results.py`