import mylib
import pandas as pd

csvpath = 'en01space.csv'



df = pd.read_csv(csvpath, delimiter=',')
dfnp = df.to_numpy()




