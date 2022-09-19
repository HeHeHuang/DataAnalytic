## Data Type:

There are two elements of structured data: numerical (continous and discrete) and cateogirical (Norminal and oridinial )

### Estimate of Location

Mean ,median, Trimmed Mean(more Robust)



**why median is robust than Mean?**

because the mean is impacted by outliner, and median is only care about the middle value



### Estimate of Variability  

Standard deviation

Range

Variance



#### Exploring Categorical Data

Mode

Expected value: sum of probability(X)*X. **Statistical Mean**



### Vasulization for different data type 

1. numerial data type: precentile, box plot, histograms, density plots
2. category data type: frequecy table  



## Sampling distribution

there is an distribution that we take samples from it.

we calcuate the sample statistics for sample such as mean. then iteration, we obtain the samples mean distribution.

#### Standard error

standard deviation of these sample means 

#### confidence interval

90% means the interval cover the 90% of sample means

### Central Limit Theorem

as the sample size bigger, the sample distribution will more like normal distribution. no matter which distribution we take sample from.



## Probability distribution

Y-axis: f(x) X-axis: x. the probability is the area of curve 

probability distribution can be divided into two types: discrete and continuous 

### normal distribution

### binomial distribution

### chi-square distribution

### F-distribution

#### poison distributions

the probability distribution of frequency of random event 

#### Exponential distribution

the probability distribution of time interval between events

#### why we need know probability of distribution

the data distribution for training set and test set is similar, the machine learning will be meaningful.





## Hypothesis:(signification Hypothoesis Testin)

we have hypothesis first and assume the H0 is correct, we try to use the **sample statistics** to find out the **P value**. the p- value is the probability of small probabity event. if the small probability event happened, we can reject the H0, if not we accpet.



#### Type 1 & Type 2 Error:

we use samples to decide whether the pupulatition parameter is ture.

type 1 error: means the H0 is true, but after the sample estimation, we reject the H0

type2 error means the H0 is false, but after the sample estimation, we accpet the H0 



### A/B Testing



### T Test: 

#### indenpent T test

use to the sample size < 30 and the SD of populuation is unknown.

independt T Test: the weight of people who smoke is different. 

H0: the mean of people smoke = the mean of general people

#### Paired T test:

one indenpent variable(two categories) with one dependent variable(continuous value)

for example:  find out weight of male and female is statistically signification.

H0: the weitht of male and that of femal is no different 



#### Chi Square Test:

two categories variable 



#### Anova(Analysis of variance):

mulitple categories with on dependent variable(continuous value)

test whether means of each categories is equal 



#### Permutation Test

user for the sample data is from unknow distribution

eg: purpose: find out whether the new teaching method is better than current method 

**Step**:  

1. there are two groups, that one group is using the new teaching method, one is still using old method 
2. calculate the differences of mean of two groups.
3. mix two group together and random combination samples for two groups
4. calculate the differnences of mean of two groups and then repeat 1000 times.
5. calculate the P-value = N (greater than original mean difference ) /1000
6. based on P-value to reject or accept the null hypothesis











