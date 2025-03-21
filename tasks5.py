'''
5.1 При помощи объединения таблиц, создайте DataFrame, состоящий из четырех столбцов: 
id, name, user_id, rating. Рецепты, на которые не оставлен ни один отзыв, должны отсутствовать в полученной таблице.
Подтвердите правильность работы вашего кода, выбрав рецепт, не имеющий отзывов, и попытавшись найти строку, 
соответствующую этому рецепту, в полученном DataFrame.
'''

new_table = pd.merge(recipes[['id', 'name']], reviews[['user_id', 'rating', 'recipe_id']].dropna(), 
                     how='right', left_on='id', right_on='recipe_id') #удаление пустующих значений

new_table.drop('recipe_id',  axis=1, inplace=True) #удалить строку

new_table

# без null
new_table[new_table.id == 388773]

# проверка на отзыв существующий
new_table[(new_table.id == 9054) & (new_table.user_id == 2002151127)]

# проверка на отзыв несуществующий
new_table[(new_table.id == 9054) & (new_table.user_id == 2001567544)]

'''
5.2 При помощи объединения таблиц и группировок, создайте DataFrame, состоящий из трех столбцов: 
recipe_id, name, review_count, где столбец review_count содержит кол-во отзывов, 
оставленных на рецепт recipe_id. У рецептов, на которые не оставлен ни один отзыв, в столбце review_count должен быть указан 0. 
Подтвердите правильность работы вашего кода, выбрав рецепт, 
не имеющий отзывов, и найдя строку, соответствующую этому рецепту, в полученном DataFrame.
'''

new_table_2 = pd.merge(recipes[['id', 'name', 'description']], reviews['recipe_id'], 
                     how='right', left_on='id', right_on='recipe_id')
new_table_2.drop('id',  axis=1, inplace=True)

new_table_2.head()

new_table_3 = pd.merge(new_table_2, new_table_2.groupby('recipe_id')['description'].count(), 
                       how='left', left_on='recipe_id', right_on='recipe_id')

new_table_3.drop_duplicates('name', inplace=True)
new_table_3.drop('description_x',  axis=1, inplace=True)
new_table_3.rename(columns={'description_y': 'review_count'}, inplace=True)
new_table_3 = new_table_3.reindex(['recipe_id', 'name', 'review_count'], axis=1)

new_table_3.head()

new_table_3[new_table_3.recipe_id == 48]  #работает