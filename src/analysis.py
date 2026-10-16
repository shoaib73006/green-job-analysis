from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

INPUT = ROOT / "data/processed/sustainability_indicators_clean.csv"
CHARTS = ROOT / "outputs/charts"
REPORTS = ROOT / "reports"

METRICS = [
    "co2_per_capita",
    "renewable_electricity_share_pct",
    "unemployment_pct",
    "labor_force_participation_pct",
    "gdp_growth_pct"
]

def main():
    if not INPUT.exists():
        raise SystemExit("Run data cleaning first.")

    CHARTS.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT)

    for metric in METRICS:
        subset = df[["year", "country", metric]].dropna()

        if subset.empty:
            print("No data available:", metric)
            continue

        plt.figure(figsize=(10, 6))

        for country, group in subset.groupby("country"):
            group = group.sort_values("year")

            plt.plot(
                group["year"],
                group[metric],
                marker="o",
                label=country
            )

        plt.title(metric.replace("_", " ").title())
        plt.xlabel("Year")
        plt.ylabel(metric.replace("_", " ").title())
        plt.grid(alpha=0.3)
        plt.legend(fontsize=8)
        plt.tight_layout()

        plt.savefig(CHARTS / f"{metric}_trend.png", dpi=150)
        plt.close()

    df[METRICS].describe().T.to_csv(
        REPORTS / "descriptive_statistics.csv"
    )

    df.groupby("country")[METRICS].count().to_csv(
        REPORTS / "data_coverage_by_country.csv"
    )

    print("Analysis completed!")
    print("Charts saved to:", CHARTS)
    print("Reports saved to:", REPORTS)

if __name__ == "__main__":
    main()