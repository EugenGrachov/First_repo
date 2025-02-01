import pandas as pd

# Середні температури за дні місяця
temperature_data = {
   'День': list(range(1, 31)),
   'Температура': [15, 18, None, 20, 17, 18, 20, None, 14, 16, 18, 19, None, 15, 14, 17, 16, None, 17, 20, 15, 16, 15, 19, 20, None, 15, 18, 17, 16]
}

temperature_df = pd.DataFrame(temperature_data)

# Знаходження середньої температури за місяць, виключаючи відсутні значення
mean_temperature = temperature_df['Температура'].mean()

# Заміна відсутніх значень температури середньою температурою за місяць
temperature_df['Температура'].fillna(mean_temperature, inplace=True)
print(temperature_df)
