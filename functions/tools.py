# TOOL FUNCTIONS

import pandas as pd
from datetime import datetime
from sys import getsizeof

from functions.arithm import perc

""" def perc(total, partial, rnd=2):
    x = (partial / total) * 100

    return round(x, rnd) """

def mem(obj, unit='KB', rnd=2):
    """ Function returning the memory size of an object 
    obj : type <object>
    unit : type <str> ['B', 'KB', 'MB']
    rnd : type <number>  
    """
    if unit == 'B':
        obj_mem = getsizeof(obj)
    elif unit == 'KB':
        obj_mem = getsizeof(obj) / 1000
    elif unit == 'MB':
        obj_mem = getsizeof(obj) / 1000000
    else:
        raise ValueError("Wrong inputs, please check docstring")
    
    return round(obj_mem, rnd)

# ------------------------------------------------

def nan(col, df=None, show_more = False):
    """ This function allows to know the integrity 
    level of a given column in a Dataframe or in a Series. 
    It returns in a tuple the number of no-NaN rows 
    as well as its percentage represented.
    
    If a Pandas dataframe has been entered as a parameter 
    (df=pandas.core.frame.DataFrame) then 'col' must be the 
    desired column name (col=string)

    If no dataframe has been entered (df=None) 
    then 'col' must be a Pandas Series
    (col=pandas.core.series.Series)

    The 'show_more' parameter (boolean) allows to display 
    additional information such as the amount of 
    NaN data and the total number of rows :
    False -> return (no-NaN rows, integrity %)
    True -> return (no-NaN rows, integrity %, NaN rows, total rows)
    """

    if isinstance(df, pd.core.frame.DataFrame):
        rows = df.shape[0]
        nan = df[col].isna().sum()
        ok = df.shape[0] - nan
        integrity = round(perc(rows, ok), 3)
    
    elif isinstance(col, pd.core.series.Series):
        rows = col.shape[0]
        nan = col.isna().sum()
        ok = col.shape[0] - nan
        integrity = round(perc(rows, ok), 3)
    
    else:
        raise TypeError('WRONG INPUTS IN PARAMETERS')
        
    if not show_more:
        return (ok, integrity)

    else:
        return (ok, integrity, nan, rows)

# ------------------------------------------------

def date_minmax(col, df=None, fmt='%Y-%m-%d', mode='max', debug=False):
    """ Returns the earliest or latest date of a column
    from a Pandas dataframe or from a Pandas Series 
    
    If a dataframe has been entered as a parameter 
    (df=pandas.core.frame.DataFrame) then 'col' must be the 
    desired column name (string)
    
    If no dataframe has been entered (df=None) 
    then 'col' must be a Pandas Series

    The default date format on which the function 
    is based is '%Y-%m-%d' but this can be changed 
    using the 'fmt' parameter

    The 'mode' parameter can have two states :
    - 'max' : (default) Returns the most recent date
    - 'min' : Returns the earliest date
    """
    errors = 0

    if isinstance(df, pd.core.frame.DataFrame):
        datetime_list = []
        for date in df[col]:
            try:
                datetime_list.append(datetime.strptime(date, fmt))
            except TypeError:
                errors+=1
                continue
            except ValueError:
                errors+=1
                continue

    elif isinstance(col, pd.core.series.Series):
        datetime_list = []
        for date in col:
            try:
                datetime_list.append(datetime.strptime(date, fmt))
            except TypeError:
                errors+=1
                continue
            except ValueError:
                errors+=1
                continue
    
    else:
        raise TypeError('WRONG INPUTS IN PARAMETERS')

    if debug and errors > 0:
        print(f"{errors} rows have been ignored due to errors")

    if mode == 'max':
        return max(datetime_list)
    else:
        return min(datetime_list)

# ------------------------------------------------

def to_df(series, label_idx='index',
    label_val='values', frm=0, to=None):
    """ Transforms a Series into a Dataframe by allowing 
    to adjust several parameters:
    - label_idx : name of the index column
    - label_val : name of the values column
    - frm : index from which to display (default : 0)
    - to : limit index to display (default : last index [None])
    """

    if not isinstance(series, pd.core.series.Series):
        raise TypeError("Not a Pandas Series")

    series = series.iloc[frm:to]

    dtf = pd.DataFrame({
        label_idx:series.index,
        label_val:series.values})
    
    return dtf