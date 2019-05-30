import matplotlib.pyplot as plt
from calcs import max_depth, z, qc, fs, u2, u0, Rf, Bq
##########################################################################################################################################################################
#Initialise Figures
fig = plt.figure(1,figsize=(20,20),dpi=300)
ax1 = plt.subplot2grid((1,10),(0,0),rowspan=1,colspan=2)
ax1_1 = ax1.twiny()
ax2 = plt.subplot2grid((1,10),(0,4),rowspan=1,colspan=2)
ax2_1 = ax2.twiny()
ax3 = plt.subplot2grid((1,10),(0,8),rowspan=1,colspan=2)
ax3_1 = ax3.twiny()
##########################################################################################################################################################################
#Set axes limits
ax1.set_xlim(0,40)
ax1.set_ylim(max_depth,0)
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('qc (MPa)')
ax1_1.set_xlim(0,1)
ax1_1.set_ylim(max_depth,0)
ax1_1.set_xlabel('fs (MPa)')

ax2.set_xlim(0,10)
ax2.set_ylim(max_depth,0)
ax2.set_ylabel('Depth (m)')
ax2.set_xlabel('Excess Pore Pressure (kPa)')
ax2_1.set_xlim(0,300)
ax2_1.set_ylim(max_depth,0)
ax2_1.set_xlabel('Hydrostatic (kPa)')

ax3.set_xlim(-10,10)
ax3.set_ylim(max_depth,0)
ax3.set_ylabel('Depth (m)')
ax3.set_xlabel('Friction Ratio')
ax3_1.set_xlim(-5,5)
ax3_1.set_ylim(max_depth,0)
ax3_1.set_xlabel('Pore Pressure Ratio')
##########################################################################################################################################################################
#Plot axes grids
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
##########################################################################################################################################################################
#Data Plots
ax1.plot(qc,z,'k-',lw=0.5)
ax1_1.plot(fs,z,'r-',lw=0.5)

ax2.plot(u2,z,'b-',lw=0.5)
ax2_1.plot(u0,z,'r-',lw=0.5)

ax3.plot(Rf,z,'k-',lw=0.5)
ax3_1.plot(Bq,z,'b-',lw=0.5)
##########################################################################################################################################################################
#Save and close figures
fig.savefig('./raw_data.png',bboxinches='tight')
plt.close(fig)
##########################################################################################################################################################################