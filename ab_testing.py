"""
A/B Test Analysis: Comparing Maximum vs. Average Bidding
Author: Halis Karaveli, 2025

This script demonstrates a complete A/B testing workflow using simulated data for demonstration purposes.
Original dataset used in MIUUL Bootcamp is NOT shared here due to copyright and educational restrictions.
You can run the script with your own data in the format expected or rely on simulated data by default.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu

os.makedirs("figures", exist_ok=True)

# --- Load Data ---
try:
    df_control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
    df_test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")
except FileNotFoundError:
    # Simulate data for demonstration if not available
    np.random.seed(42)
    df_control = pd.DataFrame({
        "impression": np.random.randint(5000, 20000, 40),
        "Click": np.random.randint(200, 900, 40),
        "Purchase": np.random.normal(35, 5, 40).astype(int),
        "Earning": np.random.normal(600, 80, 40)
    })
    df_test = pd.DataFrame({
        "impression": np.random.randint(5000, 20000, 40),
        "Click": np.random.randint(200, 900, 40),
        "Purchase": np.random.normal(36, 5, 40).astype(int),
        "Earning": np.random.normal(605, 75, 40)
    })

df_control["group"] = "control"
df_test["group"] = "test"
df = pd.concat([df_control, df_test], ignore_index=True)

# --- Exploratory Visualization ---
plt.figure(figsize=(7, 4))
sns.histplot(df, x="Purchase", hue="group", bins=20, kde=True, element="step")
plt.title("Purchase Distribution by Group")
plt.savefig("figures/purchase_distribution.png", dpi=120)
plt.close()

# --- Assumption Checks ---
def check_normality(data, group):
    stat, p = shapiro(data)
    print(f"Shapiro–Wilk for {group}: p={p:.3f}")
    return p > 0.05

def check_variance(x, y):
    stat, p = levene(x, y)
    print(f"Levene’s Test: p={p:.3f}")
    return p > 0.05

normal_control = check_normality(df.loc[df.group == "control", "Purchase"], "Control")
normal_test = check_normality(df.loc[df.group == "test", "Purchase"], "Test")
variance = check_variance(df.loc[df.group == "control", "Purchase"], df.loc[df.group == "test", "Purchase"])

# --- Hypothesis Testing ---
if normal_control and normal_test and variance:
    stat, p = ttest_ind(df.loc[df.group == "control", "Purchase"],
                        df.loc[df.group == "test", "Purchase"],
                        equal_var=True)
    test_used = "Independent Two-Sample T-Test"
else:
    stat, p = mannwhitneyu(df.loc[df.group == "control", "Purchase"],
                           df.loc[df.group == "test", "Purchase"])
    test_used = "Mann–Whitney U Test"

print(f"\n{test_used} p-value: {p:.3f}")

# --- KPI Visualization ---
means = df.groupby("group")["Purchase"].mean()
plt.figure(figsize=(6, 4))
sns.barplot(x=means.index, y=means.values)
plt.title("Average Purchases by Group")
plt.ylabel("Mean Purchase")
plt.savefig("figures/mean_purchase.png", dpi=120)
plt.close()

# --- Show Group Means ---
print("\nGroup Means (Purchases):")
print(means)

# --- Final Recommendation ---
if p < 0.05:
    print("Statistically significant difference found between bidding methods!")
else:
    print("No statistically significant difference found. Consider other business metrics or longer test duration.")
