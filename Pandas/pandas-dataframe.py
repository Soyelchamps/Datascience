import pandas as pd
d = {
    "one": pd.Series([1.0, 2.0, 3.0, 4.5, 7], index=["a", "b", "c", "e", "f"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(d)

print(df)
df.to_csv("out.csv")
