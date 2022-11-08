# PLOT FUNCTIONS

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import Image # Convert bytes to image

from utils.colors import palette

# -----------------------------------------------

def to_img(fig, frmt='png', output='img'):
        """ Function to convert a Pyplot figure 
        into an image to display or into bytes
        frmt : Image format (png, jpeg)
        output : 
        - 'img' : Output is an image to display
        - 'bytes' Output is an image in bytes format
         """

        img_bytes = pio.to_image(
                fig, 
                format=frmt, 
                validate=True, 
                engine='orca')

        if output == 'img':
                return Image(img_bytes)

        elif output == 'bytes':
                return img_bytes

        else:
                raise NameError(
                        'Wrong parameter, please check docstring'
                        )

# -----------------------------------------------

def plot_split(series, title='', x_label='x', y_label='y', 
    splits=None, show_sup=False, kind='bar', grid=False,
    bar_color='rgb(99,110,250)', output='img'):

    # -------------- SERIES CHECK --------------
    if not isinstance(series, pd.core.series.Series):
        raise TypeError("'series' must be a Pandas Series, "+
        f"{type(series)} given")
    
    else:
        series = series.dropna()

        for idx, val in enumerate(series.values):
            if not isinstance(val, (int, float)):
                raise ValueError('Series values must only '+
                f'contain int or float, {type(val)} '+ 
                f'given at index {idx}')
            else:
                continue
    
    # -------------- BAR COLOR CHECK --------------
    if not isinstance(bar_color, (tuple, str)):
        raise TypeError('bar_color must be a tuple or str')
    
    elif isinstance(bar_color, tuple):
        if len(bar_color) != 3:
            raise ValueError('Tuple must contain 3 RGB values,'+
            f' {len(bar_color)} given')

        boo = []
        for val in bar_color:
            if isinstance(val, int) and 0 <= val <= 255:
                boo.append(True)
            else:
                boo.append(False)
        
        if all(boo):
            bar_color = f"rgb{str(bar_color)}" # OK
        else:
            raise ValueError('Wrong RGB format, must be '+
            '3 values between 0 and 255')
    
    elif isinstance(bar_color, str) and bar_color[0] == '@':
        if bar_color in palette:
            bar_color = palette[bar_color] # OK
        else:
            raise NameError("Color not found in palette")
    
    else:
        pass

    # -------------- SPLITTING PHASE 1 --------------
    if splits == None:
        splits = np.array([
            [0, 5], 
            [5, 10],
            [10, 50],
            [50, 100],
            [100, 500],
            [500, 1000],
            [1000, 5000],
            [5000, 10000]])

    # -------------- SPLITS CHECK --------------
    else:
        # Not a list
        if not isinstance(splits, list):
            raise TypeError('splits must be a list, ' + 
            f'{type(splits)} given')

        for idx, val in enumerate(splits):
            # One of the elements isn't a list
            if not isinstance(val, list):
                raise TypeError('splits must only contains lists '+
                f'{type(splits[idx])} given at index {idx} \n'+
                f'--> {splits[idx]}')

            # One sublist doesn't have a length of 2
            elif not len(val) == 2:
                raise TypeError('A split must contain 2 values '+
                f'{len(splits[idx])} given at index {idx} \n'+
                f'--> {splits[idx]}')

            # One sublist does not contain a valid number
            elif not isinstance(val[0], (int, float)) or \
                not isinstance(val[1], (int, float)):
                raise ValueError('A split must contain 2 numbers, '+
                f'int or float. --> {splits[idx]} at index {idx}')
            
            # The 2nd value isn't greater than the 1st
            elif not val[0] < val[1]:
                raise ValueError('The 2nd value of a split '+
                'must be greater than the 1st \n'+
                f'--> {splits[idx]} at index {idx}')
            
            else:
                splits = np.array(splits)

    # -------------- SPLITTING PHASE 2 --------------
    splits_dict = {}

    for splt in splits:
        part = series.loc[lambda x : (x > splt[0]) & (x <= splt[1])]
        part = np.array(part.values)
        
        splits_dict[f'{splt[0]}-{splt[1]}'] = [part, len(part)]
    
    if show_sup:
        part = series.loc[lambda x : x > splits[-1][1]]
        part = np.array(part.values)

        splits_dict[f'+{splits[-1][1]}'] = [part, len(part)]        
    
    # -------------- PLOTING --------------
    x = []
    y = []

    for key, val in splits_dict.items():
        x.append(key)
        y.append(val[1])
    
    if kind == 'bar':
        fig = px.bar(
            x=x, 
            y=y,
            title=title,
            labels={'x': x_label, 'y': y_label},
            text_auto='.5'
            )
    
        fig.update_traces(
            marker_color=bar_color
            )
        
        if grid:
            fig.update_yaxes(showgrid=True, gridcolor='black',
            gridwidth=0.5)

    elif kind == 'pie':
        fig = go.Figure(data=[go.Pie(
            labels=x, 
            values=y,
            hole=.5
            )])
        
        fig.update_layout(
            title_text = f'{title}')

    else:
        raise NameError(
            'Wrong "kind" parameter, please check parameter')
    
    # -------------- OUTPUT --------------
    if output == 'img':
        return to_img(fig)

    elif output =='fig':
        return fig
        
    else:
        raise NameError('Unrecognized "output" parameter')

