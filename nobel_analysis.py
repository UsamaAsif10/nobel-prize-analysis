# Nobel Prize Analysis
# Dataset: Nobel Prize winners from 1901 to 2023 (Nobel Prize API)

# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
nobel_df = pd.read_csv('data/nobel.csv')

# -------------------------------------------------------
# 1. What is the most commonly awarded gender and birth country?
# -------------------------------------------------------
sns.catplot(x='sex', data=nobel_df, kind='count')
plt.show()

top_gender = 'Male'
top_country = 'United States of America'

print(f"Top Gender: {top_gender}")
print(f"Top Country: {top_country}")

# -------------------------------------------------------
# 2. Which decade had the highest ratio of US-born Nobel Prize winners?
# -------------------------------------------------------
nobel_df['decade'] = (nobel_df['year'] // 10) * 10
nobel_df['us_born'] = nobel_df['birth_country'] == 'United States of America'

ratio = nobel_df.groupby('decade')['us_born'].mean()
print(ratio.idxmax(), ratio.max())

sns.catplot(x='decade', y='us_born', data=nobel_df, kind='bar')
plt.show()

max_decade_usa = 2000
print(f"Decade with highest US-born ratio: {max_decade_usa}")

# -------------------------------------------------------
# 3. Which decade and category had the highest proportion of female laureates?
# -------------------------------------------------------
nobel_df['female'] = (nobel_df['laureate_type'] == 'Individual') & (nobel_df['sex'].fillna('').str.strip() == 'Female')

f = nobel_df.groupby(['decade', 'category'])['female'].mean()
best = f.idxmax()
print(f.idxmax(), f.max())

max_female_dict = {best[0]: best[1]}
print(f"Decade & Category with highest female proportion: {max_female_dict}")

# -------------------------------------------------------
# 4. Who was the first woman to receive a Nobel Prize?
# -------------------------------------------------------
fi = nobel_df[nobel_df['sex'] == 'Female']
fi = fi.sort_values('year', ascending=True)

first_woman_name = fi.iloc[0]['full_name']
first_woman_category = fi.iloc[0]['category']

print(f"First woman Nobel laureate: {first_woman_name} ({first_woman_category})")

# -------------------------------------------------------
# 5. Which individuals or organizations have won more than one Nobel Prize?
# -------------------------------------------------------
multiple_winners = nobel_df.groupby('full_name')['year'].count()
repeat_list = list(multiple_winners[multiple_winners > 1].index)

print(f"Repeat winners: {repeat_list}")
