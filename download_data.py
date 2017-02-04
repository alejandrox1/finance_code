# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:08:45 2017

@author: caenglish
"""
import os
import pandas_datareader.data as web

class DownloadData:
        
    def DownloadSymbolYahoo(ticker_list,start,end):
        for i in ticker_list:
            if not os.path.exists('equity_data/{}.csv'.format(i)):
                print('Downloading: {}'.format(i))
                try:
                    df = web.DataReader(i, 'yahoo', start, end)
                    df.to_csv('equity_data/{}.csv'.format(i))
                except:
                    print('Could not download: {}'.format(i))
                    
            else:
                print("Already have {}".format(i))
                
    
    