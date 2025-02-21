import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lxml as lxml
# URL сторінки з таблицею
url = "https://uk.wikipedia.org/wiki/Населення_України#Народжуваність"

# Завантажуємо всі таблиці зі сторінки
tables = pd.read_html(url)

# Визначаємо, яка таблиця потрібна (перевіряємо tables[0], tables[1], ..., поки не знайдемо)
df = tables[2]  # Якщо структура змінилася, змініть індекс

# Вивести перші рядки таблиці
print(df.head())

# Визначити кількість рядків та стовпців
print("Розмірність датафрейму:", df.shape)

# Замінити "—" на NaN
df.replace("—", np.nan, inplace=True)

# Визначити типи всіх стовпців
print(df.dtypes)

# Перетворити числові колонки (окрім першої) у float
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Порахувати частку пропусків у кожному стовпці
print("Частка пропусків:\n", df.isnull().sum() / len(df))

# Видалити останній рядок (загальні дані по країні)
df = df.iloc[:-1]

# Заповнити відсутні дані середніми значеннями
df.fillna(df.mean(), inplace=True)

# Отримати список регіонів, де народжуваність у 2019 році вища за середню
mean_2019 = df["2019"].mean()
high_birth_regions = df[df["2019"] > mean_2019]["Регіон"]
print("Регіони з народжуваністю вище середнього у 2019 році:\n", high_birth_regions)

# Визначити регіон з найвищою народжуваністю у 2014 році
max_region_2014 = df.loc[df["2014"].idxmax(), "Регіон"]
print("Регіон з найвищою народжуваністю у 2014 році:", max_region_2014)

# Побудувати стовпчикову діаграму народжуваності у 2019 році
plt.figure(figsize=(12, 6))
plt.bar(df["Регіон"], df["2019"], color="skyblue")
plt.xticks(rotation=90)
plt.xlabel("Регіон")
plt.ylabel("Народжуваність у 2019 році")
plt.title("Народжуваність по регіонах у 2019 році")
plt.show()
