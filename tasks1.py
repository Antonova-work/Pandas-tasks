'''
1.1 В файлах recipes_sample.csv и reviews_sample.csv находится информация об 
рецептах блюд и отзывах на эти рецепты соответственно. 
Загрузите данные из файлов в виде pd.DataFrame с названиями recipes и reviews. 
Обратите внимание на корректное считывание столбца с индексами в таблице reviews (безымянный столбец).
'''

import pandas as pd

recipes = pd.read_csv('recipes_sample.csv', sep=',')
reviews = pd.read_csv('reviews_sample.csv', sep=',', index_col=0) #колонки в значение индексов

print('RECIPES')
recipes.head()

print('REVIEWS')
reviews.head()

'''
1.2 Для каждой из таблиц выведите основные параметры:

количество точек данных (строк);
количество столбцов;
тип данных каждого столбца.
'''

# количество точек данных (строк)
print('RECIPES: ', recipes.shape[0])
print('REVIEWS: ', reviews.shape[0])

# количество столбцов
print('RECIPES: ', recipes.shape[1])
print('REVIEWS: ', reviews.shape[1])

# тип данных каждого столбца
print('RECIPES: \n\n', recipes.dtypes)
print('REVIEWS: \n\n', reviews.dtypes)

'''
1.3 Исследуйте, в каких столбцах таблиц содержатся пропуски. Посчитайте долю строк, 
содержащих пропуски, в отношении к общему количеству строк.
'''

pd.isna(recipes) #recipes в каких пропуски, отсутствующие значения

pd.isna(reviews) #reviews в каких пропуски, отсутствующие значения

print('RECIPES')
pd.isna(recipes).sum() / recipes.shape[0]

print('REVIEWS')
pd.isna(reviews).sum() / reviews.shape[0]

#общая сумма
(pd.isna(recipes).sum() / recipes.shape[0]).sum()

#общая сумма
(pd.isna(reviews).sum() / reviews.shape[0]).sum()

'''
1.4 Рассчитайте среднее значение для каждого из числовых столбцов (где это имеет смысл).
'''

recipes.select_dtypes('number').mean()[1:] #1, recipes

recipes.describe().iloc[1][1:] #2, recipes

reviews.select_dtypes('number').mean()[1:] #1, reviews

reviews.describe().iloc[1][1:] #2, reviews

'''
1.5 Создайте серию из 10 случайных названий рецептов.
'''

recipes['name'].sample(10) #случайная выборка

'''
1.6 Измените индекс в таблице reviews, пронумеровав строки, начиная с нуля.
'''

reviews.reset_index(drop=True, inplace=True) #сбросить, а не новый столбец. изменить таблицу, а не новую
reviews

'''
1.7 Выведите информацию о рецептах, время выполнения которых не 
больше 20 минут и кол-во ингредиентов в которых не больше 5.
'''

recipes[(recipes.minutes <= 20) & (recipes.n_ingredients <= 5)]