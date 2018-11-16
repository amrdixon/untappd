from scipy.stats import f as f
import pandas as pd

def anova1way(data, group, dep_var):
	#See https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
	
	
	#Use filtration to get rid of categories with <20 entries
	
	
	grouped = data.groupby(group)
		

	N = data[dep_var].count()  # conditions times participants
	n = grouped[dep_var].count() #Participants in each condition
	k = len(grouped[dep_var].count())  # number of conditions
	DFbetween = k - 1
	DFwithin = N - k
		
	SSbetween = (sum(grouped.sum()[dep_var]**2)/n) - (data[dep_var].sum()**2)/N
	
	sum_y_squared = sum([value**2 for value in data[dep_var].values])
	SSwithin = sum_y_squared - sum(grouped.sum()[dep_var]**2)/n
	
	SStotal = sum_y_squared - (data[dep_var].sum()**2)/N
	
	MSbetween = SSbetween/DFbetween
	MSwithin = SSwithin/DFwithin
	F = MSbetween/MSwithin
	
	p = f.sf(F, DFbetween, DFwithin)
	
	eta_sqrd = SSbetween/SStotal
	
	om_sqrd = (SSbetween - (DFbetween * MSwithin))/(SStotal + MSwithin)
	
	return F, p, eta_sqrd, om_sqrd