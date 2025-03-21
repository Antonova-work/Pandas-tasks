'''
1. Загрузите данные из файла sp500hst.txt и обозначьте столбцы в соответствии с содержимым: 
"date", "ticker", "open", "high", "low", "close", "volume".
'''

import pandas as pd

col = pd.read_csv('sp500hst.txt', sep=',',
                header=None, names=["date",  "ticker", "open", "high", "low", "close", "volume"]) #нет заголовка
print(col)

'''
2. Рассчитайте среднее значение показателей для каждого из столбцов c номерами 3-6.
'''
import pandas as pd

col = pd.read_csv('sp500hst.txt', sep=',',
                header=None, names=["date",  "ticker", "open", "high", "low", "close", "volume"])

col[['open', 'high', 'low', 'close']].iloc[3:6].mean(axis=0) #выбор строк

'''
3. Добавьте столбец, содержащий только число месяца, к которому относится дата.
'''
import pandas as pd

col['month'] = pd.to_datetime(col['date'], format='%Y%m%d').dt.month #месяц в число

print(col)

'''
4. Рассчитайте суммарный объем торгов для одинаковых значений тикеров.
'''

import pandas as pd

col.groupby('ticker')['open'].sum()

'''
5. Загрузите данные из файла sp500hst.txt и обозначьте столбцы в соответствии с содержимым: 
"date", "ticker", "open", "high", "low", "close", "volume". 
Добавьте столбец с расшифровкой названия тикера, используя данные из файла sp_data2.csv . 
В случае нехватки данных об именах тикеров корректно обработать их.
'''

import pandas as pd

col2 = pd.read_csv('sp_data2.csv', sep=';', header=None, names=["ticker",  "company", "percent",])

pd.merge(col, col2, how='inner', left_on='ticker', right_on='ticker') #пересечение, ключ

col_l = pd.merge(col, col2, how='left') #объединение данных несколько таблиц,сохранение строк из левой
col_l.fillna('-') #замена Nan

print(col_l)