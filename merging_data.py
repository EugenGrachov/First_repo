import pandas as pd

# Основні методи об'єднання DataFrame у Pandas:

data1 = {
   "name": {"1": "Michael", "2": "John"},
   "country": {"1": "Canada", "2": "USA"},
   "age": {"1": 25, "2": 32}
}

employees1 = pd.DataFrame(data1)

data2 = {
   "name": {"3": "Liza", "4": "Jhon"},
   "country": {"3": "Australia", "4": "Denmark"},
   "age": {"3": 19, "4": 23}
}

employees2 = pd.DataFrame(data2)

employees = pd.concat([employees1, employees2])

print(employees)


# Метод merge об'єднує DataFrame або іменовані об'єкти Series за зазначеними стовпцями або індексами.

data1 = {
   "name": ["Michael", "John"],
   "country": ["Canada", "USA"],
}

data2 = {
   "name": ["Michael", "Liza"],
   "age": [25, 19]
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

merged = pd.merge(employees1, employees2, on='name', how='outer')
print(merged)

merged = pd.merge(employees1, employees2, on='name', how='inner')
print(merged)


# method JOIN

data1 = {
   "name": {"1": "Michael", "2": "John", "3": "Liza", "4": "Jhon"},
   "country": {"1": "Canada", "2": "USA", "3": "Australia", "4": "Denmark"}
}

data2 = {
   "age": {"1": 25, "2": 32, "3": 19, "4": 23}
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

joined = employees1.join(employees2)
print(joined)

# індекси не збігаються - можна використовувати параметр on, щоб вказати стовпець для об'єднання.
import pandas as pd

data1 = {
   "name": ["Michael", "John"],
   "country": ["Canada", "USA"],
}

data2 = {
   "name": ["Michael", "Liza"],
   "age": [25, 19]
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

employees2 = employees2.set_index("name")

joined = employees1.join(employees2, on="name", how="outer")
print(joined)


employees1 = pd.DataFrame(data1).set_index("name")
employees2 = pd.DataFrame(data2).set_index("name")

joined = employees1.join(employees2, how="outer")
print(joined)


