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
  - [OP.GG](https://op.gg) and [Trackingthepros](https://trackingthepros.com) – Off-season match histories
  - [LoL Fandom Wiki](https://lol.fandom.com/wiki) – Tournament stats
  - Riot Developer API – Match verification & player activity
**NOTE** : Tournament matches are played in a series of 3/5. Only the first match of each series was considered for this project to avoid skill-based factors having a prominent, repeated effect.

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
| `riotAPI_sample.py` | Python file showcasing how the API can be utilised to retrieve player data (non-functional due to outdated key |

---

## Notes

This project was completed as part of the Data Science course (DSA210) in Spring 2025.  
All data used was publicly available and used for academic purposes only.
The sample code for the API usage is uploaded seperately. 
It is purely for grading/showcase purposes and will not function as Riot Games refreshes their API key every 24 hours.


## Data Scraping Sources
op.gg -- offseason

trackingthepros - offseason

lol.fandom -- tournament

Faker 
- https://op.gg/lol/summoners/kr/Hide%20on%20bush-KR1 
- https://lol.fandom.com/wiki/Faker/Match_History  

Chovy
- https://op.gg/lol/summoners/kr/%ED%97%88%EA%B1%B0%EB%8D%A9-0303
- https://lol.fandom.com/wiki/Chovy/Match_History

Ruler 
- https://op.gg/lol/summoners/kr/%EA%B7%80%EC%B0%AE%EA%B2%8C%ED%95%98%EC%A7%80%EB%A7%88-KR3
- https://lol.fandom.com/wiki/Ruler/Match_History

Caps
- https://op.gg/lol/summoners/euw/G2%20Caps-1323
- https://lol.fandom.com/wiki/Caps/Match_History

BlaberFish
- https://op.gg/lol/summoners/na/blaberfish2-NA1
- https://lol.fandom.com/wiki/Blaber/Match_History

Zeus 
- https://trackingthepros.com/player/Zeus
- https://lol.fandom.com/wiki/Zeus/Match_History

Hans Sama
- https://op.gg/lol/summoners/euw/G2%20Hans%20Sama-12838
- https://lol.fandom.com/wiki/Hans_Sama/Match_History
