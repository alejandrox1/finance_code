# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:56:41 2017

@author: caenglish
"""

import numpy as np
import pandas as pd
import pickle
from collections import Counter
#From https://www.youtube.com/watch?v=Z-5wNWgRJpk
class LabelData:

    def process_data_for_labels(df, ticker, hm_days):
        tickers=df.columns.values.tolist()
        df.fillna(0, inplace=True)
        
        for i in range(1,hm_days+1):
            df['{}_{}d'.format(ticker,i)]=(df[ticker].shift(-i)-df[ticker])/df[ticker]

        df.fillna(0, inplace=True)
        return tickers, df
    
    #https://www.youtube.com/watch?v=0IHy7J44Xxo
    def buy_sell_hold(*args):
        cols=[c for c in args]
        requirement=0.02
        for col in cols:
            if col > requirement:
                return 1
            elif col < -requirement:
                return -1
            else:
                return 0
        
    #https://www.youtube.com/watch?v=zPp80YM2v7k  
    def extract_featuresets(data, ticker, hm_days):
        tickers, df = LabelData.process_data_for_labels(data, ticker, hm_days)
        
        df['{}_target'.format(ticker)]=list(map( LabelData.buy_sell_hold,df['{}_1d'.format(ticker)],df['{}_2d'.format(ticker)],df['{}_3d'.format(ticker)],df['{}_4d'.format(ticker)],df['{}_5d'.format(ticker)]))
        
        #print(df['{}_target'.format(ticker)])
        vals=df['{}_target'.format(ticker)].values.tolist()
        str_vals=[str(i) for i in vals]
        print('Data spread:',Counter(str_vals))
        
        
        df.fillna(0, inplace=True)
        df=df.replace([np.inf,-np.inf],np.nan)
        df.dropna(inplace=True)
        
        df_vals=df[[ticker for ticker in tickers]].pct_change()
        df_vals=df_vals.replace([np.inf,-np.inf],0)
        df_vals.fillna(0,inplace=True)
        
        X = df_vals.values
        y = df['{}_target'.format(ticker)].values
    
        return X, y, df
        