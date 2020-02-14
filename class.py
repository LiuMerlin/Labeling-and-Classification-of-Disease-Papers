import csv
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(pd.read_excel('2000-4000全部标注.xlsx'))
df2 = DataFrame(pd.read_excel('2000-4000全部标注.xlsx'))

data = df[[u'疾病', u"详论"]]
data = DataFrame(data)

data2 = df2[u'疾病']
data2 = data2.dropna()
data2 = data2.drop_duplicates()

f = open('疾病分类.csv', 'w', newline='', encoding='utf-8-sig')

csv_writer = csv.writer(f)
csv_writer.writerow(["疾病", "总数", "详论"])
k = 0
for j in data2:
    s = 0
    for i in range(0, 1881):
        if j == data.iloc[i, 0]:
            print(j)
            m = data.iloc[i, 1]
            print(data.iloc[i, 1])
            s = s+1
            csv_writer.writerow([j, s, m])
            k = k+1
    print(s)
print(k)
f.close()
