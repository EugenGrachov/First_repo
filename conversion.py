import pandas as pd

students_data = {
  'Імена': ['Anna', 'Bohdan', 'Olena'],
  'Вік': [21.0, 22.0, 20.0],# Вік як float
  'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

# Конвертація типу стовпця 'Вік' в int

students_df['Вік'] = students_df['Вік'].astype(int)
print(students_df.dtypes)


# Приведення спеціальностей до нижнього регістру
students_df['Спеціальність'] = students_df['Спеціальність'].str.lower()
print(students_df)



