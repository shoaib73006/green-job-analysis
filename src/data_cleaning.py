from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

INPUT = ROOT / "data/processed/sustainability_indicators.csv"
OUTPUT = ROOT / "data/processed/sustainability_indicators_clean.csv"
REPORT = ROOT / "reports/data_quality_report.txt"

def main():
    if not INPUT.exists():
        raise SystemExit("Run data_collection.py first.")

    df = pd.read_csv(INPUT)
    initial_rows = len(df)

    df = df.drop_duplicates(
        subset=["country_code", "year"]
    )

    numeric_columns = [
        "co2_per_capita",
        "renewable_electricity_share_pct",
        "unemployment_pct",
        "labor_force_participation_pct",
        "gdp_growth_pct"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    missing = df[numeric_columns].isna().sum()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)

    df = df.sort_values(["country", "year"])
    df.to_csv(OUTPUT, index=False)

    report = f"""
DATA QUALITY REPORT
===================
Rows before cleaning: {initial_rows}
Rows after cleaning: {len(df)}
Duplicates removed: {initial_rows - len(df)}

Missing values:
{missing.to_string()}

Missing values were not replaced with zero.
"""

    REPORT.write_text(report, encoding="utf-8")

    print(report)
    print("Clean dataset saved:", OUTPUT)

if __name__ == "__main__":
    main()