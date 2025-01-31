import pandas as pd

students_data = {
   'Імена': ['Anna', 'Bohdan', None],
   'Вік': [21, None, 20],
   'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

# Метод dropna видаляє рядки або стовпці з відсутніми даними.
cleaned_df = students_df.dropna()
print(cleaned_df)

# Метод fillna заповнює відсутні дані вказаним значенням або методом.
import numpy as np
import pandas as pd

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

data = data.fillna({0: data[0].mean(), 1: data[1].mean(), 2: data[2].mean()})

print(data)


# Метод drop використовується для видалення конкретних рядків або стовпців з DataFrame.
students_data = {
   'Імена': ['Anna', 'Bohdan', 'Olena'],
   'Вік': [21, 22, 20],
   'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

students_df.drop([1], inplace=True)
print(students_df)

# Щоб видаляти стовпці, необхідно вказати вісь через параметр axis.
students_data = {
   'Імена': ['Anna', 'Bohdan', 'Olena'],
   'Вік': [21, 22, 20],
   'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

students_df = students_df.drop(['Вік'], axis=1)
print(students_df)