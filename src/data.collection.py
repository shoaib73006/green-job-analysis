
import requests
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COUNTRIES = {
    "IND": "India",
    "BGD": "Bangladesh",
    "NPL": "Nepal",
    "LKA": "Sri Lanka",
    "PAK": "Pakistan",
    "IDN": "Indonesia",
    "VNM": "Vietnam",
    "THA": "Thailand"
}

INDICATORS = {
    "EN.ATM.CO2E.PC": "co2_per_capita",
    "EG.ELC.RNEW.ZS": "renewable_electricity_share_pct",
    "SL.UEM.TOTL.ZS": "unemployment_pct",
    "SL.TLF.CACT.ZS": "labor_force_participation_pct",
    "NY.GDP.MKTP.KD.ZG": "gdp_growth_pct"
}

def main():
    records = []

    for code, country in COUNTRIES.items():
        for indicator, name in INDICATORS.items():
            url = (
                f"https://api.worldbank.org/v2/country/"
                f"{code}/indicator/{indicator}"
            )

            try:
                response = requests.get(
                    url,
                    params={
                        "date": "2010:2023",
                        "format": "json",
                        "per_page": 200
                    },
                    timeout=30
                )
                response.raise_for_status()
                payload = response.json()

                if not isinstance(payload, list) or len(payload) < 2:
                    continue

                for item in payload[1] or []:
                    records.append({
                        "country_code": code,
                        "country": country,
                        "year": int(item["date"]),
                        "indicator_name": name,
                        "value": item.get("value")
                    })

                print(f"Downloaded: {country} - {name}")

            except (requests.RequestException, ValueError, KeyError) as error:
                print(f"Error: {country}, {name}: {error}")

    if not records:
        raise SystemExit("No data downloaded. Check your internet.")

    df = pd.DataFrame(records)

    raw_dir = ROOT / "data" / "raw"
    processed_dir = ROOT / "data" / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    df.to_csv(raw_dir / "world_bank_indicators_long.csv", index=False)

    wide = df.pivot_table(
        index=["country_code", "country", "year"],
        columns="indicator_name",
        values="value",
        aggfunc="first"
    ).reset_index()

    wide.columns.name = None

    for column in INDICATORS.values():
        if column not in wide.columns:
            wide[column] = pd.NA

    wide.to_csv(
        processed_dir / "sustainability_indicators.csv",
        index=False
    )

    print("Data collection completed!")
    print("Dataset shape:", wide.shape)

if __name__ == "__main__":
    main()