# -----------------------------------------------

def plot_counts(
    series, x_label='x', y_label='y', title='', 
    frm=0, to=None, kind='bar', merge_low=None, 
    output='img'):
    """ The function allows to make a graphical representation 
    of a Pandas Series, particularly suitable for 
    values_counts().

    - series : a Pandas series
    - x_label : plot x axis name
    - y_label : plot y axis name
    - title : plot title
    - frm : series index start
    - to : series index end
    - kind : plot kind -> 'bar' or 'pie'
    - merge_low : Merging from a given value (default : None)
    - output : 'fig' (plotly object), 'img' (image), 
    'bytes' (image in bytes)
    """

    # -------------- SECURITY CHECK --------------
    if not isinstance(series, pd.core.series.Series):
        raise TypeError('Not a Pandas Series')

    # -------------- SERIES CROP TRUE --------------
    if frm != 0 or to != None:
        series = series[frm:to]

    # Axis creation
    x = series.index
    y = series.values

    # -------------- MERGING TRUE --------------
    if merge_low != None:
        x = []
        x_low = []

        y = []
        y_low = []
        
        for item in series.iteritems():
            if item[1] == 0:
                continue

            elif item[1] > merge_low:
                x.append(item[0])
                y.append(item[1])

            else:
                x_low.append(item[0])
                y_low.append(item[1])
            
        y.append(sum(y_low))
        x.append(f'Others ({len(x_low)})')

        if kind == 'bar':
            """ Convert all x_axis into string so that
            'others' label can be correctly display 
            in bar mode """ 
            
            for idx, val in enumerate(x):
                x[idx] = str(x[idx])

    # -------------- PLOT BAR --------------
    if kind == 'bar':
        fig = px.bar(
        x=x, 
        y=y, 
        title=title,
        labels={'x': x_label, 'y': y_label},
        text_auto='.2s'
        )
        
    # -------------- PIE CHART --------------
    elif kind == 'pie':
        fig = go.Figure(data=[go.Pie(
            labels=x, 
            values=y,
            hole=.5
            )])
        
        fig.update_layout(
            title_text = f'{title}'
        )
    
    # -------------- WRONG KIND --------------
    else:
        raise NameError("Parameter 'kind' not recognized, please check the docstring")

    # -------------- OUTPUT --------------
    if output == 'fig':
        return fig # pyplot object

    elif output == 'img' or output == 'bytes':

        fig.update_yaxes(
        showgrid=True,
        gridcolor='black',
        gridwidth=0.5
        )

        if output == 'img':
            return to_img(fig) # Image
        else:
            return to_img(fig, output='bytes') # Image bytes
    
    else:
        raise NameError('Wrong output parameter, please check the docstring')

