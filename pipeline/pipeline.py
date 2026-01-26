import sys
import pandas as pd 

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"A" : [1, 3], "B" : [5, 6], "Month" : month})
print(df)

df.to_parquet(f"output_{month}.parquet")
