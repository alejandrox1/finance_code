# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:16:32 2017

@author: caenglish
"""

from TI import TechnicalIndicator as ti
from get_correlation import getCorrelation
import numpy as np

class OptimizeParam:
    
    def OptimizeTIRSI(data, param, gain):
        average=[]
        for i in range(1,10):
            TI=ti.RSI(data, i)
            corr=getCorrelation.corr_TI(TI, gain)
            corr=np.array(corr)
            corr=corr*corr
            average.append(np.mean(corr)) 
        return average
        