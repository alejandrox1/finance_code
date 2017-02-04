# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:41:23 2017

@author: caenglish
"""

from get_tickers import get_ticker_list
from download_data import DownloadData
from compile_data import CompileData
from get_correlation import getCorrelation
from LabelData import LabelData
from do_ML import do_ML
import datetime as dt
from TI import TechnicalIndicator as ti
from optimize import OptimizeParam

start=dt.date(2000,1,1);end=dt.date(2016,12,31)
#get_ticker_list.download_russell3000_ticker()
ticker_list=get_ticker_list.get_russell3000_ticker()
ticker_list=ticker_list[:1]
#DownloadData.DownloadSymbolYahoo(ticker_list,start,end)
data=CompileData.OpenData(ticker_list)
#RSI=ti.McClellanOscillator(data, 19,39)
gain1=CompileData.PctChange(data,1)
RSI=ti.RSI(data, 2)
#print(RSI)
corr=getCorrelation.corr_TI(RSI, gain1,1)
print(corr)
#print(data.head(50))
#optimumTIperiod=OptimizeParam.OptimizeTIRSI(data, 'RSI', gain1)
#print(optimumTIperiod)
#print(optimumTIperiod)
#getCorrelation.plot_scatter_TI(RSI, gain1)
#corr=getCorrelation.correlation(x)
#getCorrelation.plot_heatmap(corr)
#print(ticker_list)
#X,y,df=LabelData.extract_featuresets(x,'AAC', 5)
#do_ML.do_ml(X, y, df)