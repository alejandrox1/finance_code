# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:42:54 2017

@author: caenglish
"""

import pandas as pd

class CompileData:
    
    #From https://www.youtube.com/watch?v=j0zW_KXyQJ4
    def OpenData(tickers):
        main_df = pd.DataFrame()
        
        for count, ticker in enumerate(tickers):
            try:
                df=pd.read_csv('equity_data/{}.csv'.format(ticker))

                df.set_index('Date',inplace=True)
                df.rename(columns={'Adj Close':ticker},inplace=True)
                df.drop(['Open','High','Low','Close','Volume'], axis=1, inplace=True)
            
                if main_df.empty:
                    main_df=df
                else:
                    main_df=main_df.join(df, how='outer')
            except:
                pass
                
                
            #if count % 10 == 0:
                #print(count)
        
        return main_df
        
    def PriceChange(price, win):
        delta=price.diff(periods=win)
        return delta
        
    def PctChange(price, period):
        pct_change=price.pct_change(periods=period)
        return pct_change