### 📱 Google Play Store Data Analysis using Python
<p align="center">

### 🚀 End-to-End Data Analytics Project using Python, Plotly & Streamlit

</p>

---

# 👨‍💻 Author

**Vansh Sharma**

---

# 📌 Project Overview

This project is an interactive **Google Play Store Analytics Dashboard** developed using **Python, Pandas, Plotly, and Streamlit**.

The project focuses on analyzing Android applications to extract meaningful insights related to:

- 📱 App Performance
- ⭐ Ratings
- 📥 Installs
- 💬 Reviews
- 💰 Pricing
- 📊 Category Trends
- 📈 Growth Analysis

The dashboard implements real-world business rules such as:

- Dynamic filtering
- Advanced data preprocessing
- Category translation
- Conditional highlighting
- Time-based visualization control

---

# 🎯 Project Objectives

- Analyze Google Play Store application data.
- Identify high-performing app categories.
- Understand relationships between ratings, reviews, and installs.
- Create interactive business dashboards.
- Generate data-driven insights for decision making.

---

# 🛠️ Technologies & Libraries Used

## Programming Language
- 🐍 Python

## Data Analysis
- 🐼 Pandas
- 🔢 NumPy

## Data Visualization
- 📊 Plotly
- 📈 Matplotlib
- 🎨 Seaborn

## Dashboard Development
- 🚀 Streamlit

## Time & Date Handling
- ⏰ Datetime
- 🌎 Pytz (IST Timezone Handling)

## Development Environment
- 📓 Jupyter Notebook
- 💻 VS Code

---

# 📂 Dataset Information

**Dataset Name:** Google Play Store Dataset

**Source:** Kaggle

**Format:** CSV

The dataset contains application details:

- App Name
- Category
- Rating
- Reviews
- Installs
- Size
- Type
- Price
- Content Rating
- Genres
- Last Updated
- Current Version
- Android Version

---

# 🧹 Data Preprocessing

Performed following cleaning steps:

✅ Removed corrupted records  
✅ Removed duplicate applications  
✅ Handled missing values  
✅ Converted Installs into numerical format  
✅ Converted Reviews into integer format  
✅ Converted Last Updated into datetime format  
✅ Converted App Size into MB  
✅ Standardized categorical values  
✅ Applied feature engineering  

---

# 🚀 Tasks Implemented

---

# ✅ GPA TASK 1 - Grouped Bar Chart

### 🎯 Objective

Compared category-wise:

- Average Rating
- Total Reviews

### 🔍 Conditions Applied

- Rating ≥ 4.0
- App Size ≥ 10 MB
- Last Updated Month = January
- Visualization available between **3 PM - 5 PM IST**

### 📊 Visualization

Grouped Bar Chart

---

# ✅ GPA TASK 2 - Interactive Choropleth Map

### 🎯 Objective

Visualized app installs geographically using an interactive map.

### 🔍 Conditions Applied

- Top 5 Categories
- Installs > 1 Million
- Excluded categories starting with:
  - A
  - C
  - G
  - S

- Dashboard visible between **6 PM - 8 PM IST**

### 📊 Visualization

Interactive Plotly Choropleth Map

---

# ✅ GPA TASK 3 - Dual Axis Chart

### 🎯 Objective

Compared:

- Average Installs
- Revenue

between Free and Paid applications.

### 🔍 Conditions Applied

- Installs > 10,000
- Revenue > $10,000
- Android Version > 4.0
- App Size > 15 MB
- Content Rating = Everyone
- App Name Length ≤ 30 Characters

### 📊 Visualization

Dual Axis Chart

---

# ✅ GPA TASK 4 - Area Chart

### 🎯 Objective

Analyzed monthly install growth trends by category.

### 🔍 Conditions Applied

- Growth > 20% Month-over-Month
- Reviews > 500
- App names not starting with X, Y, Z
- App name should not contain "S"
- Categories starting with:
  - B
  - C
  - E

### 🌎 Category Translation

- Beauty → Hindi
- Business → Tamil
- Dating → German

### 📊 Visualization

Area Chart

---

# ✅ GPA TASK 5 - Stacked Area Chart

### 🎯 Objective

Visualized cumulative installs over time for different app categories.

### 🔍 Conditions Applied

- Rating ≥ 4.2
- Reviews > 1,000
- App Size between 20 MB - 80 MB
- App names without numerical characters
- Categories starting with:
  - T
  - P

### 🌎 Category Translation

- Travel & Local → French
- Productivity → Spanish
- Photography → Japanese

### ⭐ Advanced Features

✅ Month-wise install aggregation  
✅ Pivot table analysis  
✅ Cumulative install calculation  
✅ Month-over-Month growth detection  
✅ Highlighted periods with growth >25%  

### ⏰ Time Control

Visualization is displayed only between:

**4 PM - 6 PM IST**

---

# 📊 Dashboard Visualizations

| Task | Visualization |
|---|---|
| GPA TASK 1 | Grouped Bar Chart |
| GPA TASK 2 | Choropleth Map |
| GPA TASK 3 | Dual Axis Chart |
| GPA TASK 4 | Area Chart |
| GPA TASK 5 | Stacked Area Chart |

---

# 📈 Key Insights

📌 Free applications dominate the Play Store ecosystem.

📌 Categories with higher installs generally receive more reviews.

📌 Ratings and user engagement have a strong relationship.

📌 Category-wise analysis helps identify market opportunities.

📌 Time-based dashboard controls improve user experience.

📌 Data visualization makes complex application trends easier to understand.

---

# 💡 Business Recommendations

🚀 Focus development on high-performing categories.

⭐ Improve ratings through better user experience.

📥 Monitor install growth trends regularly.

💰 Optimize pricing strategies for paid applications.

📊 Use analytics dashboards for better decision making.

---

# 🔮 Future Scope

- 🤖 Machine Learning based Rating Prediction
- 📈 Install Forecasting Model
- 💰 Revenue Prediction
- ☁️ Cloud Deployment
- 🔄 Real-Time API Data Integration
- 📊 Power BI Dashboard Development

---

# 📁 Project Structure

```
Google_Play_Store_Analysis/

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
│
└── Images/
```

---

# 📌 Note

This project was developed for **learning and practice purposes**.

It demonstrates practical skills in:

- Data Cleaning
- Data Analysis
- Exploratory Data Analysis (EDA)
- Data Visualization
- Dashboard Development
- Business Rule Implementation
- Time-Series Analysis
- Insight Generation

using Python-based analytics tools.

---

⭐ If you found this project useful, feel free to explore and connect!
