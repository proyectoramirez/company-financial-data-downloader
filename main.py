import yfinance as yf
import pandas as pd
from companies import getCompanies

columns = [
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
output = pd.DataFrame(columns=columns)

for i, company in enumerate(companies):
    try:
        stock = yf.Ticker(company).info

        output.loc[i] = [stock[column] for column in columns]
        print(company, "Done", sep="\t")
    except:
        output.loc[i] = [company] + ["" for i in range(len(columns) - 1)]
        print(company, "FAIL", sep="\t")

output.to_excel("output.xlsx", index=False)
