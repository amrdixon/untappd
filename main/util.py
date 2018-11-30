import pandas as pd
from scipy import stats

def anova1way(data, group, dep_var):
	#See https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
		
	
	grouped = data.groupby(group)
	
	#Filter out rows with NaN in either the dependant variable or the independant categories
	data = data.dropna(axis=0, subset=[group, dep_var])


	N = data[dep_var].count()  # conditions times participants
	print(N)
	n = grouped[dep_var].count() #Participants in each condition
	print(n)
	k = len(grouped[dep_var].count())  # number of conditions
	print(k)
	DFbetween = k - 1
	DFwithin = N - k

	SSbetween = sum(grouped.sum()[dep_var]**2/grouped[dep_var].count()) - (data[dep_var].sum()**2)/N

	sum_y_squared = sum([value**2 for value in data[dep_var].values])
	SSwithin = sum_y_squared - sum(grouped.sum()[dep_var]**2)/data[dep_var].count()

	SStotal = sum_y_squared - (data[dep_var].sum()**2)/N

	MSbetween = SSbetween/DFbetween
	MSwithin = SSwithin/DFwithin
	F = MSbetween/MSwithin

	p = stats.f.sf(F, DFbetween, DFwithin)

	eta_sqrd = SSbetween/SStotal

	om_sqrd = (SSbetween - (DFbetween * MSwithin))/(SStotal + MSwithin)

	
	return F, p, eta_sqrd, om_sqrd
	
def ttest_single_cat(data, group, group_member, dep_var):
	
	#Drop all NaN
	data = data.dropna(axis=0, subset=[group, dep_var])
	
	group_ratings = data[data[group] == group_member][dep_var]
	not_group_ratings = data[data[group] != group_member][dep_var]


	t, p = stats.ttest_ind(group_ratings, not_group_ratings, equal_var=False)

	return t,p
	