# Sales Analysis Project

## Project Overview

This project analyzes sales data using Python. 
The goal is to clean data, perform analysis, create visualizations, and generate reports.

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL
- VS Code

---

## Project Structure

```
Sales-Analysis-Project
│
├── data
│   └── sales.csv
│
├── reports
│   ├── category_summary.csv
│   └── category_summary.xlsx
│
├── src
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── export_report.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Project Workflow

1. Import sales data
2. Clean the dataset
3. Perform exploratory data analysis
4. Create visualizations
5. Generate summary reports

---

## Analysis Performed

### Sales Analysis

- Total sales calculation
- Total profit calculation
- Average sales calculation
- Highest and lowest sales

### Category Analysis

- Sales by category
- Profit by category
- Quantity sold by category

### Region Analysis

- Profit by region
- Sales distribution

---

## Visualizations Created

The project includes:

- Sales by Category bar chart
- Sales by Region pie chart
- Profit distribution histogram

---

## Reports Generated

The project exports:

- CSV summary report
- Excel summary report

Example:

```
category_summary.csv
category_summary.xlsx
```

---

## How to Run the Project

### 1. Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

### 2. Install Requirements

```
pip install -r requirements.txt
```

### 3. Run Analysis

```
python src/analysis.py
```

### 4. Generate Reports

```
python src/export_report.py
```

### 5. Run Visualization

```
python src/visualization.py
```

---

## Author

Your Name
## Dashboard Preview

![Sales Dashboard](screenshots/sales.png)