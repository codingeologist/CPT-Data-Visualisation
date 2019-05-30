import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from calcs import ic, max_depth, z
##########################################################################################################################################################################
#Check Soil Behaviour Type    
sbt = []
for i in np.arange(len(ic)):

    if ic[i] > 3.6:
        sbt.append('SENS')
    elif ic[i] > 3:
        sbt.append('CLAY')
    elif ic[i]  > 2.6:
        sbt.append('Silty CLAY')
    elif ic[i] > 2:
        sbt.append('Silty SAND + Sandy SILT')
    elif ic[i] > 1.4:
        sbt.append('Silty SAND')
    elif ic[i] > 1:
        sbt.append('SAND')
    else:
        sbt.append('Undefined')
##########################################################################################################################################################################
#Initialise Figures
fig2 = plt.figure(2,figsize=(20,20),dpi=300)
ax4 = plt.subplot2grid((1,10),(0,0),rowspan=2,colspan=8)
ax5 = plt.subplot2grid((1,10),(0,8),rowspan=1,colspan=2)
##########################################################################################################################################################################
#Set axes limits
ax4.set_ylim(max_depth,0)
ax4.set_xlim(1,4)
ax4.set_ylabel('Depth (m)')
ax4.set_xlabel('SBT Ic')
ax4.xaxis.set_ticks_position('none')

ax5.set_ylim(max_depth,0)
ax5.set_xlim(0,3.6)
ax5.xaxis.set_ticks_position('none')
ax5.yaxis.set_ticks_position('none')
ax5.set_xticklabels([])
ax5.set_yticklabels([])
##########################################################################################################################################################################
#Soil Behaviour Type Legend
sbt_legend_dict = {'SAND' : 'gold','Silty SAND' : 'tan','Silty SAND + Sandy SILT' : 'sandybrown','Silty CLAY' : 'palegreen','CLAY' : 'olivedrab','SENS' : 'royalblue'}
sbtpatchList = []
for key in sbt_legend_dict:
    sbt_key = mpatches.Patch(color=sbt_legend_dict[key],label=key)
    sbtpatchList.append(sbt_key)
ax4.legend(handles=sbtpatchList)
##########################################################################################################################################################################
#SBT Legends
ax4.fill([1,1,1.4,1.4],[0,max_depth,max_depth,0],'gold',alpha=0.2,edgecolor='r')
ax4.fill([1.4,1.4,2,2],[0,max_depth,max_depth,0],'tan',alpha=0.2,edgecolor='r')
ax4.fill([2,2,2.6,2.6],[0,max_depth,max_depth,0],'sandybrown',alpha=0.2,edgecolor='r')
ax4.fill([2.6,2.6,3,3],[0,max_depth,max_depth,0],'palegreen',alpha=0.2,edgecolor='r')
ax4.fill([3,3,3.6,3.6],[0,max_depth,max_depth,0],'olivedrab',alpha=0.2,edgecolor='r')
ax4.fill([3.6,3.6,4,4],[0,max_depth,max_depth,0],'royalblue',alpha=0.2,edgecolor='r')
##########################################################################################################################################################################
#SBT Profile

for i in np.arange(len(ic)):
    
    if ic[i] > 3.6:
        ax5.plot([0,3.6],[z[i],z[i]],'royalblue',lw=4)
    elif ic[i] > 3:
        ax5.plot([0,3],[z[i],z[i]],'olivedrab',lw=4)
    elif ic[i]  > 2.6:
        ax5.plot([0,2.6],[z[i],z[i]],'palegreen',lw=4)
    elif ic[i] > 2:
        ax5.plot([0,2],[z[i],z[i]],'sandybrown',lw=4)
    elif ic[i] > 1.4:
        ax5.plot([0,1.4],[z[i],z[i]],'tan',lw=4)
    elif ic[i] > 1:
        ax5.plot([0,1],[z[i],z[i]],'gold',lw=4)
##########################################################################################################################################################################
#Plot axes grids      
ax4.grid(True)
##########################################################################################################################################################################
#Data Plots
ax4.plot(ic,z,'k-',lw=0.5)
##########################################################################################################################################################################
#Save and close figures
fig2.savefig('./sbt_profile.png',bboxinches='tight')
plt.close(fig2)










