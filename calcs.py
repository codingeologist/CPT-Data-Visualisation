import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
##########################################################################################################################################################################
Tk().withdraw()
file = askopenfilename(filetypes=[('EXCEL Files','*.xls')])
data_source = pd.read_excel(file,header=0,true_values=True)
#data_source
##########################################################################################################################################################################
#Data_Source
z  = data_source['SCPT_DPTH']        #Depth
qc = data_source['SCPT_RES']          #Cone Resistance
fs = data_source['SCPT_FRES']         #Sleeve Friction
u2 = data_source['SCPT_PWP2']         #U2 pore pressure
##########################################################################################################################################################################
#Assumptions
title = 'CPT01'                       #CPT test number
gwl = 3.5                             #ground water level
soil_den = 18                         #soil density
max_depth = 30                        #Maximum depth to display plots
##########################################################################################################################################################################
#Calculations
u0 = [0]                              #Hydrostatic water pressure
for i in np.arange(len(z)):
    if z[i] < gwl:
        u0.append(0)
    elif z[i] > gwl:
        u0.append((z[i] - gwl)*10)

udl = (u2 - u0)                                                                             #U_delta
sig_vo = z * soil_den                                                                       #Total Vertical Stress
sig1_vo = sig_vo - u0                                                                       #Effective Vertical Stress
np.seterr(divide='ignore')                                                                  #Ignore math errors
Rf = (fs/qc) * 100                                                                          #Friction Ratio
qt = (qc*1000) + (0.21+u2)                                                                  #qt kPa
qn = qt - sig_vo                                                                            #net qc
Bq = udl/(qn)                                                                               #Pore pressure ratio
qtm = qt/1000                                                                               #qt MPa
Su_15 = qn / 15                                                                             #Su Nkt = 15
Su_15 = qn / 20                                                                             #Su Nkt = 20
qt_norm = qn / sig1_vo                                                                      #normalised qc
fr_norm = ((fs * 1000) / qn) * 100                                                          #normalised fs
ic = np.sqrt(np.power(((3.47-(np.log10(qc/0.1)))),2) + np.power(((np.log10(Rf)+1.22)),2))   #Soil Behaviour Type Index
##########################################################################################################################################################################