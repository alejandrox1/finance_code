# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:57:03 2017

@author: caenglish
"""
import numpy as np

class TechnicalIndicator:
    
    def RSI(price, win):
        delta=price.diff()
        dUp, dDown = delta.copy(), delta.copy()
        dUp[dUp < 0] = 0
        dDown[dDown > 0] = 0
        RolUp=dUp.rolling(window=win,center=False).mean()
        RolDown = dDown.rolling(window=win,center=False).mean().abs()
        RS = RolUp / RolDown
        RS=RS.replace(np.inf, np.NaN)
        RSI=100.0-((100.0)/(1+RS))
        return RSI
    
    def McClellanOscillator(price, win_s, win_l): 
        ema_s = price.ewm(com=win_s).mean()
        ema_l = price.ewm(com=win_l).mean()
        mcclellan_oscillator=(ema_s-ema_l)*100.0
        return mcclellan_oscillator