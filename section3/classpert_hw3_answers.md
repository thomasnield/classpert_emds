# Homework 3 (with answers)

1. You flipped a coin 25 times and got heads 19 times and tails 5 times. Do you think this coin has any good probability of being fair? Why or why not?


```python
from scipy.stats import beta

a = 19
b = 5

p = beta.cdf(.50, a, b)

# 0.001299738883972168
print(p)

# The coin is unfair with a .1% probability of a 50% probability or less of heads! 
```

    0.001299738883972168


We can visualize this area using matplotlib. Notice how tiny it is. 


```python
from scipy.stats import beta 
import matplotlib.pyplot as plt
import numpy as np 

a, b = 19, 5
x = np.arange(0, 1.01, .01)
y = beta.pdf(x, a, b)

upper_area_x = .5
x_area_range = (x <= upper_area_x)

plt.plot(x, beta.pdf(x, a, b))
plt.fill_between(x[x_area_range], y[x_area_range], 0, alpha=.5,  color='red')
plt.show()
```


    
![png](classpert_hw3_answers_files/classpert_hw3_answers_4_0.png)
    


2. There is a 30% chance of rain today, and a 40% chance your umbrella order will arrive on time. You are eager to walk in the rain today and cannot do so without either! What is the probability it will rain AND your umbrella will arrive?


```python
# joint probability is simple multiplication 
# .12 probability it will rain and your umbrella will arrive
.3 * .4 
```




    0.12



3. There is a 30% chance of rain today, and a 40% chance your umbrella order will arrive on time.You will be able to run errands only if it does not rain or your umbrella arrives. What is the probability it will not rain OR your umbrella arrives?


```python
# union probability is addition with the subtraction of joint probability. 
.3 + .4 - (.3 * .4) 
```




    0.58



4. There is a 30% chance of rain today, and a 40% chance your umbrella order will arrive on time. However, you found out if it rains there is only a 20% chance your umbrella will arrive on time. What is the probability it will rain AND your umbrella will arrive on time?


```python
# use the conditional probability in a joint probability if it is available and applicable 
.3 * .2 
```




    0.06



5. You have 175 passengers booked on a flight from. Las Vegas to Dallas. However, it is Las Vegas on a Sunday morning and you estimate each passenger is 30% likely to not. show up. You are trying to figure out how many seats to overbook so the plane does not fly empty. How likely is it that at least 50 passengers will not show up?


```python
from scipy.stats import binom

n = 175
p = 0.3

total_p = 0.0 

# add probabilities between 50 and 175 passengers
for k in range(50, n+1):
    total_p += binom.pmf(k, n, p)

print(total_p)
```

    0.6866320986767304

