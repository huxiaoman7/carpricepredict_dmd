def heatmap(x,y,dataframe):
	plt.figure(figsize=(x,y))
	n_variables = ['symboling','wheelbase','carlength', 'carwidth', 'carheight', 'curbweight', 'enginesize', 'boreratio', 'stroke','compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg','price']
	pc = dataframe[n_variables].corr(method='pearson')
	cols = n_variables
	sns.heatmap(pc,annot=True,yticklabels=cols,xticklabels=cols,annot_kws={'size':10},cmap='coolwarm')
	plt.show()
  
heatmap(20,12,data)
