# 📊 Fraud Risk Dashboard

## 📌 Project Overview

This project presents an end-to-end data analytics workflow for detecting high-risk merchants using transaction data.

It combines Python for data processing and Power BI for interactive visualization.

---

## 🎯 Objectives

* Identify high-risk merchants
* Analyze fraud patterns
* Monitor transaction behavior
* Provide actionable insights

---

## 🧠 Methodology

### 🔹 Python (Data Processing)

* Loaded transaction dataset using Pandas
* Created features:

  * Fraud Rate
  * Small Transaction Rate
* Calculated a combined **Risk Score**
* Identified Top 5 risky merchants
* Exported results for further use

---

### 🔹 Power BI (Visualization)

* Built interactive dashboard
* Created KPI cards and alerts
* Implemented slicer for merchant selection
* Designed Top 5 risky merchants chart
* Added risk-based color logic

---

## 📈 Key Metrics

* **Fraud Rate**
* **Small Transaction Rate**
* **Advanced Risk Score**
* **Total Transaction Amount**

---

## 🚨 Features

* Global risk alert
* Selected merchant alert
* Top 5 risky merchants
* Interactive filtering
* Comparative charts

---

## 🔗 End-to-End Workflow

1. Data loading and processing in Python
2. Feature engineering and risk calculation
3. Exporting processed data
4. Visualization in Power BI

---

## 🛠 Tools & Technologies

* Python (Pandas)
* Power BI
* DAX

---

## 📸 Dashboard Preview

### 🔹 Overview

![Dashboard](dashboard_overview.png)

### 🔹 Alerts

![Alerts](alerts_section.png)

### 🔹 Top 5 Analysis

![Top5](top5_analysis.png)

---

## 📂 Project Structure

Fraud-Risk-Dashboard/
├── data/
│   └── transactions.csv
├── notebooks/
│   └── analysis.py
├── dashboard/
│   └── Fraud_Risk_Dashboard.pbix
├── dashboard_overview.png
├── alerts_section.png
├── top5_analysis.png
└── README.md

---

## 🚀 How to Run

1. Clone the repository
2. Run Python script:
   python3 notebooks/analysis.py
3. Open Power BI file

---

## 👩‍💻 Author

Data Analytics Portfolio Project

---

## 🔄 Future Improvements

* Add time-based analysis
* Implement anomaly detection
* Extend Python analysis
