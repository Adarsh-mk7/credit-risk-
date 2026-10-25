# Credit Risk Assessment and Decision Support System with Comprehensive Visualization Using Python and Power BI

An end-to-end Credit Risk Assessment and Decision Support System combining machine learning predictive analytics in **Python** with interactive business intelligence dashboards in **Power BI**.

---

## 📌 Project Architecture

```
├── CODE/
│   ├── code.py                          # ML pipeline (Data Prep, Random Forest, Evaluation, Export)
│   ├── Credit card Fraud Analysis.pbix  # Interactive Power BI Dashboard
│   ├── data.csv                         # Credit dataset (Tracked with Git LFS)
│   └── README.md                        # Dashboard documentation
├── DOCS/
│   ├── abstract.docx                    # Project abstract
│   ├── base paper.pdf                   # Reference research paper
│   ├── Credit card Fraud Analysis.pdf   # Analysis & technical report
│   └── Credit Risk Assessment ...docx   # Comprehensive documentation
├── output/
│   ├── Credit card Fraud Analysis.png   # Dashboard overview
│   └── Screenshot 2025-07-15 175851.png # Detailed dashboard view
├── .gitattributes                       # Git LFS tracking configuration
├── .gitignore                           # Python and IDE ignore rules
└── README.md                            # Project repository documentation
```

---

## 🚀 Key Features

- **Machine Learning Predictive Modeling**:
  - Preprocesses credit and borrower attributes (handling missing values, label encoding categorical features).
  - Computes correlation matrix and feature relationships.
  - Trains a **Random Forest Classifier** to assess credit risk flags / default indicators.
  - Evaluates models with Accuracy Score, Confusion Matrix, and Precision/Recall Classification Reports.
  - Exports test risk predictions for seamless ingestion into Power BI.

- **Power BI Decision Support Dashboard**:
  - Interactive drill-downs by customer demographics (Age, Education, Marital Status, Sex).
  - Analysis of Credit Limit Balance vs. Default Rates.
  - Dynamic risk filtering and KPI cards for actionable lending decisions.

- **Comprehensive Documentation**:
  - Includes academic base paper, project abstract, and complete system documentation.

---

## 📊 Dashboard Visualizations

![Power BI Dashboard](output/Credit%20card%20Fraud%20Analysis.png)

---

## 🛠️ Tech Stack & Requirements

- **Python 3.10+**:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
- **Business Intelligence**:
  - Microsoft Power BI Desktop
  - DAX (Data Analysis Expressions) & Power Query
- **Version Control**:
  - Git & [Git LFS](https://git-lfs.github.com/) (for dataset tracking)

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
# Ensure Git LFS is installed
git lfs install

# Clone the repository
git clone https://github.com/Adarsh-mk7/credit-risk-.git
cd credit-risk-
```

### 2. Run Python ML Pipeline
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
cd CODE
python code.py
```

### 3. Open Power BI Dashboard
1. Open [Power BI Desktop](https://powerbi.microsoft.com/).
2. Open `CODE/Credit card Fraud Analysis.pbix`.
3. Refresh data source connection to `data.csv` or exported `credit_risk_results.csv` if prompted.

---

## 👥 Authors & Acknowledgments

- **Adarsh** ([GitHub: @Adarsh-mk7](https://github.com/Adarsh-mk7))
- Reference documentation and research papers available in the `DOCS/` folder.
