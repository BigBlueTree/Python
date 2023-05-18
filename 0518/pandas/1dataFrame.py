import numpy as np
import pandas as pd


np.random.seed(0)
arr = np.random.randint(10, size=(2,2))
print(arr)

dfa=pd.DataFrame(arr,copy=False)
dfb=pd.DataFrame(arr,copy=True)
arr[0,0]=100
print(dfa)
print(dfb)