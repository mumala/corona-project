import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

train = pd.read_csv('./COVID_19/index.csv')
plt.rcParams['font.family'] = 'Malgun Gothic' ## 그래프에서 한글보이도록 폰트설정

temp = train[(train.sigungu == 'all') & (train.gender == 'all')& (train.age == 'all')].reset_index(drop=True)
temp = temp.sort_values(['period', 'cgi'], ascending=[True, True]).reset_index(drop=True)

plt.figure(figsize=(10,5))
plt.xlim(201901, 201912)
chart = sns.lineplot(

    x= "period",
    y= "cgi",
    hue='catl',
    data=temp
)
chart.set_title('서울시 2019 카테고리별 성장지수')
fig = chart.get_figure()
fig.savefig("categ_2019.png")

plt.figure(figsize=(10,5))
plt.xlim(202001, 202012)
chart = sns.lineplot(

    x= "period",
    y= "cgi",
    hue='catl',
    data=temp
)
chart.set_title('서울시 2020 카테고리별 성장지수')
fig = chart.get_figure()
fig.savefig("categ_2020.png")
