import numpy as np
import matplotlib.pyplot as plt
x=["con.1","con.2", "con.3", "con.4", "con.5", "con.6" ]
y=[3.07, 3.79, 3.36, 3.37, 3.42, 3.37]
plt.xlabel('throughput')
plt.ylabel('Gbits/sec')
plt.bar(x,y)
plt.show()
