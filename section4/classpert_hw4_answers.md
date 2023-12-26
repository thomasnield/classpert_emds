## Homework 4 (with answers)

1. You are measuring the life of a cheap capacitor in a circuit board, and obtained a small sample of these values (in days)

$
x = (656,694,558,618,613,687,744,703,591,665)
$

Calculate the mean, variance, and standard deviation of this sample. 


```python
from math import sqrt

sample = [656,694,558,618,613,687,744,703,591,665]

def mean(values):
    return sum(values) /len(values)

def variance_sample(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
    return var

def std_dev_sample(values):
    return sqrt(variance_sample(values))

mean = mean(sample)
var = variance_sample(sample)
std_dev = std_dev_sample(sample)

print("MEAN: ", mean) # 652.9
print("VAR: ", var) # 3273.8777777777777
print("STD DEV: ", std_dev) # 57.21780997012886
```

    MEAN:  652.9
    VAR:  3273.8777777777777
    STD DEV:  57.21780997012886


2. An Android tablet that came on the market a few years ago had data collected from random users to assess battery wear and tear. It was found that the battery would show significant failure on average at 24 months, with 3 months standard deviation. What is the probability the battery will last between 20 and 28 months? 


```python
from scipy.stats import norm

mean = 24
std_dev = 3

x = norm.cdf(28, mean, std_dev) - norm.cdf(20, mean, std_dev)

print(x) # 0.8175775605482642
```

    0.8175775605482642


3. I am skeptical that my 3D printer filament is not 1.75 mm in average diameter as advertised. I sampled 34 measurements with my tool. The sample mean is 1.715588 and the sample standard deviation is 0.029252. What is the 99% confidence interval for the mean of my entire spool of filament?


```python
from math import sqrt
from scipy.stats import norm

def critical_z_value(p, mean=0.0, std=1.0):
    norm_dist = norm(loc=mean, scale=std)
    left_area = (1.0 - p) / 2.0
    right_area = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(left_area), norm_dist.ppf(right_area)


def ci_large_sample(p, sample_mean, sample_std, n):
    # Sample size must be greater than 30

    lower, upper = critical_z_value(p)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))

    return sample_mean + lower_ci, sample_mean + upper_ci


print(ci_large_sample(p=.99, sample_mean=1.715588, sample_std=0.029252, n=34))
# (1.7026658973748656, 1.7285101026251342)
```

    (1.7026658973748656, 1.7285101026251342)


4. The 3D printer filament company told me they improved their processes so the filament was consistently closer to 1.74 mm. I recieved a new spool and took 34 measurements, and found I got a mean of 1.762. What is the p-value this observation was by random chance, and no change effectively happened? At a two-tailed threshold of .05, is it small enough to compel us they've made a meaningful change? 


```python
from scipy.stats import norm

mean = 1.715588 
sd = 0.029252

p = 1.0 - norm.cdf(1.762, mean, sd)

# P-value of both tails, 
# Take advantage of symmetry
p_value = p*2 

print("Two-tailed P-value", p_value)
if p_value <= .05:
    print("Passes two-tailed test")
else:
    print("Fails two-tailed test")

# Two-tailed P-value 0.01888333596496139
# Passes two-tailed test
```

    Two-tailed P-value 0.11259724934038529
    Fails two-tailed test

