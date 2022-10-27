""" 
Classification of column names by category so they can easily 
be iterated
"""

# Masses
mass_cols = {
    'pl_masse' : "Planet's matter mass [Earth Mass]", 
    'pl_massj' : "Planet's matter mass [Jupiter Mass]",
    'pl_msinie' : 'Minimum mass by radial velocity [Earth Mass]',
    'pl_msinij' : 'Minimum mass by radial velocity [Jupiter Mass]',
    #'pl_cmasse' : None, # Deleted column
    #'pl_cmassj' : None, # Deleted column
    'pl_bmasse' : 'Best mass avaiable [Earth Mass]',
    'pl_bmassj' : 'Best mass avaiable [Jupiter Mass]' 
    }

# Discovery methods
disc_meth = {
    'rv_flag':'Radial Velocity',
    'pul_flag':'Pulsar Timing Variation',
    'ptv_flag':'Pulsation Timing Variation',
    'tran_flag':'Transit',
    'ast_flag':'Astrometric Variations',
    'obm_flag':'Orbital Brightness Modulations',
    'micro_flag':'Microlensing',
    'etv_flag':'Eclipse Timing Variations',
    'ima_flag':'Imaging',
    'dkin_flag':'Disk Kinematics'
    }