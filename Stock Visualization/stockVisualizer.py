import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run():
    stockData = pd.read_csv('../Datasets/Stocks/HAL.csv',delimiter=',',usecols=['date','volume','open','close','high','low'])
    stockData = stockData.sort_values('date')
    stockData.head()

    plt.figure(figsize = (18,9))
    plt.plot(range(stockData.shape[0]),(stockData['low']+stockData['high'])/2.0)
    plt.xticks(range(0,stockData.shape[0],500),stockData['date'].loc[::500],rotation=45)
    plt.title('Halliburton Company')
    plt.xlabel('Date',fontsize=18)
    plt.ylabel('Mid Price',fontsize=18)
    plt.show()

if __name__ == "__main__":
    run()