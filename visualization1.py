import pandas as pd
from matplotlib import pyplot as plt
train = pd.read_csv('./COVID_19/TimeProvince.csv')

plt.rcParams['font.family'] = 'Malgun Gothic' ## 그래프에서 한글보이도록 폰트설정




temp_Seoul = train[(train.province=='서울')& (train.date < '2020-03-01')]
temp_Seoul = temp_Seoul.drop_duplicates('confirmed', keep='first')
temp_Seoul

import seaborn as sns
sns.set()
sns.set_style('whitegrid')
sns.set_color_codes()

sns.relplot(x="date", y="confirmed",data=temp_Seoul)
