import pandas as pd
import numpy as np
Fruit={'fruits':['apple','orange','banana','orange','guava','apple']}
df=pd.DataFrame(Fruit)
unique_value=np.unique(df['fruits'],return_index=True)
p=sorted(zip(unique_value[1],unique_value[0]))
ordered_unique=[x for _,x in p]
df['Ordinal_Encoded']=[ordered_unique.index(x) for x in df['fruits']]
print(df)
