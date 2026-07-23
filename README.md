 # 📱 Google Play Store Analytics Dashboard

## 1. Project Title

Google Play Store Analytics Dashboard Using Python, Plotly & Streamlit

---

## 2. Project Overview

This project is an interactive **Google Play Store Analytics Dashboard** developed using **Python, Pandas, NumPy, Plotly, and Streamlit**. It analyzes Google Play Store applications to uncover insights into app ratings, installs, reviews, pricing, categories, and user engagement.

The project also implements **advanced business rules**, including dynamic filtering, multilingual category labels, conditional formatting, and **time-based chart rendering**, making it a realistic Business Intelligence (BI) dashboard.

---

## 3. Objectives

- Analyze Google Play Store app performance.
- Discover trends in ratings, installs, reviews, and pricing.
- Build interactive dashboards using Plotly & Streamlit.
- Implement advanced filtering and business rules.
- Generate meaningful business insights for developers and businesses.

---

## 4. Tools & Technologies

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Matplotlib
- Jupyter Notebook

---

## 5. Dataset

- **Dataset:** Google Play Store Dataset
- **Source:** Kaggle
- **Format:** CSV

---

## 6. Data Preprocessing

- Removed duplicate records
- Handled missing values
- Converted data types
- Cleaned Reviews, Installs, Price, and Size columns
- Converted **Last Updated** to datetime format
- Standardized categorical values
- Applied feature engineering
- Implemented advanced filtering conditions

---

## 7. Key Performance Indicators (KPIs)

- Total Applications
- Average Rating
- Total Installs
- Total Reviews
- Average App Size
- Average App Price
- Free vs Paid Apps
- Highest Installed Category
- Highest Rated Category
- Category-wise Reviews

---

## 8. Exploratory Data Analysis (EDA)

- App Category Analysis
- Rating Distribution
- Reviews Analysis
- Installs Analysis
- Free vs Paid Analysis
- Size Analysis
- Price Analysis
- Correlation Analysis
- Time-based Analysis

---

## 9. Dashboard Visualizations

- Grouped Bar Chart
- Interactive Choropleth Map
- Dual-Axis Chart
- Area Chart
- Bubble Chart
- Stacked Area Chart

---

# 🚀 Tasks Implemented

## ✅ Task 1 – Grouped Bar Chart

**Objective**
- Compared **Average Rating** and **Total Reviews** for the **Top 10 Categories** based on installs.

**Conditions Applied**
- Average Rating ≥ 4.0
- App Size ≥ 10 MB
- Last Updated Month = January
- Dashboard visible only between **3:00 PM – 5:00 PM IST**

---

## ✅ Task 2 – Interactive Choropleth Map

**Objective**
- Visualized installs using an interactive Plotly Choropleth Map.

**Conditions Applied**
- Top 5 Categories
- Installs > 1 Million
- Excluded categories starting with **A, C, G, S**
- Dashboard visible only between **6:00 PM – 8:00 PM IST**

---

## ✅ Task 3 – Dual Axis Chart

**Objective**
- Compared **Average Installs** and **Revenue** for **Free vs Paid Apps**.

**Conditions Applied**
- Top 3 Categories
- Installs > 10,000
- Revenue > $10,000
- Android Version > 4.0
- App Size > 15 MB
- Content Rating = Everyone
- App Name ≤ 30 Characters
- Dashboard visible only between **1:00 PM – 2:00 PM IST**

---

## ✅ Task 4 – Area Chart

**Objective**
- Visualized monthly install growth segmented by app category.

**Conditions Applied**
- Growth > 20% Month-over-Month
- Reviews > 500
- App Name should not start with **X, Y, Z**
- App Name should not contain **S**
- Categories should start with **B, C, or E**
- Category Translation:
  - Beauty → Hindi
  - Business → Tamil
  - Dating → German
- Dashboard visible only between **6:00 PM – 9:00 PM IST**

---

## ✅ Task 5 – Bubble Chart

**Objective**
- Compared **App Size**, **Average Rating**, and **Installs**.

**Conditions Applied**
- Rating > 3.5
- Reviews > 500
- Installs > 50,000
- Sentiment Subjectivity > 0.5
- Selected Categories only
- App Name should not contain **S**
- Highlighted **Game** category in Pink
- Category Translation:
  - Beauty → Hindi
  - Business → Tamil
  - Dating → German
- Dashboard visible only between **5:00 PM – 7:00 PM IST**

---

## ✅ Task 6 – Stacked Area Chart

**Objective**
- Visualized cumulative installs over time.

**Conditions Applied**
- Average Rating ≥ 4.2
- Reviews > 1,000
- App Size between **20 MB – 80 MB**
- App Name should not contain numbers
- Categories should start with **T** or **P**
- Category Translation:
  - Travel & Local → French
  - Productivity → Spanish
  - Photography → Japanese
- Increased color intensity when installs increased by **more than 25% Month-over-Month**
- Dashboard visible only between **4:00 PM – 6:00 PM IST**

---

## 11. Key Insights

- Free applications dominate the Google Play Store.
- Game and Family categories have the highest installs.
- Higher-rated apps generally receive more downloads.
- Reviews positively influence app popularity.
- Interactive dashboards provide better decision-making support.
- Advanced filtering improves business-focused analysis.
- Time-based dashboard rendering enhances user experience.

---

## 12. Business Recommendations

- Focus development on high-performing categories.
- Improve ratings through user feedback.
- Optimize pricing strategies for paid apps.
- Monitor install growth regularly.
- Use dashboard insights to identify market opportunities.

---

## 13. Future Scope

- Machine Learning for Rating Prediction
- Install Prediction Model
- Revenue Forecasting
- Power BI Dashboard
- Real-Time Data Integration
- Cloud Deployment

---

## 14. Project Structure

```text
Google_Play_Store_Analysis/
│
├── Google_Play_Store_Analysis.ipynb
├── app.py
├── googleplaystore.csv
├── README.md
├── requirements.txt
└── Images/
```
 

## 📌 Note

This project was developed for **learning and practice purposes**. It demonstrates **data preprocessing, exploratory data analysis (EDA), interactive dashboard development, advanced business rule implementation, time-based visualization control, multilingual category translation, and business insight generation** using Python, Plotly, and Streamlit.

Author Vansh Sharma
