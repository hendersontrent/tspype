"""Builds a reusable decomposition function"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.tsa.seasonal import seasonal_decompose

def decomposer(data, x, y, periods, figsize = (12,8)):
        decomposition = seasonal_decompose(y, period = periods)

        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
    
        sns.set(style = "darkgrid")
        fig = plt.figure(figsize = figsize)
        layout = (2,2)
        orig_ax = plt.subplot2grid(layout, (0,0))
        trend_ax = plt.subplot2grid(layout, (0,1))
        seas_ax = plt.subplot2grid(layout, (1,0))
        resid_ax = plt.subplot2grid(layout, (1,1))
    
        sns.lineplot(x = x, y = y, 
                     data = data, ax = orig_ax)
        trend.plot(ax = trend_ax, title = 'Trend')
        seasonal.plot(ax = seas_ax, title = 'Seasonal')
        residual.plot(ax = resid_ax, title = 'Residual')
        plt.tight_layout()
        return orig_ax, trend_ax, seas_ax, resid_ax