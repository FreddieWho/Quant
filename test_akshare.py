import akshare as ak

allStockID = ak.stock_zh_a_spot()

allHistory = {}

for symbol in allStockID['symbol']:
    current = stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol=symbol, adjust="hfq")
    allHistory[symbol] = current

