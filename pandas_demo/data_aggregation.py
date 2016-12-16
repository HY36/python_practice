import pandas as pd
from numpy.random import seed
from numpy.random import rand
from numpy.random import random_integers
import numpy as np

seed(42)

df = pd.DataFrame({'Weather' : ['cold', 'hot', 'cold', 'hot','cold', 'hot', 'cold'],
                   'Food' : ['soup', 'soup', 'icecream', 'chocolate','icecream', 'icecream', 'soup'],
                   'Price' : 10 * rand(7),
                   'Number' : random_integers(1, 9, size=(7,))})
print(df)
weather_group = df.groupby('Weather')
i = 0
for name, group in weather_group:
    i += 1
    print("Group", i, name)
    print(group)

print(weather_group.first())
print(weather_group.last())
print(weather_group.mean())
wf_group = df.groupby(['Weather', 'Food'])
print(wf_group.groups)
print(wf_group.agg([np.mean, np.median]))