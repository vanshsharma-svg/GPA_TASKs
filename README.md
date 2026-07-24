# 📱 Google Play Store Data Analysis using Python

<p align="center">

## 🚀 End-to-End Data Analytics Project

**Data Cleaning • Exploratory Data Analysis (EDA) • Business Insights • Advanced Visualizations**

**👨‍💻 Author:** **Vansh Sharma**

</p>

---

# 📌 Project Overview

This project presents an **end-to-end data analysis** of the Google Play Store dataset using **Python** and popular data analytics libraries.

The project focuses on extracting meaningful insights from Android application data through **data preprocessing, exploratory data analysis (EDA), advanced filtering, KPI generation, and interactive visualizations**.

Real-world business rules such as **multilingual category translation, conditional highlighting, advanced filtering, and time-based visualization control** have been implemented to simulate practical business intelligence scenarios.

---

# 🎯 Project Objectives

- 📱 Analyze Google Play Store application performance.
- ⭐ Study relationships between ratings, reviews, installs, and pricing.
- 📊 Perform Exploratory Data Analysis (EDA).
- 📈 Create meaningful business visualizations.
- 🔍 Apply advanced filtering conditions.
- 🌍 Implement multilingual category translations.
- ⏰ Apply time-based visualization controls.
- 💡 Generate business insights for better decision making.

---

# 🛠️ Technologies & Libraries Used

## 💻 Programming Language

- Python

## 📊 Data Analysis

- Pandas
- NumPy

## 📈 Data Visualization

- Matplotlib
- Seaborn
- Plotly

## ⏰ Date & Time Handling

- datetime
- pytz

## 📓 Development Environment

- Jupyter Notebook
- Visual Studio Code (VS Code)

---

# 📂 Dataset Information

**Dataset:** Google Play Store Dataset

**Source:** Kaggle

**Format:** CSV

The dataset contains application details including:

- 📱 App Name
- 📂 Category
- ⭐ Rating
- 💬 Reviews
- 📥 Installs
- 📦 Size
- 💲 Price
- 🏷️ Type
- 👨‍👩‍👧 Content Rating
- 🎮 Genres
- 📅 Last Updated
- 🔖 Current Version
- 🤖 Android Version

---

# 🧹 Data Preprocessing

The dataset was cleaned and transformed before analysis.

### ✔ Cleaning Steps

- Removed corrupted records.
- Removed duplicate applications.
- Handled missing values.
- Converted **Installs** into numeric format.
- Converted **Reviews** into integer format.
- Converted **Size** into MB.
- Converted **Last Updated** into datetime format.
- Standardized categorical values.
- Performed feature engineering.
- Prepared data for visualization and business analysis.

---

# 🚀 Tasks Implemented

# ✅ GPA TASK 1 – Grouped Bar Chart

## 🎯 Objective

Compare the **Average Rating** and **Total Reviews** of the **Top 10 app categories** based on installs.

### 🔍 Business Rules Applied

- ⭐ Rating ≥ **4.0**
- 📦 App Size ≥ **10 MB**
- 📅 Last Updated Month = **January**
- ⏰ Visualization available only between **3 PM – 5 PM IST**

### 📊 Visualization

- Grouped Bar Chart
- Category-wise comparison of Ratings and Reviews

---

# ✅ GPA TASK 2 – Interactive Choropleth Map

## 🎯 Objective

Visualize application installs geographically using an **Interactive Plotly Choropleth Map**.

### 🔍 Business Rules Applied

- 📈 Top **5 Categories**
- 📥 Installs > **1 Million**
- 🚫 Excluded categories starting with:
  - A
  - C
  - G
  - S
- ⏰ Visualization available only between **6 PM – 8 PM IST**

### 📊 Visualization

- Interactive Choropleth Map

---

# ✅ GPA TASK 3 – Dual Axis Chart

## 🎯 Objective

Compare **Average Installs** and **Revenue** for **Free vs Paid Applications**.

### 🔍 Business Rules Applied

- 📥 Installs > **10,000**
- 💰 Revenue > **$10,000**
- 🤖 Android Version > **4.0**
- 📦 App Size > **15 MB**
- 👨‍👩‍👧 Content Rating = **Everyone**
- 🔤 App Name Length ≤ **30 Characters**
- ⏰ Visualization available only between **1 PM – 2 PM IST**

### 📊 Visualization

- Dual Axis Chart

---

# ✅ GPA TASK 4 – Area Chart

## 🎯 Objective

