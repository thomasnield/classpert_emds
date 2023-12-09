import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x = np.array([84,37,58,52,47,78,93,15,12,60]).reshape(-1, 1)
y = np.array([155.8,102.0,164.8,120.9,86.8,93.0,201.6,25.2,14.7,118.6])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3)

lr = LinearRegression().fit(x_train, y_train)

result = lr.score(x_test, x_test)
print(f"r^2: {result}") # r^2: -15.9340823907845