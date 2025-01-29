import pandas as pd

employees = pd.read_json("./json/split.json", orient="split")

print(employees)