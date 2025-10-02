import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint

p = np.pi
y0 = 1
num = 5
# print("pi = \n", p)
xx = np.arange(0.0, 2.01, .01)

functs = dict()
for n in range(num):
    yy = y0*np.sin(n*p*xx)
    functs[f"n={n}"] = yy
    
f = pd.DataFrame(functs, index=xx)
f.index.name = "x"
f['sum'] = f.sum(axis=1)        
pprint(f)

    
for col in f.columns:
    if col == "sum":
        plt.plot(f.index, f[col], label=col, linewidth=2.5, linestyle="--")
    else:
        plt.plot(f.index, f[col], label=col)
plt.legend(title="columns")
plt.xlabel("position (x)")
plt.ylabel("Amplitude")
plt.title("wave harmonics")
plt.grid(True)
plt.show()



