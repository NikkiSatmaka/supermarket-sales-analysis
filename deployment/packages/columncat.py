#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

"""
Useful functions to manipulate pandas column with object dtype
"""


def unique_count(data):
    """
    Count the number of unique categories in each object dtype columns

    Parameters
    ----------
    data : DataFrame

    Returns
    -------
    DataFrame
        Number of unique values of each column
    """
    return pd.DataFrame.from_records(
        [(col, data[col].nunique()) for col in data.select_dtypes('object').columns],
        columns=['Column Name', 'Num Unique']
    )


def categorize(data, threshold=20, exclusion=[]):
    """
    Convert object dtype columns within a certain threshold into categorical dtype

    Parameters
    ----------
    data : DataFrame
    threshold : integer or real
        The max number of unique values (inclusive) allowed to determine
        whether a column will be converted into categorical data
    exclusion : array-like, Series, or list of arrays/Series
        Columns to be excluded from conversion

    Returns
    -------
    DataFrame
        DataFrame which columns have been categorized
    """
    if type(data) != pd.DataFrame:
        raise TypeError('Not a valid DataFrame')

    if type(threshold) != int:
        raise TypeError('threshold only accepts integer')
    
    if type(exclusion) not in (list, tuple, pd.Series):
        raise TypeError('exclusion only accepts list, tuple or pandas Series')

    for col in data.select_dtypes('object').columns:
        if data[col].nunique() <= threshold and col not in exclusion:
            data[col] = pd.Categorical(data[col])

    return data

