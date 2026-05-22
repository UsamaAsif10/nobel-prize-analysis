# Nobel Prize Analysis

Analysis of Nobel Prize winner data from 1901 to 2023 using Python and Pandas.

## Dataset

`nobel.csv` — Nobel Prize winner data from 1901 to 2023 (sourced from [DataCamp](https://www.datacamp.com)). Dataset not included due to licensing — download it from the DataCamp project workspace (**"A Visual History of Nobel Prize Winners"**) or from [Kaggle](https://www.kaggle.com/datasets/nobelfoundation/nobel-laureates).

It includes the following columns:

| Column | Description |
|--------|-------------|
| year | Year the prize was awarded |
| category | Nobel Prize category |
| prize | Full prize name |
| motivation | Reason for the award |
| prize_share | Share of the prize |
| laureate_id | Unique ID of the laureate |
| laureate_type | Individual or Organization |
| full_name | Full name of the laureate |
| birth_date | Date of birth |
| birth_city | City of birth |
| birth_country | Country of birth |
| sex | Gender of the laureate |
| organization_name | Affiliated organization |
| organization_city | Organization city |
| organization_country | Organization country |
| death_date | Date of death |
| death_city | City of death |
| death_country | Country of death |

## Questions Answered

1. **Most commonly awarded gender and birth country**
   - Top gender: Male
   - Top country: United States of America

2. **Which decade had the highest ratio of US-born Nobel Prize winners?**
   - Decade: 2000s

3. **Which decade and category had the highest proportion of female laureates?**
   - Stored as a dictionary with decade as key and category as value

4. **Who was the first woman to receive a Nobel Prize, and in what category?**
   - Extracted directly from the dataset

5. **Which individuals or organizations have won more than one Nobel Prize?**
   - Stored as a list of full names

## Libraries Used

- Pandas
- NumPy
- Seaborn
- Matplotlib

## How to Run

1. Clone the repo
2. Download `nobel.csv` from DataCamp or Kaggle and place it in the same folder
3. Run the script:

```bash
python nobel_analysis.py
```
