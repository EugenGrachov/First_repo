import pandas as pd

students_data = {
   'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
   'Вік': [21, 22, 20, 21, 23],
   'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)

print(students_df)

grouped = students_df.groupby('Спеціальність')

print(grouped)

mean_age = grouped['Вік'].mean()
print(mean_age)

min_max_age = grouped['Вік'].agg(['min', 'max'])
print(min_max_age)

summary = grouped.agg({
'Вік': ['min', 'max', 'mean'],
'Імена': 'count'
})
print(summary)

result = grouped['Вік'].agg(lambda x: x.max() - x.min())
print(result)
