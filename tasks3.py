'''
3.1 Добавьте в таблицу recipes столбец description_length, в котором хранится длина описания рецепта из столбца description.
'''

recipes['description_length'] = recipes.description.str.len()
recipes

'''
3.2 Измените название каждого рецепта в таблице recipes таким образом, 
чтобы каждое слово в названии начиналось с прописной буквы.
'''

recipes.name = recipes.name.str.title()
recipes

'''
3.3 Добавьте в таблицу recipes столбец name_word_count, в котором хранится количество 
слов из названии рецепта (считайте, что слова в названии разделяются только пробелами).
Обратите внимание, что между словами может располагаться несколько пробелов подряд.
'''

recipes['name_word_count'] = recipes.name.str.split().str.len()
recipes