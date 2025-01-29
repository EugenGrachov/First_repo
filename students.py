import pandas as pd

students_df = pd.DataFrame({
   'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
   'Вік': [21, 22, 20, 21, 23],
   'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
   }, index=['st1', 'st2', 'st3', 'st4', 'st5'])

print(students_df)

value = students_df.loc['st2', 'Вік'] 
print(value) # 22

subset = students_df.loc['st2':'st4', 'Імена':'Вік']
print(subset) 

subset_2 = students_df.loc['st1':'st4', 'Вік':'Спеціальність']
print(subset_2) 

# DATAFRAME INLOC

value = students_df.iloc[1, 1]
print(value) # 22

subset = students_df.iloc[1:4, 0:2]
print(subset) 

