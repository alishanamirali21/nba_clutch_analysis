# NBA Fatigue Analysis: The Impact of "Back-to-Back" Games

## Project Overview
This project investigates the statistical impact of schedule fatigue on NBA team performance. By constructing a data pipeline from the NBA API to a local SQLite database, I engineered features to identify "Back-to-Back" games (0 days rest) and compared point differentials against rested games.

## Methodology
* **Data Ingestion:** Automated extraction of 2023-24 Season logs using `nba_api`.
* **Data Engineering:** Built a local SQLite database to simulate a production environment.
* **SQL Logic:** Utilized Window Functions (`LAG`, `OVER PARTITION`) to calculate `days_rest` for every team dynamically.
* **Analysis:** Python (Pandas/Seaborn) for statistical visualization.

## Key Findings
* **Statistical Significance:** A Welch’s t-test confirmed a statistically significant difference in performance between rested teams and teams on 0 days rest (**p = 0.00485**).
* **Quantifiable Impact:** Teams on back-to-backs averaged a **-2.02** Plus/Minus, compared to **+0.43** for rested teams—a net performance swing of ~2.5 points attributable to schedule fatigue.
* **Sample Size:** Analysis was performed on a dataset of **2,430 games** (N=422 Back-to-Back, N=2008 Rested).

## How to Run
1. Install requirements: `pip install pandas nba_api matplotlib seaborn`
2. Run pipeline:
   * `python src/ingest_data.py`
   * `python src/create_db.py`
   * `python src/visualize_results.py`
