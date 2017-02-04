# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:24:03 2017

@author: caenglish
"""

import bs4 as bs
import pickle
import requests
import PyPDF2

class get_ticker_list:
    def __init__(self, ticker_name):
        ticker_name=ticker_name
    

#This section is from https://www.youtube.com/watch?v=C--57BP79EM
    def download_sp500_tickers():
        print("Updating list of S&P500 stocks from wikipedia ...")
        resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs.BeautifulSoup(resp.text,'lxml')
        table = soup.find('table', {'class':'wikitable sortable'})
        tickers=[]
        for row in table.findAll('tr')[1:]:
            ticker=row.findAll('td')[0].text
            tickers.append(ticker)
            with open('sp500tickers.pickle','wb') as f:
                pickle.dump(tickers, f)
        return tickers
    
    def download_russell3000_ticker():
        print('Updating list of Russell3000 stocks ...')
        print('Warning: list may be out of date as download is not automated and relies on a saved pdf. Check https://www.ftserussell.com/membership-russell-3000 for the latest list.')
        pdfFileObj = open('Russell3000_ticker_list.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        tickers=[]
        for i in range(pdfReader.numPages-1):
            pageObj = pdfReader.getPage(i)
            text=pageObj.extractText()
            text=text.split('\n')
            for j in range(len(text)):
                text[j]=text[j].replace(' ','')
            for j in range(3,len(text)-5,2):
                if text[j]!='Ticker':
                    tickers.append(text[j])
    
        with open('rus3000tickers.pickle','wb') as f:
                pickle.dump(tickers, f)
                
        return tickers

        
    def get_sp500_ticker():
        with open('sp500tickers.pickle','rb') as f:
            ticker_list=pickle.load(f)
        return ticker_list

    def get_russell3000_ticker():
        with open('rus3000tickers.pickle','rb') as f:
            ticker_list=pickle.load(f)
        return ticker_list