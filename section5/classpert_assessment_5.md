# Section 5
## Assessment Questions

1. True or False: linear regression is a form of machine learning.

   a. True [correct answer]

   b. False

FEEDBACK: A linear regression is the most basic form of machine learning, or more specifically supervised machine learning. We are fitting a function (a linear function) to data and hoping to make effective generalizations of the data for analysis and prediction. 

2. How do you calculate the sum of squares?

   a. Square each input variable value and sum them

   b. Square the residuals (differences between predicted y-values and actual y-values) and sum them [correct answer]

   c. Calculate the average of the residuals (differences between predicted y-values and actual y-values)

   d. Take the absolute values of the residuals (differences between predicted y-values and actual y-values) and sum them

FEEDBACK: The sum of squares will calculate the squared residuals, the differences between the predicted y-values and actual y-values, and sum them together. This is a way to measure how closely the line is fit to the points. 

3. What is the most efficient, stable, and scalable way to perform linear regression?

   a. Gradient descent

   b. Inverse matrices

   c. Hill climbing

   d. QR Decomposition [correct answer]

FEEDBACK: The most scalable and stable way to fit a linear regression is using the linear algebra decomposition technique called QR decomposition. It will ensure floating point arithmetic minimizes errors and efficiently fit a line using least squares. 

4. True or false: When you fit a linear regression using a least squares method, you have an effective model to analyze variable relationships and make predictions.

   a. True

   b. False [correct answer]

FEEDBACK: Just because you fit a linear regression to some data does not mean the model is going to perform well. There are other concerns like correlation, p-values, overfitting, and bias that have to be considered. 

5. The raw output of a logistic regression is...

   a. A binary output variable

   b. A probability output variable [correct answer]

   c. A real positive/negative floating point number

   d. None of the above

FEEDBACK: A logistic regression is going to strictly output a probability between 0 and 1. However, you can use that probability with a threshold to assign it a True/False or even a category. 

6. True or false: A logistic regression only supports true/false categories and cannot extend to more categories.

   a. True

   b. False [correct answer]

A logistic regression CAN be extended to support multiple categories, one way being to create a separate logistic regression for each category and choosing the one with the highest probability. 
