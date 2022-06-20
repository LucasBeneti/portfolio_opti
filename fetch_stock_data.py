#!/usr/bin/env python3
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

# 1. pegar dados de várias stocks brasileiras
# 2. salvar esses dados em um .csv pra conseguir ler depois sem problemas

# seria interessante ter uma selecao das acoes pra escolher, com bastante variedade
# e arrumar algum jeito de fazer as regras de quantias máximas ou mínimas para os tipos
# diferentes das acoes, por exemplo, 30% de energia, 30% de bancos e 40% tecnologias...

tickers = [
    'ABEV3.SA',
'ASAI3.SA',
'AZUL4.SA',
# 'BTOW3',
'B3SA3.SA',
'BBSE3.SA',
# 'VRML3.SA',
'BBDC4.SA',
'BBDC3.SA',
'BRAP4.SA',
'BBAS3.SA',
'BRKM5.SA',
'BRFS3.SA',
'CRFB3.SA',
'CCRO3.SA',
# 'CMIG4.SA',
# 'HGTX3.SA',
'COGN3.SA',
'CPLE6.SA',
'CSAN3.SA',
'CPFE3.SA',
'CVCB3.SA',
'CYRE3.SA',
'ECOR3.SA',
'ELET3.SA',
'ELET6.SA',
'EMBR3.SA',
'ENBR3.SA',
'ENGI11.SA',
'ENEV3.SA',
# 'ENGIE3.SA',
'EQTL3.SA',
'EZTC3.SA',
'FLRY3.SA',
'GGBR4.SA',
'GOAU4.SA',
'GOLL4.SA',
'NTCO3.SA',
'HAPV3.SA',
'HYPE3.SA',
# 'IGTA3.SA',
# 'GNDI3.SA',
'IRBR3.SA',
'ITSA4.SA',
'ITUB4.SA',
'JBSS3.SA',
'JHSF3.SA',
'KLBN11.SA',
'RENT3.SA',
'LCAM3.SA',
# 'LAME4.SA',
'LREN3.SA',
'MGLU3.SA',
'MRFG3.SA',
'BEEF3.SA',
'MRVE3.SA',
'MULT3.SA',
'PCAR3.SA',
'PETR3.SA',
'PETR4.SA',
# 'BRDT3.SA', verdade
'PRIO3.SA',
'QUAL3.SA',
'RADL3.SA',
'RAIL3.SA',
'SBSP3.SA',
# 'VIVT4.SA', verdade
# 'TIMP3.SA', verdade
'TOTS3.SA',
'UGPA3.SA',
'USIM5.SA',
'VALE3.SA',
# 'VVAR3.SA', verdade
'WEGE3.SA',
'YDUQ3.SA',
]

# style.use('ggplot')

# stocks = ['TSLA', 'AAPL', 'KO']
start_date = dt.datetime(2017,1,1)
end_date = dt.datetime(2022,1,1)

number_of_portfolios = 5

stock_returns = pd.DataFrame()
for stock in tickers:
  data = web.DataReader(stock, 'yahoo', start_date, end_date)
  data = pd.DataFrame(data)
  data[stock] = data['Adj Close']

  if stock_returns.empty:
    stock_returns = data[[stock]]
  else :
    stock_returns = stock_returns.join(data[[stock]], how='outer')

print(stock_returns.head())
stock_returns.to_csv("stock_returns_brl.csv", index=True)
# test = web.DataReader(["ITUB4.SA", "FB"], 'yahoo', start_date, end_date)

