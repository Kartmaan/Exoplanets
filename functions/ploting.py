# PLOT FUNCTIONS

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import Image # Convert bytes to image

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

def plot_counts(
    series, x_label='x', y_label='y', title='', 
    frm=0, to=None, output='img'):
    """ The function allows to make a graphical representation 
    of a Pandas Series, particularly suitable for 
    values_counts()

    x_label : x axis name
    y_label : y axis name
    title : plot title
    frm : index start
    to : index end
    output : 'fig', 'img', 'bytes'
    """

    if frm != 0 or to != None:
        series = series[frm:to]

    x = series.index
    y = series.values

    fig = px.bar(
    x=x, 
    y=y, 
    title=title,
    labels={'x': x_label, 'y': y_label},
    text_auto='.2s'
    )

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
        raise TypeError('Wrong output parameter, please check the docstring')

# -----------------------------------------------

def plot_disc_meth(dataframe, merge_low=None, 
title='Discovery methods'):

    from column_names import disc_meth
    
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