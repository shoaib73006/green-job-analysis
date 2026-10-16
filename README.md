# Green Job Analysis

## Green Jobs & Sustainability Data Analysis

An end-to-end data analysis project that explores sustainability and labour-market indicators across selected Asian countries using publicly available World Bank data.

## Project Objectives

- Collect sustainability indicators from a public data source.
- Clean and preprocess the collected datasets using Python.
- Analyse trends in CO₂ emissions, renewable electricity, unemployment, labour-force participation, and GDP growth.
- Generate visualisations and summary reports to support data-driven insights.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Requests
- World Bank Indicators API
- Git and GitHub

## Indicators Analysed

- CO₂ emissions per capita
- Renewable electricity output
- Unemployment rate
- Labour-force participation rate
- GDP growth

## Project Structure

```text
green job project/
├── src/
│   ├── data.collection.py
│   ├── data_cleaning.py
│   └── analysis.py
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   └── charts/
├── reports/
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/shoaib73006/greenjobanalysis.git
   cd greenjobanalysis
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the Project

Run the scripts in this order from the project root:

```bash
python src/data.collection.py
python src/data_cleaning.py
python src/analysis.py
```

The data collection step requires an internet connection to access the World Bank API.

## Expected Outputs

- Downloaded indicator datasets
- Cleaned CSV files
- Data quality and summary statistics
- Sustainability trend charts
- Country-level data coverage information

## Important Note

This project analyses general sustainability and labour-market indicators. These indicators do not directly measure the number of green jobs, so the findings should not be interpreted as direct green-employment estimates.

## Data Source

World Bank Indicators API: https://api.worldbank.org/

## Author

Shoaib Ahmed

GitHub: https://github.com/shoaib73006
