import pandas as pd

df = pd.DataFrame({
  "Фрукт": ["Яблуко", "Яблуко", "Груша", "Груша", "Банан", "Банан"],
  "Колір": ["Червоний", "Зелений", "Жовтий", "Зелений", "Жовтий", "Зелений"],
  "Кількість": [10, 12, 15, 9, 20, 18],
  "Ціна": [5, 4, 6, 7, 3, 2]
})

print(df)

table = df.pivot_table(values="Ціна", index="Фрукт", columns="Колір")
print(table)

table = df.pivot_table(values="Ціна", index="Фрукт", columns="Колір", margins=True, fill_value=0)

print(table)


