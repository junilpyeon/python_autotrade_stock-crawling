import numpy as np
import pandas as pd

df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Coconut', 2, 6, 'Fruit'],
    ['Rice', 8, 2, 'Meal'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])

df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency",
    aggfunc=np.max
)
print(df)
