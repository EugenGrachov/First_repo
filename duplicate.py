import pandas as pd

data = {
    "name": ["Michael", "Steve", "Liza", "Jhon", "Liza", "Jhon"],
    "country": ["Canada", "USA", "Australia", "Denmark", "Australia", "Denmark"],
    "age": [25, 32, 19, 23, 19, 23]
}

employees = pd.DataFrame(data)

# Для видалення дублюючих даних можна використовувати метод drop_duplicates

employees = employees.drop_duplicates()
print(employees)

# Метод replace використовується для заміни одного або декількох значень у DataFrame або Series. Він може бути корисний для заміни певних значень, які можуть бути неправильними або небажаними.

