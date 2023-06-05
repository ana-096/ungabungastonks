import glob
import numpy as np
import pandas as pd

START_DATE = ""

path = "./*.csv"
files = glob.glob(path)

names = [x[2:].split("_")[0] for x in files]

stonks = {
    name: stock for name, stock in zip(names, [pd.read_csv(file) for file in files])
}

for stock in stonks.values():
    pass