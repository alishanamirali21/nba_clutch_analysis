# NBA Fatigue Analysis: The Impact of "Back-to-Back" Games

## Project Overview
This project investigates the statistical impact of schedule fatigue on NBA team performance. By constructing a data pipeline from the NBA API to a local SQLite database, I engineered features to identify "Back-to-Back" games (0 days rest) and compared point differentials against rested games.

## Methodology
* **Data Ingestion:** Automated extraction of 2023-24 Season logs using `nba_api`.
* **Data Engineering:** Built a local SQLite database to simulate a production environment.
* **SQL Logic:** Utilized Window Functions (`LAG`, `OVER PARTITION`) to calculate `days_rest` for every team dynamically.
* **Analysis:** Python (Pandas/Seaborn) for statistical visualization.

## Key Findings
* [Teams playing on 0 days rest suffer a measurable performance penalty, likely averaging a net negative point differential compared to their baseline."]

## How to Run
1. Install requirements: `pip install pandas nba_api matplotlib seaborn`
2. Run pipeline:
   * `python src/ingest_data.py`
   * `python src/create_db.py`
   * `python src/visualize_results.py`