# -----------------------------------------------

def plot_disc_meth(dataframe, merge_low=None, 
    title='Discovery methods', duo=None):

    from utils.column_names import disc_meth
    
    if duo == None:
        lab_list = [] # List of labels
        lab_list_low = [] # List of merged labels

        val_list = [] # List of values
        val_list_low = [] # List of merged values

        
        # COLUMNS INTERATION LOOP
        for name in disc_meth.items():
            val = dataframe.loc[dataframe[name[0]] == 1].shape[0]
            if val == 0:
                continue

            # MERGING TRUE IN LOOP
            if merge_low != None:
                if val > merge_low:
                    val_list.append(val)
                    lab_list.append(name[1])
                else: # Value will be merged
                    val_list_low.append(val)
                    lab_list_low.append(name[1])
            
            # MERGING FALSE IN LOOP
            if merge_low == None: # merged False
                val_list.append(val)
                lab_list.append(name[1])

        # MERGING TRUE OUTSIDE LOOP
        if merge_low != None:
            val_list.append(sum(val_list_low))
            lab_list.append(f"Others ({len(lab_list_low)})")
            
            other_txt = ["<b>Other methods :</b><br>"]

            for name in lab_list_low:
                if name == lab_list_low[-1]:
                    other_txt.append(name)
                else:
                    other_txt.append(name+'<br>')
            other_txt = ''.join(other_txt)

        # fig without merging
        fig = go.Figure(data=[go.Pie(
            labels=lab_list, 
            values=val_list,
            hole=.5
            )])
        
        fig.update_layout(
            title_text = f'{title}'
        )

        # SHOW ANNOTATIONS
        if merge_low != None:
            fig.add_annotation(
                x=1.31,
                y=0.22,
                text=other_txt,
                showarrow=False,
                align='right',
                width=195,
                bgcolor='gainsboro',
                bordercolor='silver',
                borderwidth=0.5
            )

        return to_img(fig)
    
    if duo != None:
        if not isinstance(dataframe, pd.core.frame.DataFrame):
            raise TypeError('"dataframe" must be a Pandas dataframe')

        elif not isinstance(duo, (list, tuple)):
            raise TypeError('"duo" must be a list or tuple')

        elif len(duo) != 2:
            raise ValueError('"duo" must only contain 2 indexes')

        elif not isinstance(duo[0], str) or \
        not isinstance(duo[1], str):
            raise ValueError('Each iterable must contain 1 index')

        elif duo[0] not in disc_meth.keys() or \
        duo[1] not in disc_meth.keys():
            raise NameError('Column name(s) not in dataframe')
        
        else:
            meth_1 = dataframe.loc[
            ((dataframe[duo[0]] == 0) & 
            (dataframe[duo[1]] == 1))
            ].shape[0]
            meth_1_lab = disc_meth[duo[1]]

            meth_2 = dataframe.loc[
            ((dataframe[duo[0]] == 1) & 
            (dataframe[duo[1]] == 0))
            ].shape[0]
            meth_2_lab = disc_meth[duo[0]]

            meth_1_2 = dataframe.loc[
            ((dataframe[duo[0]] == 1) & 
            (dataframe[duo[1]] == 1))
            ].shape[0]

            vals = [meth_1, meth_2, meth_1_2]
            labs = [f'Just by {meth_1_lab}', f'Just by {meth_2_lab}', 
            f'By {meth_1_lab} AND {meth_2_lab}']

            fig = go.Figure(data=[go.Pie(labels=labs, values=vals)])

            fig.update_layout(
            title_text = title)

            fig.update_traces(hole=.5)

            return to_img(fig)