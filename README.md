# 🚢 Task 2 - Titanic Dataset Exploratory Data Analysis (EDA)

## 📌 Objective

The objective of this project is to perform Exploratory Data Analysis (EDA) on the Titanic Dataset to identify patterns, trends, and factors that influenced passenger survival.

---

## 📂 Dataset

Dataset Used: Titanic Dataset

The dataset contains information about passengers such as:

- Passenger ID
- Survival Status
- Passenger Class
- Name
- Gender
- Age
- Fare
- Cabin
- Embarked Port
- Family Information

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📁 Project Structure

Task-2-EDA-Titanic/
│
├── Titanic-Dataset.csv
├── EDA_Titanic.ipynb
├── Cleaned_Titanic_Data.csv
├── outputs/
│   ├── missing_values_heatmap.png
│   ├── survival_count.png
│   ├── gender_survival.png
│   ├── class_survival.png
│   ├── age_distribution.png
│   ├── fare_distribution.png
│   ├── correlation_matrix.png
│   └── fare_outliers.png
│
└── README.md

---

## 🔍 Exploratory Data Analysis Performed

### 1. Data Exploration

- Displayed first five rows
- Checked dataset dimensions
- Examined column names
- Verified data types
- Generated dataset information
- Generated descriptive statistics

---

### 2. Missing Value Analysis

Missing Values Found:

| Column | Missing Values |
|----------|----------|
| Age | 177 |
| Cabin | 687 |
| Embarked | 2 |

Visualized missing values using a heatmap.

---

### 3. Survival Analysis

Analyzed:

- Overall survival count
- Survival based on gender
- Survival based on passenger class

---

### 4. Distribution Analysis

Visualized:

- Age Distribution
- Fare Distribution

using histograms and density plots.

---

### 5. Correlation Analysis

Generated a correlation matrix to understand relationships between numerical features.

---

### 6. Outlier Detection

Detected outliers in Fare using a boxplot.

---

### 7. Data Cleaning

Performed the following preprocessing steps:

- Filled missing Age values using mean.
- Filled missing Embarked values using mode.
- Removed Cabin column due to excessive missing values.
- Checked for duplicate records.

---

## 📊 Key Insights

### Gender Survival

- Female passengers had significantly higher survival rates than male passengers.

### Passenger Class

- First-class passengers had a greater chance of survival compared to second and third-class passengers.

### Age Distribution

- Most passengers were between 20 and 40 years old.

### Fare Distribution

- Fare data was highly skewed with several high-value outliers.

---

## 📈 Visualizations Generated

- Missing Values Heatmap
- Survival Count Plot
- Survival by Gender
- Survival by Passenger Class
- Age Distribution Histogram
- Fare Distribution Histogram
- Correlation Heatmap
- Fare Outlier Boxplot

---

## ▶️ How to Run

### Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Run the Notebook

```bash
jupyter notebook EDA_Titanic.ipynb
```

or run the Python script:

```bash
python EDA_Titanic.py
```

---

## 📁 Output

The cleaned dataset is exported as:

```text
Cleaned_Titanic_Data.csv
```

---

## 🎯 Learning Outcomes

- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis
- Data Visualization
- Correlation Analysis
- Outlier Detection
- Feature Understanding

---

## 👩‍💻 Author

**Sadula Sarika**

Data Analytics Intern – CodeAlpha
