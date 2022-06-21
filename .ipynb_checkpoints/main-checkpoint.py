#!/usr/bin/env python3
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

# seria interessante ter uma selecao das acoes pra escolher, com bastante variedade
# e arrumar algum jeito de fazer as regras de quantias máximas ou mínimas para os tipos
# diferentes das acoes, por exemplo, 30% de energia, 30% de bancos e 40% tecnologias...

stockAdjClose = './stock_adj_close_brl.csv'
marketAdjClose = './market_adj_close_brl.csv'
stockRows = 1243
stockCols = 62


style.use('ggplot')

stocks = ['TSLA', 'AAPL', 'KO']
start_date = dt.datetime(2017,1,1)
end_date = dt.datetime(2022,1,1)

number_of_portfolios = 5

stock_returns = pd.DataFrame()
for stock in stocks:
  data = web.DataReader(stock, 'yahoo', start_date, end_date)
  data = pd.DataFrame(data)
  data[stock] = data['Adj Close'].pct_change()

  if stock_returns.empty:
    stock_returns = data[[stock]]
  else :
    stock_returns = stock_returns.join(data[[stock]], how='outer')

print(stock_returns.head())
# test = web.DataReader(["ITUB4.SA", "FB"], 'yahoo', start_date, end_date)
