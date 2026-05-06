# E-commerce Data Pipeline & Analytics Dashboard

## 📌 Overview

This project demonstrates the end-to-end development of a data pipeline for e-commerce transactional data, from raw ingestion to business-ready analytics and visualization.

The pipeline focuses on:

- Data quality and validation
- Clean, modular architecture
- Business-oriented metrics
- Integration with Power BI for reporting

---

## 🧱 Project Structure

```
project/
│
├── data/
│   ├── raw/  # Raw input CSVs
|   |    ├── orders.csv
|   |    ├── customers.csv
|   |    └── products.csv
│   └── processed/     # Cleaned and aggregated outputs
│
├── src/
|  ├── load.py               # Data ingestion
|  ├── clean.py              # Data cleaning & validation
|  ├── transform.py          # Data modeling (fact table)
|  ├── aggregate.py          # KPI computation
|  └── main.py               # Pipeline orchestration
│
└── README.md
```

---

## 🔄 Pipeline Flow

Raw Data → Clean → Validate → Transform → Aggregate → Output

### 1. Load

- Reads raw CSV files
- Handles file paths and ingestion

### 2. Clean

- Schema validation
- Type conversion
- Value validation (e.g., quantity > 0)
- Deduplication
- Relationship validation (foreign keys)

### 3. Transform

- Joins orders, customers, and products
- Creates a denormalized fact table
- Adds derived fields:
  - revenue
  - year_month

### 4. Aggregate

Generates business metrics:

- Monthly Revenue
- Revenue by Category
- Customer Summary

---

## 📊 Outputs

Saved in `data/processed/`:

- monthly_revenue.csv
- category_revenue.csv
- customer_summary.csv
- merged_data.csv (fact table)

---

## 📈 Power BI Dashboard

The processed data is used to build an interactive dashboard including:

### KPIs

- Total Revenue
- Total Orders
- Average Order Value (AOV)
- Total Customers

### Visuals

- Revenue trend over time
- AOV trend
- Revenue by category
- Revenue by country
- Top customers

### Filters

- Month
- Quarter
- Country
- Category

### Screenshot

![Screenshot of Power BI dashboard](/dashboard/dashboard_screenshot.png "Power BI Dashboard Screenshot")

---

## 🧠 Key Concepts Demonstrated

- Data validation pipelines
- Schema enforcement
- Handling missing and invalid data
- Avoiding aggregation bias (correct AOV calculation)
- Data modeling for BI tools
- Separation of concerns (modular design)

---

## 🚀 How to Run

```bash
python main.py
```

Ensure your folder structure matches:

data/raw/
data/processed/

---

## 📌 Key Insight

Revenue growth is primarily driven by a few key categories and markets, with noticeable seasonality in later months. The pipeline ensures that these insights are derived from clean, reliable data.

---

## 🧑‍💻 Author

### Ignacio Spreafico

Senior Data Analyst | Product Analytics | Experimentation & Decision

[Linkedin]("https://www.linkedin.com/in/ignacio-spreafico")
[Github]("https://www.github.com/nachospreafico")
[Website]("https://ignaciospreafico.vercel.app")

---

## ⭐ Notes

This project is designed to reflect real-world data workflows:

- Clean architecture
- Reproducibility
- Business relevance
