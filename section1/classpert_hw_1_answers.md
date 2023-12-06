# Homework 1 (with answers)
## Linear Algebra

1. Perform the matrix-vector multiplication below by hand or using NumPy or Sympy:
    
    $
    \left[\begin{matrix}1 & 3\\4 & -1\end{matrix}\right] \left[\begin{matrix}3\\2\end{matrix}\right]  = ?
    $
   

### Numpy Answer: 


```python
import numpy as np 

A = np.array([[1, 3],[4, -1]]) 
v = np.array([3, 2])

A @ v # array([ 9, 10])
```




    array([ 9, 10])



### SymPy Answer: 


```python
from sympy import * 

A = Matrix([[1, 3],[4, -1]]) 
v = Matrix([3, 2])

A @ v
```




$\displaystyle \left[\begin{matrix}9\\10\end{matrix}\right]$



2. Vector $ \vec{w} = \begin{bmatrix} 3 \\ -1 \end{bmatrix} $ is the transformation of vector $ \vec{v} $, where the linear transformation was the result of matrix $ \left[\begin{matrix}1 & 3\\4 & -1\end{matrix}\right] $. What was vector $ \vec{v} $?



### Numpy Answer: 


```python
import numpy as np 
from numpy.linalg import inv 

A = np.array([[1, 3],[4, -1]])
w = np.array([3, -1])

inv_A = inv(A)

v = inv_A @ w 
v 
```




    array([0., 1.])



### SymPy Answer: 


```python
from sympy import*  

A = Matrix([[1, 3],[4, -1]])
w = Matrix([3, -1])

inv_A = A.inv()

v = inv_A @ w 
v 
```




$\displaystyle \left[\begin{matrix}0\\1\end{matrix}\right]$



3. Is the matrix $ \left[\begin{matrix}2 & 1\\6 & 3\end{matrix}\right] $ linearly dependent? Why or why not?


### Numpy Answer: 


```python
import numpy as np 
from numpy.linalg import det 

A = np.array([[2, 1],[6,3]])
det(A) # -3.330669073875464e-16
```




    -3.330669073875464e-16



### SymPy Answer: 


```python
from sympy import * 

A = Matrix([[2, 1],[6,3]])
det(A) # 0 
```




$\displaystyle 0$




4. Solve the following system of equations:

   $
   50x + 3y + 2z = 25
   $

   $
   x - 2y + 12z = 12
   $

   $
   8x + 5y + 2z = 5
   $

### Numpy Answer: 


```python
from numpy import array
from numpy.linalg import inv

# 50x + 3y + 2z = 25
# x - 2y + 12z = 12
# 8x + 5y + 2z = 5

A = array([
    [50, 3, 2],
    [1, -2, 12],
    [8, 5, 2]
])

B = array([
    25,
    12,
    5
])

X = inv(A) @ B 

print(X) # [ 0.47009736 -0.12795549  0.9394993 ]
```

    [ 0.47009736 -0.12795549  0.9394993 ]


### SymPy Answer: 


```python
from sympy import *


# 50x + 3y + 2z = 25
# x - 2y + 12z = 12
# 8x + 5y + 2z = 5

A = Matrix([
    [50, 3, 2],
    [1, -2, 12],
    [8, 5, 2]
])

B = Matrix([
    25,
    12,
    5
])

X = A.inv() * B

print(X) # Matrix([[338/719], [-92/719], [1351/1438]])
```

    Matrix([[338/719], [-92/719], [1351/1438]])


5. For discussion in the next cohort, what are some other applications of linear algebra you can think of? How would vectors, matrices, and linear transformations be used in systems you touch every day?

* Computer games
* Flight simulators
* Computer graphic editors
* Weather data
* Engineering specifications
* Machine learning
* Data storage
* Networking 
