# ARITHMETIC FUNCTIONS
def perc(total, partial, rnd=2):
    """ Function to calculate the percentage represented 
    by a partial value on a total value 
    total : type <number>
    partial : type <number>
    rnd : type <number>
    """

    x = (partial / total) * 100

    return round(x, rnd)

def perc_var(start, end, rnd=2):
    """ Function to calculate the variation between 
    an initial (start) and final (end) value in percentage
    start : type <number>
    end : type <number>
    rnd : type <number> 
    """

    variation = ((end - start) / start) * 100

    return round(variation, rnd)