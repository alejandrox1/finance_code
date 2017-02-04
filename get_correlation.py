# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:31:32 2017

@author: caenglish
"""
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

style.use('ggplot')

#

class getCorrelation:
    #From https://www.youtube.com/watch?v=PxUzcDJBEZ4
    def visualize_data(data,name):
        data[name].plot()
        plt.show()
        
    def correlation(data):
        data_corr=data.corr()
        return data_corr
    
    def plot_heatmap(data_corr):
        data_corr_values=data_corr.values
        
        fig = plt.figure()
        ax=fig.add_subplot(1,1,1)
        
        heatmap = ax.pcolor(data_corr_values, cmap=plt.cm.RdYlGn)
        fig.colorbar(heatmap)
        ax.set_xticks(np.arange(data_corr.shape[1])+0.5,minor=False)
        ax.set_yticks(np.arange(data_corr.shape[1])+0.5,minor=False)
        ax.invert_yaxis()
        ax.xaxis.tick_top()
        
        column_labels = data_corr.columns
        row_labels = data_corr.index
        
        ax.set_xticklabels(column_labels)
        ax.set_yticklabels(row_labels)
        plt.xticks(rotation=90)
        heatmap.set_clim(-1,1)
        plt.tight_layout()
        plt.show()
        
    def corr_TI(ti, gain,period):
        corr=[]
        for i in range(len(ti.columns)):
            x=ti.ix[:,i]
            y=gain.ix[:,i]
            x=x.shift(1)
            z=pd.concat([x, y], axis=1)
            z.dropna(inplace=True)
            corr.append(z.corr().ix[0,1])
            print(z)
        return corr

            

    def plot_scatter_TI(ti, gain):
        data=ti.join(gain, how='outer',lsuffix='_TI', rsuffix='_pc')
        data.dropna(inplace=True)
        plt.scatter(ti, gain)
        plt.show()
        
        