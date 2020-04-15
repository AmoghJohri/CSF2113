import pandas as pd
import matplotlib as plt



data = pd.read_csv("items.csv")

X = pd.DataFrame(data)
print(X.head(1))
