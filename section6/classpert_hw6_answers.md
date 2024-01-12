# Homework 6

1. Perform a train/test split on this background color and light/dark font prediction dataset using a logistic regresion. 


```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np

# Load the data
df = pd.read_csv("light_dark_font_training_set.csv", delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

model = LogisticRegression(solver='liblinear')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.33)
model.fit(X_train, Y_train)
prediction = model.predict(X_test)

"""
The confusion matrix evaluates accuracy within each category.
[[truepositives falsenegatives]
 [falsepositives truenegatives]]

The diagonal represents correct predictions,
so we want those to be higher
"""
matrix = confusion_matrix(y_true=Y_test, y_pred=prediction)
print(matrix)
```

    [[166   1]
     [  1 276]]


2.  You have decided to take on Stanley Tumblers and come up with your own tumbler that you believe will keep drinks cooler longer. You create two linear regressions, one for the Stanley Tumbler and one for yours. The x-axis is the environment temperature and the y-axis is the number of hours before reaching room temperature. You collected 60 data points off each tumbler. What are some confounding factors to consider and control for in this experiment when you compare the results? 

3. Your executive director oversees 12 departments in a company of 2000 people, ranging from airport operations to accounting and IT. 
She tasks you to create and lead a “data science” team of 20 people 
This data science team will “rove” and aid each of the 12 departments to make them more “data-driven,” apply machine learning, and break down data siloes that exis .
Is this objective reasonable? What opportunities/challenges lie ahe?



4. You work at an airline. 
As aircraft age, maintenance costs increase, and the manufacturer is not delivering planes fast enough.
Your director wants to hire a data scientist who can app machine learningng to plan the retirement schedule of aircraft to minimize losses without shrinking the fleet too quickl .
The director knows that a single data scientist/deep learning job will get hundreds of applications, and reasons one capable candidate should exist in that po l.
Is this the right talent strategy? Why or why nt? 


5. You work at a specialty laptop manufacturer and as the data scientist, your boss hands you an assignment. He wants you to show that their laptop battery life is slightly superior to competitors and gives no more direction or details. What do you do in this situation? How would you go about collecting data? How would you explain and approach the results to your manager? 


```python

```
