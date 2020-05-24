import yfinance as yf
import pandas as pd
from companies import getCompanies

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

companies = getCompanies()
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
