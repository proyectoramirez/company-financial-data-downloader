import yfinance as yf
import pandas as pd

COLUMNS = [
    "symbol",
    "longName",
    "sector",
    "previousClose",
    "trailingAnnualDividendYield",
    "totalAssets",
    "marketCap",
    "forwardPE",
    "bookValue",
    "priceToBook",
    "threeYearAverageReturn",
    "earningsQuarterlyGrowth",
    "fiveYearAverageReturn"
]

data = pd.read_excel("S&P Analysis.xlsx")
companies = data["Symbol"]

output = pd.DataFrame(columns=COLUMNS)

for i, company in enumerate(companies):
    try:
        stock = yf.Ticker(company).info

        output.loc[i] = [stock[column] for column in COLUMNS]
        print(company, "Done", sep="\t")
    except:
        output.loc[i] = [company] + ["" for i in range(len(COLUMNS) - 1)]
        print(company, "FAIL", sep="\t")

output.to_excel("output.xlsx", index=False)
