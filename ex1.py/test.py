import numpy as np
a=np.ones((3,1))
b=np.ones((1,3))
b=b.transpose()
print(a*b)