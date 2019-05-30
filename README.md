# CPT-Data-Visualisation
Geotechnical Cone Penetration Testing Data Visualisation

Reference Book on CPT techniques and analysis: T. Lunne , J.J.M Powell, P.K. Robertson: Cone Penetration Testing in Geotechnical Practice
Amazon Link: https://www.amazon.co.uk/Cone-Penetration-Testing-Geotechnical-Practice/dp/041923750X

Three Python scripts have been created to perform the calculations and data visualisation based on the techniques provided by Lunne et al 
and according to Geotechnical industry practice (British Standard: BS EN ISO 22476-1:2012)

The Raw data is loaded into Python from *.xls files*, with four columns of data representing  the required datasets. The first row of each of the columns saved within the excel files assumes a header with the standard [AGS4](https://www.ags.org.uk/) headers.
  1) Test Depth (SCPT_DPTH).
  2) Tip Resistance (SCPT_RES).
  3) Cone Sleeve Friction (SCPT_FRES).
  4) Measured Pore Pressure (U2 position, behind the tip) (SCPT_PWP2).
  
 Calculations:
 This is performed within the *calcs.py* script. The user should satisfy themselves that the assumptions used for the calculations are   repreentative of the ground conditions.

Graphing:
The *raw_grapher.py* script has been setup to import the requried parameters for producing the standard tip resistance, sleeve friction and pore pressure plots. The resuting plots will be saved as a *.png file* within the specified root folder.

Soil Behaviour Type Index:
The *sbt_index.py* script reads the calculated *Ic - Soil Behavior Type Index* arrays and plots the data with the representative descriptions based on the industry standard guidance and Lunne et al. Two plots are saved as a *.png file* within the specified root folder, illustrating the test trace as well as an _interpreted_ soil column.
