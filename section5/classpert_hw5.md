## Homework 5

1. You have a dataset of an input variable $ x $ and an output variable $ y $ below. Complete the code below to fit a linear regression using scikit-learn, and identify the coefficients for the slope and intercept. Don't worry about train/test splits for now. 


```python
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([91,70,95,6,56,13,46,21,72,35,91,35,84,62,51,39,17,58,42,60,39,85,51,0,90]).reshape(-1, 1)

Y = np.array([184.2,162.5,201.8,-4.4,133.0,25.2,91.4,47.2,149.0,43.9,197.9,71.7,163.1,
              132.2,94.9,92.8,20.1,132.7,78.3,141.6,87.4,175.9,90.0,5.8,167.3])

# Fit a line to the points
# Be sure to save the coefficients m and b to variables as well 
# ==================================

# ==================================

# show in chart
plt.plot(X, Y, 'o') # scatterplot
plt.plot(X, m*X+b) # line
plt.show()
```

2. Fit a logistic regression to [this data](https://bit.ly/3imidqa) that predicts a light/dark font for a given background color. Each data point contains red, green, and blue values composing the given background color and an output variable column indicating whether it belongs to a light (0) or dark (1) background color. Complete the code below by replacing the indicated comment block. 


```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load the data
df = pd.read_csv("https://bit.ly/3imidqa", delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Fit a line to the points
# Be sure to save the coefficients m and b to variables as well 
# ==================================

# ==================================

# Test a prediction
while True:
    n = input("Input a color {red},{green},{blue}: ")
    (r, g, b) = n.split(",")
    x = model.predict(np.array([[int(r), int(g), int(b)]]))
    if model.predict(np.array([[int(r), int(g), int(b)]]))[0] == 0.0:
        print("LIGHT")
    else:
        print("DARK")
```

3. Is there a strong correlation between $ X $ and $ Y $ below? Find the correlation coefficient, coefficient of determination, and p-value of the data.


```python
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([91,70,95,6,56,13,46,21,72,35,91,35,84,62,51,39,17,58,42,60,39,85,51,0,90])

Y = np.array([162.9,159.2,206.6,-21.9,109.5,26.7,103.7,51.6,136.7,57.8,192.9,52.9,193.0,
              139.6,66.2,96.1,43.3,139.8,76.1,163.1,88.6,157.4,76.2,21.2,138.9]) 

df = pd.DataFrame({"X": X, "Y" : Y})

# Calculate the correlation coefficient, coefficient of determination, and p-value below 
# ==========================================

# ==========================================
```
