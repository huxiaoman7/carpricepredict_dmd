from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train,y_train)


rfe = RFE(estimator=LinearRegression(), n_features_to_select=10)
rfe = rfe.fit(x_train,y_train)

for z in range(len(x_train.columns)):
    print(x_train.columns[z],'\t\t\t',rfe.support_[z])

#选择10个重要变量
col = x_train.columns[rfe.support_]
for x in col:
    print(x)
    
X_train_rfe = x_train[x_train.columns[rfe.support_]]
X_train_rfe.head()

#用新变量训练模型
import statsmodels.api as sm 
import webbrowser

def color_code_vif_values(val):
    if val > 10 : color = 'red' 
    elif val > 5 and val <= 10 : color = 'blue'
    elif val > 0 and val <= 5 : color = 'darkgreen'
    else : color = 'black'
    return 'color: %s' % color

def drop_col(dataframe,col_to_drop) :
    dataframe.drop([col_to_drop],axis=1,inplace=True)
    return dataframe

def display_vif(x) :
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    vif = pd.DataFrame()
    X = x
    vif['Features'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.set_index("Features")
    vif = vif.sort_values(by = "VIF", ascending = False)
    df = pd.DataFrame(vif.VIF).style.applymap(color_code_vif_values)
    df = pd.DataFrame(vif.VIF).style.applymap(color_code_vif_values)
    display(df)
#注意:如果在本地运行，可把上述的display(df)改成如下代码，会输出本地文件显示VIF值
#     with open('str.html','w') as f:
#         df.to_html(f)
#     filename = ' str.html'
#     webbrowser.open_new_tab(filename)

 
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

#删除无关变量后再运行
X_train_rfe = X_train_rfe.drop(["carbody_sedan","carbody_wagon"], axis = 1)
X_train_rfe.head()
lm = statsmodel_summary(y_train,X_train_rfe)


#删除无关变量并运行新模型
X_train_rfe = X_train_rfe.drop(["CompanyName_porsche"], axis = 1)
lm = statsmodel_summary(y_train,X_train_rfe)

#预测新模型
final_features = list(X_train_rfe.columns)

#过滤测试数据
X_test_new = x_test.filter(final_features)

X_test_new.head()

lm = sm.OLS(y_train,X_train_rfe).fit()
y_pred=lm.predict(X_test_new)

resid = y_test - y_pred.to_frame('price')

#检测模型
#1.检测残差分布
fig = plt.figure(figsize=(9,6))
sns.distplot(resid, bins = 20)
fig.suptitle('Error Terms', fontsize = 20)                 
plt.xlabel('Errors', fontsize = 18)
plt.show()

#2.检测自相关系数ACF
import statsmodels.tsa.api as smt
acf = smt.graphics.plot_acf(resid, lags=40 , alpha=0.05)
acf.show()

#3.检测同方差性
homoscedasticity_test(lm)

from scipy import stats

def normality_of_residuals_test(model):
    sm.ProbPlot(lm.resid).qqplot(line='s');
    plt.title('Q-Q plot');

    ad = stats.anderson(lm.resid, dist='norm')
    
    print(f'----Anderson-Darling test ---- \nstatistic: {ad.statistic:.4f}, critical value of 5%: {ad.critical_values[2]:.4f}')
    
normality_of_residuals_test(lm)

fig = plt.figure(figsize=(11,5))
plt.scatter(y_test,y_pred)
plt.xlabel('y_test', fontsize=18)
plt.ylabel('y_pred', fontsize=16)

#Regression Line function
f = lambda x: x

# x values of line to plot
x = np.array(y_test)

# plot fit
plt.plot(x,f(x),lw=2.5, c="orange")

#输出预测R-square
from sklearn.metrics import r2_score 
r2_score(y_test, y_pred)



