#!/usr/bin/python
# coding: UTF-8

import tushare as ts 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import talib 

df=ts.get_k_data('600600') 
df['MA10_rolling'] = pd.rolling(df['close']).mean(10) 
close = [float(x) for x in df['close']] # 调用talib计算10日移动平均线的值 
df['MA10_talib'] = talib.MA(np.array(close), timeperiod=10) 
df.tail(12)
