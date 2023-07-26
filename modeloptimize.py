from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train,y_train)


rfe = RFE(estimator=LinearRegression(), n_features_to_select=10)
rfe = rfe.fit(x_train,y_train)

for z in range(len(X_train.columns)):
    print(X_train.columns[z],'\t\t\t',rfe.support_[z])


col = x_train.columns[rfe.support_]
for x in col:
    print(x)

X_train_rfe = x_train[x_train.columns[rfe.support_]]
X_train_rfe.head()


import statsmodels.api as sm 

def color_code_vif_values(val):
    """
    Take a scalar and return a string with the property css 'color: red' for 10, black otherwise.
    """
    if val > 10 : color = 'red' 
    elif val > 5 and val <= 10 : color = 'blue'
    elif val > 0 and val <= 5 : color = 'darkgreen'
    else : color = 'black'
    return 'color: %s' % color

def drop_col(dataframe,col_to_drop) :
    dataframe.drop([col_to_drop],axis=1,inplace=True)
    return dataframe

def display_vif(x) :
    #Calculer les VIFs pour le nouveau modèle
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    vif = pd.DataFrame()
    X = x
    vif['Features'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.set_index("Features")
    vif = vif.sort_values(by = "VIF", ascending = False)
    df = pd.DataFrame(vif.VIF).style.applymap(color_code_vif_values)
    with open('str.html','w') as f:
        df.to_html(f)
    filename = ' str.html'
    webbrowser.open_new_tab(filename)

 
model_count = 0

def statsmodel_summary(y_var,x_var) :
    global model_count
    model_count = model_count + 1
    text = "*****MODEL - " + str(model_count)
    print(text)
    
    x_var_const = sm.add_constant(x_var) # adding constant
    lm = sm.OLS(y_var,x_var_const).fit() # calculating the fit
    print(lm.summary()) # print summary for analysis
    display_vif(x_var_const.drop(['const'],axis=1))
    return x_var_const , lm


lm = statsmodel_summary(y_train,X_train_rfe)


x_var_const = sm.add_constant(X_train_rfe)
display_vif(x_var_const.drop(['const'],axis=1))
with open('str.html','w') as f:
    df.to_html(f)

filename = ' str.html'
webbrowser.open_new_tab(filename)
