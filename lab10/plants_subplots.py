import pandas as pd
import matplotlib.pyplot as plt

plant_1 = pd.read_csv('Plant_1_Generation_Data.csv', index_col=[2, 0], parse_dates=True, dayfirst=True)
plant_2 = pd.read_csv('Plant_2_Generation_Data.csv', index_col=[2, 0], parse_dates=True, dayfirst=True)
df = pd.concat([plant_1, plant_2])

df = df.dropna()

generator_1 = '1BY6WEcLGh8j5v7'
generator_2 = '1IF53ai7Xc0U56Y'


def calculate_ratio(generator):
    plant1 = pd.read_csv('Plant_1_Generation_Data.csv')
    plant2 = pd.read_csv('Plant_2_Generation_Data.csv')
    new_df = pd.concat([plant1, plant2])
    mean = new_df.groupby('DATE_TIME').mean()['DAILY_YIELD']

    dict_of_frequency = {'<75%': 0, '75-85%': 0, '85-95%': 0, '95-105%': 0, '105-115%': 0, '115-125%': 0, '>125%': 0}
    end_of_day_generator = new_df[(new_df['DATE_TIME'].str.contains('23:00')) & (new_df['SOURCE_KEY'] == generator)].loc[:,
                             ['DATE_TIME', 'DAILY_YIELD']]
    for date in end_of_day_generator['DATE_TIME']:
        ratio = float(
            end_of_day_generator[end_of_day_generator['DATE_TIME'] == date]['DAILY_YIELD'] / mean.loc[date])
        if ratio < 0.75:
            dict_of_frequency['<75%'] += 1
        elif 0.75 <= ratio < 0.85:
            dict_of_frequency['75-85%'] += 1
        elif 0.85 <= ratio < 0.95:
            dict_of_frequency['85-95%'] += 1
        elif 0.95 <= ratio < 1.05:
            dict_of_frequency['95-105%'] += 1
        elif 1.05 <= ratio < 1.15:
            dict_of_frequency['105-115%'] += 1
        elif 1.15 <= ratio <= 1.25:
            dict_of_frequency['115-125%'] += 1
        elif ratio > 1.25:
            dict_of_frequency['>125%'] += 1
    return dict_of_frequency


plt.figure()
plt.subplot(221)
plt.xlabel('TIME', fontsize=6)
plt.ylabel('AC POWER', fontsize=6)
plt.plot(df.loc[generator_1]['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'dodgerblue', linewidth=2,
         label=generator_1)
plt.plot(df.loc[generator_2]['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'green', linewidth=2,
         label=generator_2)
plt.plot(df.loc['3PZuoBAID5Wc2HD']['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'black', linewidth=1,
         label='3PZuoBAID5Wc2HD')
plt.plot(df.loc['7JYdWkrLSPkdwr4']['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'orange', linewidth=1,
         label='7JYdWkrLSPkdwr4')
plt.plot(df.loc['McdE0feGgRqW7Ca']['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'violet', linewidth=1,
         label='McdE0feGgRqW7Ca')
plt.plot(df.loc['VHMLBKoKgIrUVDU']['AC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'brown', linewidth=1,
         label='VHMLBKoKgIrUVDU')
plt.title('AC POWER')
plt.legend()

plt.subplot(222)
plt.xlabel('TIME', fontsize=6)
plt.ylabel('DC POWER', fontsize=6)
plt.plot(df.loc[generator_1]['DC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'dodgerblue', linewidth=2,
         label=generator_1)
plt.plot(df.loc[generator_2]['DC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'green', linewidth=2,
         label=generator_2)
plt.plot(df.loc['3PZuoBAID5Wc2HD']['DC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'black', linewidth=1,
         label='3PZuoBAID5Wc2HD')
plt.plot(df.loc['7JYdWkrLSPkdwr4']['DC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'orange', linewidth=1,
         label='7JYdWkrLSPkdwr4')
plt.plot(df.loc['McdE0feGgRqW7Ca']['DC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'violet', linewidth=1,
         label='McdE0feGgRqW7Ca')
plt.plot(df.loc['VHMLBKoKgIrUVDU']['DC_POWER']['2020-05-15 00:00:00':'2020-05-22 00:00:00'], 'brown', linewidth=1,
         label='VHMLBKoKgIrUVDU')
plt.title('DC POWER')
plt.legend()

plt.subplot(223)
plt.title('RATIO FOR GENERATOR 1')
plt.xlabel('INTERVALS', fontsize=6)
plt.ylabel('FREQUENCY', fontsize=6)
plt.bar(calculate_ratio(generator_1).keys(), calculate_ratio(generator_1).values())

plt.subplot(224)
plt.title('RATIO FOR GENERATOR 2')
plt.xlabel('INTERVALS', fontsize=6)
plt.ylabel('FREQUENCY', fontsize=6)
plt.bar(calculate_ratio(generator_1).keys(), calculate_ratio(generator_2).values())

plt.show()
