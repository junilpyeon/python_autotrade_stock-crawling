import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randint(1, 10, (4, 4)),
    index=[['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
    columns=['1회', '2회', '3회', '4회']
)

print(df)
print(df[["1회", "2회"]].loc["2차"])
