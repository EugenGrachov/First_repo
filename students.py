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

subset = students_df.iloc[[0, 2], [0,2]]
print(subset) 

# Використання loc для вибору даних за мітками
bohdan_data = students_df.loc['st2', 'Спеціальність']
print(bohdan_data) # "Physics"

# Використання iloc для вибору даних за індексами
bohdan_data = students_df.iloc[1, 2]
print(bohdan_data) # "Physics"

bodya = students_df.loc['st2', 'Імена']
print(bodya)

bodya = students_df.iloc[1, 2]
print(bodya)

# Використання loc (включає 'st4')
subset_loc = students_df.loc['st2':'st4', 'Вік':'Спеціальність']
print(subset_loc) 

# Використання iloc (не включає 4-й рядок)
subset_iloc = students_df.iloc[1:4, 1:3]
print(subset_iloc)

# Вибірка студентів, які вивчають фізику, за допомогою loc
physics_students = students_df.loc[students_df['Спеціальність'] == 'Physics']
print(physics_students)

# Вибірка студентів за конкретними індексами за допомогою iloc
specific_students = students_df.iloc[[1, 4]]
print(specific_students)
