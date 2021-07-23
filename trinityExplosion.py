# Based on dimensional analysis, we use the data of radius of the shock front and time to estimate the yield of the
# bomb.


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Taylor studied the movie of Trinity test explosion
rho = 1.25
t = np.array(
    [0.1, 0.24, 0.38, 0.52, 0.66, 0.8, 0.94, 1.08, 1.22, 1.36, 1.5, 1.65, 1.79, 1.93, 3.26, 3.53, 3.8, 4.07, 4.34, 4.61,
     15, 25, 34, 53, 62]).reshape(-1, 1)
r = np.array(
    [11.1, 19.9, 25.4, 28.8, 31.9, 34.2, 36.3, 38.9, 41, 42.8, 44.4, 46, 46.9, 48.7, 59, 61.1, 62.9, 64.3, 65.6, 97.3,
     106.5, 130, 145, 175, 185])
ln_t = np.log(t)
ln_r = np.log(r)
reg = LinearRegression()
reg.fit(ln_t, ln_r)
print(reg.coef_)
# The result is very closed to 2/5, which is from the dimensional analysis
c = np.mean(5 * ln_r - 2 * ln_t)
E = rho * np.exp(c) * 1000000 / (4.182e12)  # unit - Joule, 1kt = 4.184e12 J
print(E)
