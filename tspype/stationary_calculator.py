"""
This is the stationary_calculator function.

Args:
    data: Single column which holds the y axis variable (should be time-ordered, numeric and represent the outcome)
    sig_threshold (float): Decimal number corresponding to p-value cutoff for the Dickey-Fuller unit root test. Suggested value is 0.05.

Returns:
    Dickey-Fuller test statistic, p-value, and commentary on whether data is time-dependent or stationary.
"""

import pandas as pd
import numpy as np
import statsmodels as sm

from statsmodels.tsa.stattools import adfuller

def stationary_calculator(data, sig_threshold):
    
    if np.issubdtype(y.dtype, np.number) == False:
        raise TypeError("stationary calculator expects vector data as a float or integer.")
    elif isinstance(sig_threshold, float) == False:
        raise TypeError("Significance threshold should be specified as a decimal number float")
    else:
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