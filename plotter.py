import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class plotter(object):
	''''''
	def __init__(self,dataframe_name):
		self.table = dataframe_name


	def percent_stacked(self,barcol,colorcol,nan_exclude = 'True'):
		'''To plot the side by side plot on the given fields '''
		df = eval("self.table.groupby(['"+colorcol+"'])."+barcol+".value_counts(dropna="+nan_exclude+")")
		df = df.unstack()
		df = df.div(df.sum())
		df.T.plot(kind = 'bar',stacked = True,rot = 90,figsize = (10,4),title =barcol+' and '+colorcol)


	def sbs_chart(self,barcol,colorcol,nan_exclude = 'True'):
		'''To plot the percent stacked plot on the given fields '''
		df = eval("self.table.groupby(['"+colorcol+"'])."+barcol+".value_counts(dropna="+nan_exclude+")")
		df.unstack(0).plot(kind = 'bar',stacked = False,rot = 90,figsize = (10,4),title =barcol+'and'+'colorcol')

	def get_alert_array(self,row_num,feature_names_list):
		dataframe = self.table[feature_names_list].fillna(0)
		for i in feature_names_list:
			dataframe[i+'_scaled'] = (max(dataframe[i])-dataframe[i])/(max(dataframe[i])-min(dataframe[i]))
		dataframe = dataframe[[i for i in dataframe.columns if '_scaled' in i]]
		alert_array	 = dataframe.iloc[row_num,:]
		return alert_array	

	def radial_plot_profile(self,row_num,feature_names_list,color_field):
		state_val = self.table.iloc[row_num,:][color_field]
		if state_val ==1:
			color_val = 'r'
		else:
			color_val = 'g'
		alert_np_array = self.get_alert_array(row_num,feature_names_list)
		angles  = np.linspace(0, 2* np.pi, len(feature_names_list),endpoint = False)
		stats = np.concatenate((alert_np_array,[alert_np_array[0]]))
		angles =np.concatenate((angles,[angles[0]]))
		fig = plt.figure()
		ax = fig.add_subplot(111, polar = True)
		ax.plot(angles, stats, 'o-', linewidth = 2)
		ax.fill(angles, stats, alpha = 0.25, color = color_val)
		ax.set_thetagrids(angles*180/np.pi,feature_names_list)
		ax.grid(True)

if __name__ == '__main__':
	plot_me = plotter()




