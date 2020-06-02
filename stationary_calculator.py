"""Write a reusable stationarity calculator function"""

import pandas as pd
import numpy as np
import statsmodels as sm

from statsmodels.tsa.stattools import adfuller

def stationary_calculator(data, sig_threshold):
    
    the_test = adfuller(data)
    
    adf_statistic = the_test[0]
    adf_pvalue = the_test[1]
    
    if adf_pvalue > sig_threshold:
        print("Your data is non-stationary and has a time-dependent structure.")
        print("Test: Augmented Dickey-Fuller")
        print('ADF Statistic: %f' % adf_statistic)
        print('ADF p-value: %f' % adf_pvalue)
    else:
        print("Your data is stationary.")
        print("Test: Augmented Dickey-Fuller")
        print('ADF Statistic: %f' % adf_statistic)
        print('ADF p-value: %f' % adf_pvalue)