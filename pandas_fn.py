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