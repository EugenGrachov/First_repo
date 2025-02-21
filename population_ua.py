import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Чтение таблицы с Wikipedia
url = "https://uk.wikipedia.org/wiki/Населення_України#Народжуваність"
tables = pd.read_html(url)
df = tables[0]

# 2. Вывод первых строк таблицы
print(df.head())

# 3. Определение количества строк и столбцов
print(f"Размер таблицы: {df.shape}")

# 4. Замена "—" на NaN
df.replace("—", pd.NA, inplace=True)

# 5. Определение типов данных
print(df.dtypes)

# 6. Преобразование нечисловых колонок в числовые
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# 7. Подсчет пропущенных значений
print("Пропущенные значения:\n", df.isnull().sum())

# 8. Удаление строки с данными по всей Украине
df = df.iloc[:-1]

# 9. Заполнение пропусков средними значениями
df.fillna(df.mean(), inplace=True)

# 10. Получение списка регионов с рождаемостью выше средней в 2019 году
avg_2019 = df["2019"].mean()
high_birth_regions = df[df["2019"] > avg_2019]
print("Регионы с рождаемостью выше средней в 2019 году:\n", high_birth_regions)

# 11. Регион с наивысшей рождаемостью в 2014 году
highest_2014 = df[df["2014"] == df["2014"].max()]
print("Регион с наибольшей рождаемостью в 2014 году:\n", highest_2014)

# 12. График рождаемости по регионам в 2019 году
plt.figure(figsize=(12, 6))
sns.barplot(x=df["Регіон"], y=df["2019"])
plt.xticks(rotation=90)
plt.title("Рівень народжуваності в 2019 році")
plt.ylabel("Коефіцієнт народжуваності")
plt.show()

# 13. Сортировка по убыванию рождаемости в 2019 году
df_sorted = df.sort_values(by="2019", ascending=False)
print("ТОП-10 регионов по рождаемости в 2019 году:\n", df_sorted.head(10))

# 14. Сохранение результатов в CSV
df.to_csv("birth_rates.csv", index=False)

# 15. Альтернативный метод заполнения NaN
df.fillna(method="ffill", inplace=True)

# 16. Гистограмма значений 2019 года
df["2019"].hist(bins=15)
plt.title("Розподіл рівня народжуваності у 2019 році")
plt.show()

# 17. Стандартизация данных
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled.iloc[:, 1:] = scaler.fit_transform(df.iloc[:, 1:])
print("Стандартизированные данные:\n", df_scaled.head())

# 18. Создание нового столбца с изменением рождаемости
df["Зміна 2019-2018"] = df["2019"] - df["2018"]
print(df[["Регіон", "Зміна 2019-2018"]])

# 19. ТОП-5 регионов с ростом рождаемости
top_growth = df.sort_values(by="Зміна 2019-2018", ascending=False).head(5)
print("ТОП-5 регионов по росту рождаемости:\n", top_growth)

# 20. Проверка на выбросы
print("Статистика данных:\n", df.describe())

# 21. Тепловая карта корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Корреляция показателей рождаемости")
plt.show()

# 22. Запись в Excel
df.to_excel("birth_rates.xlsx", index=False)

# 23. Прогнозирование рождаемости на 2025 год
df["Прогноз 2025"] = df["2019"] + (df["2019"] - df["2018"])
print("Прогноз на 2025 год:\n", df[["Регіон", "2019", "Прогноз 2025"]])

# 24. Анализ среднего уровня рождаемости за десятилетие
df["Середнє за 2010-2019"] = df.loc[:, "2010":"2019"].mean(axis=1)
print("Средний коэффициент рождаемости за 2010-2019:\n", df[["Регіон", "Середнє за 2010-2019"]])

# 25. Фильтр регионов с низкой рождаемостью
df_filtered = df[df["2019"] > 8.0]
print("Регионы с рождаемостью выше 8.0:\n", df_filtered)

# 26. Вычисление стандартного отклонения
print("Стандартное отклонение рождаемости:\n", df.std())

# 27. Вычисление медианы рождаемости
print("Медиана рождаемости:\n", df.median())

# 28. Фильтр регионов, где рождаемость снизилась
df_decline = df[df["2019"] < df["2018"]]
print("Регионы с падением рождаемости:\n", df_decline)
