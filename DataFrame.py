import pandas as pd

data1 = [[1, 'Alice'], [2, 'Bob']]
df = pd.DataFrame(data1, columns=['ID', 'Name'])
print(df)

data2 = {'ID': [1,2], 'Name': ['Alice', 'Bob']}
dft = pd.DataFrame(data2)
print(dft)

import numpy as np

data = np.array([[1, 'Alice'], [2, 'Bob']])
df = pd.DataFrame(data, columns=['ID', 'Name'])
print(df)

import pandas as pd

data3 = {'A': [1, 2], 'B': [3, 4]}
dfre = pd.DataFrame(data3)
print(dfre.shape) # Виведе: (2, 2)

print(df.columns) # Виведе: Index(['A', 'B'], dtype='object')
print(df.index) # Виведе: RangeIndex(start=0, stop=2, step=1) 
print(df.dtypes)
# Виведе:
# A    int64
# B    int64
# dtype: object

import pandas as pd

contacts = pd.DataFrame(
   {
      "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
      ],
      "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
      ],
      "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
      ],
      "favorite": [False, False, True, False, True],
	},
	index=[1, 2, 3, 4, 5],
)

print(contacts)

print(contacts["name"])

print(contacts.loc[1])

print(contacts.iloc[1])

print(contacts[0:2])

print(contacts[contacts["favorite"]])

contacts.set_index('name', inplace=True)
print(contacts)

df.rename(columns={'name': 'Full Name'}, inplace=True)

df = df.rename(columns={'name': 'Full Name'})

contacts.reset_index(inplace=True)
print(contacts)

contacts['favorite'] = contacts['favorite'].astype('int64')
print(contacts.dtypes)

contacts.rename(columns={'name': 'Full Name', 'email': 'Email Address'}, inplace=True)
print(contacts)

df.fillna(0, inplace=True) # Замінює всі NaN на 0
df.fillna(method='ffill', inplace=True) # Заповнює NaN попереднім значенням у рядку

import pandas as pd
import numpy as np

df = pd.DataFrame({
   'A': [1, np.nan, 3],
   'B': [np.nan, 5, np.nan]
})

# Застосування методу 'ffill'
df_ffill = df.fillna(method='ffill')

# Застосування методу 'bfill'
df_bfill = df.fillna(method='bfill')

print("Using ffill:")
print(df_ffill)

print("\\nUsing bfill:")
print(df_bfill)

df.dropna(inplace=True) # Видаляє всі рядки, які містять хоча б один NaN
df.dropna(axis=1, inplace=True) # Видаляє всі стовпці, які містять хоча б один NaN
df.dropna(subset=['column_name'], inplace=True) # Видаляє рядки, де NaN в стовпці 'column_name'

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
})

# Видалити рядки, де є NaN у стовпці 'B'

df.dropna(subset=['B'], inplace=True)
print(df)
