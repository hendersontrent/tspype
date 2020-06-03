"""
This is the tsplotter function.

Args:
    x: Single column which holds the x axis variable (should represent time).
    y: Single column which holds the y axis variable (should be numeric and represent the outcome)

Returns:
    Quadrant matrix of plots for raw data, density of response variable, autocorrelation function and partial autocorrelation function.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

def tsplotter(x, y, figsize = (12,8)):

    if np.issubdtype(y.dtype, np.number) == False:
        raise TypeError("tsplotter expects the y (response) variable to be a float or integer.")
    else:
        sns.set(style = "darkgrid")
        fig = plt.figure(figsize = figsize)
        layout = (2,2)
        data_ax = plt.subplot2grid(layout, (0,0))
        dens_ax = plt.subplot2grid(layout, (0,1))
        acf_ax = plt.subplot2grid(layout, (1,0))
        pacf_ax = plt.subplot2grid(layout, (1,1))
        
        sns.lineplot(x = x, y = y, 
                     ax = data_ax)
        sns.distplot(y, ax = dens_ax)
        plot_acf(y, ax = acf_ax)
        plot_pacf(y, ax = pacf_ax)
        sns.despine()
        plt.tight_layout()
        return data_ax, dens_ax, acf_ax, pacf_ax