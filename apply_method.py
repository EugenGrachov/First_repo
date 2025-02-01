import pandas as pd

# Метод apply

data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура C': [25, 28, 24]
}

weather_df = pd.DataFrame(data)

weather_df['Температура F'] = weather_df['Температура C'].apply(lambda temp: (temp * 9/5) + 32)

print(weather_df)


# Дані про продукти та їх ціни та знижки
data = {
    'Product': ['iPhone 13', 'MacBook Pro', 'Apple Watch'],
    'Price': [699, 1299, 399],
    'Discount': [0.1, 0.05, 0.15]
}

# Створення DataFrame з цими даними
df = pd.DataFrame(data)

# Застосування lanbda-функції до кожного рядка за допомогою apply з axis=1
df['Final Price'] = df.apply(lambda row: row['Price'] * (1 - row['Discount']), axis=1)

print(df)


