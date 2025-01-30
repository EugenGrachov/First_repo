import pandas as pd

students_df = pd.DataFrame({
   'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
   'Вік': [21, 22, 20, 21, 23],
   'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
   }, index=['st1', 'st2', 'st3', 'st4', 'st5'])

print(students_df)

subset = students_df[1:3]
print(subset)

subset = students_df[3:]
print(subset)

subset = students_df[:2]
print(subset)

subset = students_df.loc[:, 'Імена':'Вік']
print(subset)

