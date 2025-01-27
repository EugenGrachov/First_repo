import pandas as pd

mountains_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])

print(mountains_height)

box_200 = pd.Series([250000, 300000, 750000, 25000000])

print(box_200)

mountains_height = pd.Series(
data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
name="Height, m",
dtype=float,
)

print(mountains_height)

box_200 = pd.Series(
data=[250000, 300000, 750000, 25000000],
index=["Goblin", "Gremlin", "Barlog","Ork"],
name="Gut, pcs",
dtype=float,
)

print(box_200)

heroes = pd.Series(
data=[2000000, 55000000, 8000000, 960000000],
index=["Mazepa", "Bandera","Skoropadsky","Sirko"],
name="Shanovni gromadyane",
dtype=float
)

print(heroes)

print(heroes[0]) # 2000000
print(heroes["Mazepa"]) # 2000000

print(mountains_height[["Pip_Ivan", "Goverla", "Gutin_Tomnatik"]])
print(heroes[["Mazepa", "Sirko", "Skoropadsky"]]) # 2000000

print(mountains_height[1:3])
print(mountains_height["Brebenskyl":"Petros"])

print(mountains_height.Petros) # 2022.5
print(mountains_height.Brebenskyl) # 2035.8

print(mountains_height > 2030)
print(mountains_height[mountains_height > 2030])

print(heroes > 200000)

print("Goverla" in mountains_height) # True

sort_index = mountains_height.sort_index()
print(sort_index)

sort_index = mountains_height.sort_index()
print(sort_index)

mountains_height.sort_values(inplace=True, ascending=False)
print(mountains_height)

mountains_height = pd.Series(
	{"Goverla": 2061, "Brebenskyl": 2035.8, "Pip_Ivan": 2028.5},
	index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
	name="Height, m",
	dtype=float,
)

print(mountains_height)

mountains_height.fillna(0, inplace=True)

print(mountains_height)

def square(x):
	return x**2

squared_height = mountains_height.apply(square)
print(squared_height)


# mountains_height.plot(kind='bar')  not worked

other_mountains = pd.Series([2001.1, 1998.4], index=['Rebra', 'Menchul'])
all_mountains = pd.concat([mountains_height, other_mountains])
print(all_mountains)
