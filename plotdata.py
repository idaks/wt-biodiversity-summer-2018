#to get this module to work, you have to:
#1. install the libraries: numpy, pandas, matplotlib, seaborn, Basemap
#installation instruction of seaborn library: https://seaborn.pydata.org/installing.html
#installation instruction of Basemap: https://matplotlib.org/basemap/users/installing.html
#2. read into a Darwin-core based species occurence dataset, such as: 
#d1=pd.read_csv("FILEPATH.csv",error_bad_lines=False)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap

def plotdata(d,t): #d= datasets; t= taxonomy name in text. e.g. plotdata (d1, "Weakley 2014")
	sns.lmplot( x="decimalLongitude", y="decimalLatitude", data=d, fit_reg=False, hue='scientificName', legend=False, size=10, aspect=1.5)
	plt.legend(loc='lower right')
	plt.title(t)
	m=Basemap(llcrnrlat = 23.05,llcrnrlon = -126.58, urcrnrlat = 50.43, urcrnrlon = -64.09) #this is where the map's geo-locations are 
	m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
	m.fillcontinents(color='grey', alpha=0.3)
	m.drawcoastlines(linewidth=0.1, color="white")
	plt.savefig(t, bbox_inches='tight') #this line directly saves the figures in PNG format

