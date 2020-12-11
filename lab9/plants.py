import pandas as pd
import matplotlib.pyplot as plt


plant_1 = pd.read_csv('Plant_1_Generation_Data.csv', index_col=[2, 0], parse_dates=True)
plant_2 = pd.read_csv('Plant_2_Generation_Data.csv', index_col=[2, 0], parse_dates=True)
df = pd.concat([plant_1, plant_2])

df = df.dropna()

plt.figure(figsize=(18, 8))
plt.xlabel('TIME', fontsize=10)
plt.ylabel('AC POWER', fontsize=10)
plt.plot(df.loc['zVJPv84UY57bAof']['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'dodgerblue',
         label='zVJPv84UY57bAof')
plt.plot(df.groupby(level=1).mean()['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'green',
         label='Mean for all generators')
plt.legend()
plt.show()


df['MEAN'] = pd.DataFrame(df.groupby(level=1).mean()['AC_POWER']).loc[df.index.get_level_values('DATE_TIME')].values
worse_results = df[['AC_POWER', 'MEAN']][df['AC_POWER'] < 0.8 * df['MEAN']]
print(worse_results['AC_POWER'].groupby(level=0).count().sort_values())
