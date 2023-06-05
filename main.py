import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TRAINING_START_DATE = "2022"
TRAINING_END_DATE = "2023"

path = "./*.csv"
files = glob.glob(path)

names = [x[2:].split("_")[0] for x in files]

stonks = {
    name: stock for name, stock in zip(names, [pd.read_csv(file) for file in files])
}

training_stonks = {}

for name, stonk in stonks.items():
    # convert dates to datetime for comparisons
    stonk['Date'] = pd.to_datetime(stonk['Date'], dayfirst=False)

    # select only date and close
    training_stonks[name] = stonk[stonk['Date'].isin(pd.date_range(TRAINING_START_DATE, TRAINING_END_DATE))][['Date','Close/Last']]

    # convert close to int in cents
    training_stonks[name]['Close/Last'] = training_stonks[name]['Close/Last'].str.replace("$", "")
    training_stonks[name]['Close/Last'] = training_stonks[name]['Close/Last'].str.replace(".", "")
    training_stonks[name]['Close/Last'] = training_stonks[name]['Close/Last'].map(lambda x: int(x))

for name, training_stonk in training_stonks.items():
    training_stonk.plot(title = name,x = 'Date', y = 'Close/Last')

plt.show()