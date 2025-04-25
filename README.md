# League of Legends Pro Player Performance Analysis

**Faris Aleem Ahmad – 33570**  
**DSA210 – Spring 2025 – Term Project**

---

## Project Summary

This project analyzes the performance of seven professional League of Legends players across two match types: **off-season solo queue games** and **official tournament matches**. The goal is to evaluate whether there are **statistically significant differences** in player behavior and performance based on the match environment.

---

## Key Metrics Analyzed

- **KDA** (Kill/Death/Assist ratio)  
- **CS per Minute** (Creep Score)  
- **Gold per Minute**  
- **Damage per Minute**  
- **Deaths**  
- **Custom Performance Score** (combined weighted metric)

---

## Dataset

- 14 CSV files (7 players × 2 match types: Offseason & Tournament)
- 10 matches per player per type (total = 140 matches)
- Data sources:
  - [OP.GG](https://op.gg) – Off-season match histories
  - [LoL Fandom Wiki](https://lol.fandom.com/wiki) – Tournament stats
  - Riot Developer API – Match verification & player activity

---

## Methodology

1. Collected and cleaned raw match data for each player
2. Enriched each record with:
   - KDA, CS/min, Gold/min, Damage/min, Win
   - Custom performance score
3. Performed **Exploratory Data Analysis (EDA)**
4. Conducted **3 statistical hypothesis tests**:
   - Difference in overall performance score
   - Difference in deaths per match
   - Difference in CS per minute

---

## Results

- **Performance Score:** Significantly higher in off-season  
- **Deaths:** Significantly lower in tournament matches  
- **CS/min:** Significantly higher in tournament matches  

These results support the idea that players adjust their strategy based on match environment — playing safer and farming more efficiently in tournaments.

---

## Files in This Repository

| File/Folder | Description |
|-------------|-------------|
| `main_notebook.ipynb` | Full notebook with all analysis, EDA, and hypothesis testing |
| `data/` | Folder containing 14 CSV files for each player and match type |

---

## Notes

This project was completed as part of the Data Science course (DSA210) in Spring 2025.  
All data used was publicly available and used for academic purposes only.
