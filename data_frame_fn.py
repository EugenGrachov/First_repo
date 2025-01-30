import pandas as pd

students_data = {
   'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
   'Вік': [21, 22, 20, 21, 23],
   'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)

total_age = students_df['Вік'].sum() # 107
average_age = students_df['Вік'].mean() # 21.4
median_age = students_df['Вік'].median() # 21.0
min_age = students_df['Вік'].min() # 20
max_age = students_df['Вік'].max() # 23
std_age = students_df['Вік'].std() # 1.1401754250991378
variance_age = students_df['Вік'].var() # 1.2999999999999998
count_age = students_df['Вік'].count() # 5
unique_specialties = students_df['Спеціальність'].nunique() # 3
first_quartile_age = students_df['Вік'].quantile(0.25) # 21.0

idx_max_age = students_df['Вік'].idxmax() # 4
idx_min_age = students_df['Вік'].idxmin() # 2
product_age = students_df['Вік'].prod() # 4462920
sem_age = students_df['Вік'].sem() # 0.5099019513592784
