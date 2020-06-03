# tspype
Time Series Python Pipeline (`tspype`). Builds a Python package to host time series functions I have written and re-use often.

## Installation

You can install `tspype` from GitHub by running the following:

```
pip install git+https://github.com/hendersontrent/tspype/
```

## Dependencies

`tspype` uses [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/), and [statsmodels](https://www.statsmodels.org/stable/index.html).

## Examples

One of the packages main functions `tsplotter` produces a matrix of plots similar to below. It plots the raw time series data, density of the response variable, autocorrelation function and partial autorcorrelation function.
[](https://github.com/hendersontrent/tspype/blob/master/blob/tsplotter.png)

Another core function is `decomposer` which produces plots of time series features in a decomposed format, such as trend, seasonality and residuals.
[](https://github.com/hendersontrent/tspype/blob/master/blob/decomposer.png)
