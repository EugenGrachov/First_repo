import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Прочитайте дані за допомогою методу read_html з таблиці "Коефіцієнт народжуваності в регіонах України (1950—2019)"
url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C"
tables = pd.read_html(url)
table = tables[13]

# Вивести перші рядки таблиці за допомогою методу head
print(table.head())

# Визначити кількість рядків і стовпців у датафреймі (атрибут shape)
print("Shape:", table.shape)

# Замінити у таблиці значення "—" на значення NaN
table = table.replace("—", np.nan)
table.head()
print(table.head())

# Визначити типи всіх стовпців
print(table.dtypes)

# Замінити типи нечислових колонок на числові
table[["2014", "2019"]] = table[["2014", "2019"]].apply(pd.to_numeric)

# Порахуйте, яка частка пропусків міститься в кожній колонці
print(table.isnull().sum())

# Видалити з таблиці дані по всій країні, останній рядок таблиці
table = table[:-1]
print(table)

# Замінити відсутні дані в стовпцях середніми значеннями цих стовпців метод fillna)
table = table.fillna({
   "1950": table["1950"].mean(), "1960": table["1960"].mean(),
   "1970": table["1970"].mean(), "2014": table["2014"].mean(), "2019": table["2019"].mean()
})

print(table)

# Отримати список регіонів, де рівень народжуваності у 2019 році був вищим за середній по Україні
print(table[table["2019"] > table["2019"].mean()]["Регіон"])

# Визначити регіон з найвищою народжуваністю у 2014 році
print(table[table["2014"] == table["2014"].max()])

# Побудувати стовпчикову діаграму народжуваності за регіонами у 2019 році
plt.figure(figsize=(10, 6))
table.plot(x="Регіон", y="2019", kind="bar", legend=False)
plt.title("Народжуваність за регіонами у 2019 році")
plt.xlabel("Регіон")
plt.ylabel("Коефіцієнт народжуваності")
plt.xticks(rotation=90)
plt.grid()
plt.show()

# Зберегти таблицю у файл
table.to_csv("birth_rate.csv", index=False)

