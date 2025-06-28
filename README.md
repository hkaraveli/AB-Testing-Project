# A/B Test Analysis: Comparing Bidding Strategies (Maximum vs. Average)

**Author:** Halis Karaveli  
**Date:** 2025

---

## Project Overview

This project analyzes the impact of two digital marketing bidding strategies—Maximum Bidding and Average Bidding—on purchase conversion rates using A/B testing.  
The analysis is based on anonymized e-commerce data and demonstrates a full statistical workflow:  
- Data preparation
- Assumption checks
- Parametric/non-parametric hypothesis testing
- Visualization
- Practical recommendations

**Disclaimer:**  
This repository is based on an educational exercise from MIUUL Data Science Bootcamp.  
All code, analysis, and documentation are original, written by Halis Karaveli, and are provided for portfolio and demonstration purposes only.  
*No proprietary or paid data is shared in this repository. If you need data, you may simulate similar features or request access from the original provider.*

---

## Business Problem

A retail client is evaluating a new bidding strategy ("Average Bidding") introduced alongside the existing "Maximum Bidding" method. The goal is to determine if the new strategy leads to statistically significant improvements in purchase conversion rates.

---

## Dataset

- **impression**: Number of ad impressions
- **Click**: Number of ad clicks
- **Purchase**: Number of purchases following ad clicks
- **Earning**: Revenue earned from purchases

*Data was provided for educational use only. No original dataset is distributed here.*

---

## Methods

- Data exploration and visualization
- Independent two-sample t-test and Mann–Whitney U test
- Test of assumptions (Shapiro–Wilk, Levene)
- KPI visualization using Seaborn & Matplotlib
- Data-driven recommendations

---

## Example Results & Visualizations

**1. Distribution of Purchases per Group:**  
![Purchase Distribution](figures/purchase_distribution.png)

**2. Statistical Test Results:**  
| Metric           | Control Group | Test Group |
|------------------|--------------|------------|
| Purchase Mean    |  X.XX        |   X.XX     |
| t-test p-value   |   0.349      |            |

*No statistically significant difference was found between bidding strategies.*

---

## Usage

1. Clone the repository.
2. Place your data in the `datasets/` directory or simulate your own sample data.
3. Run:
    ```bash
    python ab_test_analysis.py
    ```

---

## Author

Halis Karaveli, 2025

---
