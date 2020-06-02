"""Builds a function that returns a time series plot, density of y values, ACF and PACF"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

def tsplotter(x, y, data, figsize = (12,8)):
    sns.set(style = "darkgrid")
    fig = plt.figure(figsize = figsize)
    layout = (2,2)
    data_ax = plt.subplot2grid(layout, (0,0))
    dens_ax = plt.subplot2grid(layout, (0,1))
    acf_ax = plt.subplot2grid(layout, (1,0))
    pacf_ax = plt.subplot2grid(layout, (1,1))
    
    sns.lineplot(x = x, y = y, 
                 data = data, ax = data_ax)
    sns.distplot(y, ax = dens_ax)
    plot_acf(y, ax = acf_ax)
    plot_pacf(y, ax = pacf_ax)
    sns.despine()
    plt.tight_layout()
    return data_ax, dens_ax, acf_ax, pacf_ax