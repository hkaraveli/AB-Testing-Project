# AB-Testing-Project

## 📌 Project Overview
This project analyzes the impact of **Maximum Bidding vs. Average Bidding** strategies in **A/B testing** to optimize conversion rates. It uses statistical hypothesis testing to determine which strategy is more effective.

## 📊 Dataset
- The dataset includes **user interactions and conversion data** collected from an online platform.
- Key columns: `user_id`, `group (control/test)`, `clicks`, `conversions`, `impressions`.

## 🔬 Methodology
1. **Data Cleaning & Preprocessing**:
   - Handling missing values, duplicates, and data type conversions.
2. **Exploratory Data Analysis (EDA)**:
   - Visualizing key metrics (e.g., conversion rates per group).
3. **Statistical Hypothesis Testing**:
   - Using **t-tests** and **chi-square tests** to compare group performance.
4. **Decision Making**:
   - Interpreting p-values to decide whether Maximum Bidding or Average Bidding performs better.

## 🛠 Technologies Used
- **Python**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`
- **Statistical Methods**: `t-tests`, `chi-square test`, `confidence intervals`
- **Jupyter Notebook**: For analysis and visualization

## 🚀 How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/hkaraveli/AB-Testing-Project.git
   cd AB-Testing-Project
