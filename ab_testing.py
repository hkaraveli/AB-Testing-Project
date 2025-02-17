######################################################
# Basic Statistical Concepts
######################################################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

############################
# Sampling
############################

population = np.random.randint(0, 80, 10000)
population.mean()

np.random.seed(115)

sample = np.random.choice(a=population, size=100)
sample.mean()

np.random.seed(10)
sample1 = np.random.choice(a=population, size=100)
sample2 = np.random.choice(a=population, size=100)
sample3 = np.random.choice(a=population, size=100)
sample4 = np.random.choice(a=population, size=100)
sample5 = np.random.choice(a=population, size=100)
sample6 = np.random.choice(a=population, size=100)
sample7 = np.random.choice(a=population, size=100)
sample8 = np.random.choice(a=population, size=100)
sample9 = np.random.choice(a=population, size=100)
sample10 = np.random.choice(a=population, size=100)

(sample1.mean() + sample2.mean() + sample3.mean() + sample4.mean() + sample5.mean()
 + sample6.mean() + sample7.mean() + sample8.mean() + sample9.mean() + sample10.mean()) / 10

############################
# Descriptive Statistics
############################

df = sns.load_dataset("tips")
df.describe().T

############################
# Confidence Intervals
############################

df = sns.load_dataset("tips")
df.describe().T
df.head()

sms.DescrStatsW(df["total_bill"]).tconfint_mean()
sms.DescrStatsW(df["tip"]).tconfint_mean()

df = sns.load_dataset("titanic")
df.describe().T
sms.DescrStatsW(df["age"].dropna()).tconfint_mean()
sms.DescrStatsW(df["fare"].dropna()).tconfint_mean()

######################################################
# Correlation
######################################################

df = sns.load_dataset('tips')
df.head()

df["total_bill"] = df["total_bill"] - df["tip"]

df.plot.scatter("tip", "total_bill")
plt.show()

df["tip"].corr(df["total_bill"])

######################################################
# A/B Testing (Independent Two-Sample T-Test)
######################################################

# 1. Define Hypotheses
# 2. Assumption Checks
#   - 1. Normality Assumption
#   - 2. Homogeneity of Variance
# 3. Applying the Hypothesis Test
#   - 1. If assumptions are met, apply independent two-sample t-test (parametric test)
#   - 2. If assumptions are not met, apply the Mann-Whitney U test (non-parametric test)
# 4. Interpret results based on p-value

############################
# Application 1: Is There a Statistically Significant Difference Between Smokers and Non-Smokers in Terms of Bill Amounts?
############################

df = sns.load_dataset("tips")
df.head()

df.groupby("smoker").agg({"total_bill": "mean"})

############################
# 1. Define Hypotheses
############################

# H0: M1 = M2 (No significant difference)
# H1: M1 != M2 (There is a significant difference)

############################
# 2. Assumption Checks
############################

# Normality Assumption
# H0: Data follows a normal distribution
# H1: Data does not follow a normal distribution

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "Yes", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Homogeneity of Variance
# H0: Variances are homogeneous
# H1: Variances are not homogeneous

test_stat, pvalue = levene(df.loc[df["smoker"] == "Yes", "total_bill"],
                           df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

############################
# 3. Apply the Hypothesis Test
############################

# 1.1 If assumptions are met, apply independent two-sample t-test (parametric test)
test_stat, pvalue = ttest_ind(df.loc[df["smoker"] == "Yes", "total_bill"],
                              df.loc[df["smoker"] == "No", "total_bill"],
                              equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# 1.2 If assumptions are not met, apply the Mann-Whitney U test (non-parametric test)
test_stat, pvalue = mannwhitneyu(df.loc[df["smoker"] == "Yes", "total_bill"],
                                 df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
