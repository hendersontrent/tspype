#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Trent Henderson

DESCRIPTION = "tspype: time series diagnostic pipeline for Python"
LONG_DESCRIPTION = """\
tspype is a library for automating high level time series diagnostics in Python.
Some of the functionality in tspype includes:
- Automation of preliminary time series visualisations including autocorrelation and partial autocorrelation functions.
- Automation of calculations around stationarity and advice for modelling
- Automation of time series statistical decomposition and subsequent visualisation.
"""

DISTNAME = 'tspype'
MAINTAINER = 'Trent Henderson'
MAINTAINER_EMAIL = 'trent.henderson1@outlook.com'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/hendersontrent/tspype/'
VERSION = '0.1.0.'
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'numpy>=1.13',
    'scipy>=1.0',
    'pandas>=0.23',
    'matplotlib>=2.1',
    'statsmodels>=0.11',
    'seaborn>=0.10'
]


PACKAGES = [
    'tspype',
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Multimedia :: Graphics',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]


if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 6):
        raise RuntimeError("tspype requires python >= 3.6.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )