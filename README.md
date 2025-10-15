# 🩺 CDE Health Monitor – Data Discrepancy & Freshness Dashboard

## 📘 Project Overview
The **CDE Health Monitor** project tracks and visualizes **data quality and freshness** across Customer Data Elements (CDEs).  
It detects missing or outdated records, highlights discrepancies, and visualizes overall data health.

This project reflects how enterprise analytics teams (like Amazon’s CDE Science Team) maintain accurate and timely customer data for decision-making.

---

## 🎯 Objectives
- Detect missing or inconsistent data across key attributes  
- Track data freshness (days since last update)  
- Visualize missing vs valid data in dashboards  
- Automate discrepancy reporting for continuous monitoring  

---

## 🧩 Project Structure
CDE-Health-Monitor/
│
├── data/ # Input or raw data
├── processed/ # Cleaned files and reports
│ ├── discrepancy_report.ods
│ ├── discrepancy_report.xlsx
│ └── CDE_Health_Report.xlsx
│
├── src/ # Scripts and code files
│ └── validate_cde_health.py
│
├── notebooks/ # Optional: Jupyter analysis
│ └── CDE_analysis.ipynb
│
└── README.md

---

## 📊 Key Visuals

### 🔹 Missing vs Valid Records
A **Pie Chart** representing missing and valid records in the dataset.

### 🔹 Data Freshness by CDE Name
A **Column Chart** showing how recently each record was updated.

---

## 🧠 Tools Used
| Tool | Purpose |
|------|----------|
| **LibreOffice Calc / Excel** | Data cleaning, charting, and reporting |
| **Python (optional)** | Automating discrepancy validation |
| **Git & GitHub** | Version control and collaboration |
| **Power BI (future)** | Interactive dashboard development |

---

## 🧩 Workflow Summary
1. Data is extracted and validated using Python or manual entry.  
2. LibreOffice (or Excel) is used to calculate data freshness and visualize discrepancies.  
3. Final reports (`CDE_Health_Report.xlsx`) are generated and saved under `/processed/`.  
4. The results are version-controlled in GitHub for continuous monitoring.

---

## 🧠 Learnings
- Building professional Excel dashboards  
- Performing data quality validation  
- Automating data discrepancy detection  
- Structuring analytics projects for GitHub portfolios  






