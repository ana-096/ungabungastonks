import glob
import pandas as pd

# expects .csv as STOCK_1Y.csv
# to convert to convenient format
# for backtester
# do not run twice! or you will have many .csv.csv

path = "./*.csv"
files = glob.glob(path)

names = [x[2:].split("_")[0] for x in files]

stocks = {
    name: stock for name, stock in zip(names, [pd.read_csv(file) for file in files])
}

for name, stock in stocks.items():
    # remove $ signs
    for column in stock.columns:
        if stock[column].dtype == pd.StringDtype:
            stock[column] = stock[column].str.replace("$", "")
    # convert dates to datetime for comparisons
    stock['Date'] = pd.to_datetime(stock['Date'], dayfirst=False)
    stock.to_csv(name+".csv", index=False)