import os
import datetime as dt
import pandas_datareader.data as web
 
#銘柄コード入力(7177はGMO-APです。)
ticker_symbol_1 = "^NIKKEI"
ticker_symbol_dr_1 = ticker_symbol_1 + ".T"

ticker_symbol_2 = "^GSPC"
ticker_symbol_dr_2 = ticker_symbol_2 + ".T"

#2022-01-01以降の株価取得
start='2022-7-1'
end = dt.date.today()
 
#データ取得
df = web.DataReader(ticker_symbol_dr, data_source='yahoo', start=start,end=end)

print(df)