import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(pd.read_excel('2000-4000.xlsx'))
df2 = DataFrame(pd.read_excel('1101-1400.xlsx'))
df2 = df2.dropna()
data = df[u'详论']
data2 = df2[u'疾病']
k = 0
n = -1
for i in df[u'详论']:
    n = n+1
    for j in data2:
        if j in str(i):
            print(j)
            print(i)
            df.iloc[[n], [0]]=j
            k = k+1
print(k)
df.to_excel('标注.xlsx')
