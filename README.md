
# n Adjusted Pvalue Packages
In the face of the Large N problem, this package reports what your p-values would be if your sample was instead shrunk to $n = 100$. 

>BEWARE: This assumes that the mean and standard error are the same between your sample and the smaller sample.

There are two packages:
- <em>nAdjPval</em>: This can directly take your basic linear regression result (via Python's <em>sm.OLS(y, X).fit()</em> )
- <em>nAdjCalc</em>: If you didn't run your regression in Python, you can directly input your sample size as well as your t-scores (for each variable of your model) into this calculator (either individually, or as a group of p-values)

## nAdjPval Package
As for how this package works, it directly takes your basic linear regression result (via Python's <em>sm.OLS(y, X).fit()</em> ) as an input and prints a table with the new p-values that will attach to the bottom of your initial regression result.
- INPUT: Basic regression result
- <em> (Optional) </em> RETURN: Dataframe with the new p-values in one column, and the variable names in the other column

### Example 1

#### Set Up
Here we're going to randomly generate a data with $n=10,000$ and run a basic linear regression

```python
import random
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Randomly generate x1, x2 and y for our regression
np.random.seed(27)
x1 = pd.Series(np.random.randn(n))
np.random.seed(100)
x2 = pd.Series(np.random.randn(n))
np.random.seed(54)
y1 = pd.Series(np.random.randn(n))

# Run our regression
X1 = pd.DataFrame(index=range(len(x1)),columns=range(0))
X1['x'] = x1
X1['x2'] = x2
X1['constant'] = 1  
reg1 = sm.OLS(y1, X1).fit()

# Show our regression results
model1 = reg1.summary()
print(model1)
```

#### Now let's adjust our p-values!
Now we're going to adjust our p-values
```python
# pip install nAdjPval
	# to install the library if necessary

from nAdjPval import nAdjPval

df = nAdjPval(reg1)
print(df)
```
>BEWARE: Do NOT drop the <em>from</em> syntax, it won't work!

## nAdjCalc Package
This package is incredibly similar to the above package, the key difference is in the input type. So if you didn't run your regression directly in Python, you can simply input your sample size and t-score(s) to get the new p-values.

INPUT: ($n$,$tScore$). $n$ stands for your data's sample size \& $tScore$ is 1 variable that can be either:
- a one decimal number (float)
- a one integer number
- a <em>one column</em> dataframe
- a series
- a list <em>(with ONLY floats or integers)</em>
- a <em>one column</em> array

RETURN <em> (Required) </em>: The new p-value(s), these will be the same data type as your input

### Example 2

#### Set Up

Here suppose you already ran a basic linear regression of $x$ on $y$ and got a t-Score of $0.219$ for $x$ in your results. We'll use the same $n=10,000$ as Example 1.

```python
# pip install nAdjPval
	# to install the library if necessary

from nAdjPval import nAdjCalc

n=10000
tScore=.219

# Now let's adjust our p-values!
pVal_fromCalc = nAdjCalc(n,tScore)
print(pVal_fromCalc)
```
>BEWARE: Do NOT drop the <em>from</em> syntax, it won't work!

#### Handling multivariate regressions
The introduction introduced the different type of inputs this package will accept for the variable $tScore$. The code below gives a template that shows the different types of acceptable inputs.

```python
# pip install nAdjPval
	# to install the library if necessary

from nAdjPval import nAdjCalc

n=10000

# 
tScore = pd.DataFrame([.219, 2.784, .219])		# Dataframe
# tScore = pd.Series([.219, 2.784, .219])		# Series
# tScore = [.219, 2.784, .219]  				# List
# tScore = np.array([.219, 2.784, .219])		# Array

# Now let's adjust our p-values!
pVal_fromCalc = nAdjCalc(n,tScore)
print(pVal_fromCalc)
```

## Details on How these Packages Work

This is inspired by the methodology proposed in Good (1988) "The Interface between Statistics and Philosophy of Science", and does so as follows:

$$tScore_{new}=tScore_{orig}\cdot\frac{\sqrt{n_{100}}}{\sqrt{n_{original}}}$$

This new $tScore$ then gives a new $pValue$.
>This is incredibly valuable because you'll see that large sample sizes can immensely skew what the p-values are (compared to what they should be).