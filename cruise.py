import seaborn as sns
print(sns.__version__)
import pandas as pd

# Завантаження набору даних "Titanic"
titanic = sns.load_dataset('titanic')

# Виведення перших 5 рядків
print(titanic.head())

# Створення зведеної таблиці
pivot_table = pd.pivot_table(titanic, values='age', index=['class'], columns=['sex'], aggfunc='mean')

# Виведення зведеної таблиці
print(pivot_table)

# Створення зведеної таблиці з двома рівнями індексу
pivot_table = pd.pivot_table(titanic, values='age', index=['class', 'survived'], columns=['sex'], aggfunc='mean')

# Виведення зведеної таблиці
print(pivot_table)

# Створення зведеної таблиці з різними функціями агрегації
pivot_table = pd.pivot_table(titanic, values=['fare', 'survived'], index=['class', 'sex'], aggfunc={'fare': 'mean', 'survived': 'count'})

# Виведення зведеної таблиці
print(pivot_table)