Analyze **Monthly Install Growth** across different application categories.

### 🔍 Business Rules Applied

- 📈 Growth > **20% Month-over-Month**
- 💬 Reviews > **500**
- 🚫 App names should not start with:
  - X
  - Y
  - Z
- 🚫 App names should not contain **"S"**
- 📂 Categories should start with:
  - B
  - C
  - E

### 🌍 Category Translation

- Beauty → Hindi
- Business → Tamil
- Dating → German

### 📊 Visualization

- Area Chart

---

# ✅ GPA TASK 5 – Stacked Area Chart

## 🎯 Objective

Visualize **Cumulative Installs Over Time** across application categories.

### 🔍 Business Rules Applied

- ⭐ Rating ≥ **4.2**
- 💬 Reviews > **1,000**
- 📦 App Size between **20 MB – 80 MB**
- 🔤 App names without numerical characters
- 📂 Categories starting with:
  - T
  - P

### 🌍 Category Translation

- Travel & Local → **French**
- Productivity → **Spanish**
- Photography → **Japanese**

### ⭐ Advanced Features

- 📅 Month-wise install aggregation
- 📊 Pivot Table creation
- 📈 Cumulative install calculation
- 🚀 Month-over-Month growth analysis
- ✨ Highlighted periods with **more than 25% growth**

### ⏰ Time Control

Visualization is displayed only between:

**🕓 4 PM – 6 PM IST**

---

# 📊 Dashboard Visualizations

| GPA Task | Visualization |
|----------|---------------|
| GPA TASK 1 | 📊 Grouped Bar Chart |
| GPA TASK 2 | 🌍 Interactive Choropleth Map |
| GPA TASK 3 | 📈 Dual Axis Chart |
| GPA TASK 4 | 📉 Area Chart |
| GPA TASK 5 | 📊 Stacked Area Chart |

---
# 📈 Key Insights

- 📌 Free applications dominate the Google Play Store ecosystem.
- ⭐ Higher-rated applications generally receive more installs.
- 💬 Categories with higher installs tend to attract more user reviews.
- 📈 Monthly install trends help identify category growth patterns.
- 🌍 Category-wise analysis highlights high-performing market segments.
- 📊 Advanced visualizations simplify complex business trends.
- 🚀 Business-rule filtering provides more focused analytical insights.

---

# 💡 Business Recommendations

- 🚀 Prioritize development in high-performing app categories.
- ⭐ Improve application quality to increase ratings and user retention.
- 📥 Monitor install growth regularly to identify emerging trends.
- 💰 Optimize pricing strategies for paid applications.
- 💬 Encourage user reviews to improve app visibility.
- 📊 Use analytical insights to support product and marketing decisions.

---

# 🔮 Future Scope

- 🤖 Machine Learning for Rating Prediction
- 📈 Install Forecasting Model
- 💰 Revenue Prediction
- 📊 Power BI Dashboard Development
- 🌐 Real-Time API Integration
- ☁️ Cloud Deployment
- 📱 Interactive Web Dashboard
- 🧠 Recommendation System for App Categories

---

# 📁 Project Structure

```text
Google_Play_Store_Data_Analysis/
│
├── GPA_TASK_1.ipynb
├── GPA_TASK_2.ipynb
├── GPA_TASK_3.ipynb
├── GPA_TASK_4.ipynb
├── GPA_TASK_5.ipynb
│
├── Play Store Data.csv
├── User Reviews (1).csv
│
├── app.py
├── newssee.py
│
├── requirements.txt
├── README.md
```

---

# 🏆 Skills Demonstrated

- 🧹 Data Cleaning
- 🔄 Data Transformation
- 📊 Exploratory Data Analysis (EDA)
- 📈 Data Visualization
- 📉 Statistical Analysis
- 🎯 Business Rule Implementation
- 🌍 Category Translation
- ⏰ Time-Based Visualization Control
- 📋 KPI Generation
- 💡 Business Insight Generation

---

# 📌 Note

This project was developed for **learning, portfolio building, and practical data analytics practice**.

It demonstrates an end-to-end analytics workflow including:

- Dataset Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Business Rule Implementation
- KPI Development
- Advanced Data Visualization
- Time-Series Analysis
- Business Insight Generation

using **Python, Pandas, NumPy, Matplotlib, Seaborn, and Plotly**.

---

## ⭐ If you found this project useful, consider giving it a star!

### 👨‍💻 Author

**Vansh Sharma**

📧 Feel free to explore the repository and connect for feedback or collaboration.
