'''
2.1 Преобразуйте столбец submitted из таблицы recipes в формат времени. 
Модифицируйте решение задачи 1.1 так, чтобы считать столбец сразу в нужном формате.
'''

recipes.submitted = pd.to_datetime(recipes.submitted, format='%Y-%m-%d')
recipes.submitted.dt.day

#модификация решения 1.1

recipes = pd.read_csv('recipes_sample.csv', sep=',', parse_dates=[4])
reviews = pd.read_csv('reviews_sample.csv', sep=',', index_col=0)
recipes.submitted.dt.year

'''
2.2 Выведите информацию о рецептах, добавленных в датасет не позже 2010 года.
'''

recipes[recipes.submitted.dt.year > 2010]