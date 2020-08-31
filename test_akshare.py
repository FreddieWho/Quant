import akshare as ak
import pandas as pd

allStockID = ak.stock_zh_a_spot()
allStockID.to_csv('allStockID.csv')

allHistory = {}

for symbol in allStockID['symbol']:
    print(symbol)
    current = stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol=symbol, adjust="hfq",)
    allHistory[symbol] = current

allHistory = pd.concat(allHistory)

allHistory.to_json('allHistory.json')