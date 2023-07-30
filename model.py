from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,scale
cars_train, cars_test= train_test_split(data, train_size=0.67, test_size=0.33, random_state = 0)
sc = StandardScaler() 

col_to_scale = ['wheelbase','boreratio','horsepower','citympg','price']

cars_train[col_to_scale] = sc.fit_transform(cars_train[col_to_scale])
cars_test[col_to_scale] = sc.fit_transform(cars_test[col_to_scale])

y_train = cars_train.loc[:,cars_train.columns == 'price']
x_train = cars_train.loc[:, cars_train.columns != 'price']

y_test = cars_test.loc[:,cars_test.columns == 'price']
x_test = cars_test.loc[:, cars_test.columns != 'price']

cars_train.head()

#构建模型
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm 
model = LinearRegression()
model.fit(x_train,y_train)
result = sm.OLS(y_train,x_train).fit()
result.summary()

#模型检验
y_pred=result.predict(x_test)
resid = y_test - y_pred.to_frame('price')
fig = plt.figure(figsize=(9,6))
sns.distplot(resid, bins = 20)
fig.suptitle('Error Terms', fontsize = 20)                  
plt.xlabel('Errors', fontsize = 18)
plt.show()

plt.figure(figsize=(9,9))
plt.scatter(y_pred, resid)
plt.hlines(0,-2,4)
plt.suptitle('Residuals vs Predictions', fontsize=16)
plt.xlabel('Predictions')
plt.ylabel('Residuals')

plt.figure(figsize=(15,9))
plt.scatter(resid.index, resid.values)
plt.hlines(0,0,200)
plt.suptitle('Residuals by order', fontsize=16)
plt.xlabel('Order')
plt.ylabel('Residuals')
plt.show()


##Goldfeld-Quandt test 
%matplotlib inline
%config InlineBackend.figure_format ='retina'
import seaborn as sns 
import matplotlib.pyplot as plt
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
sns.set_style('darkgrid')
sns.mpl.rcParams['figure.figsize'] = (15.0, 9.0)

def homoscedasticity_test(model):
    fitted_vals = model.predict()
    resids = model.resid

    #fit_reg=False
    sns.regplot(x=fitted_vals, y=resids, lowess=True, line_kws={'color': 'red'})
    plt.suptitle('Résidus vs Prédictions', fontsize=16)
    plt.xlabel('Prédictions')
    plt.ylabel('Résidus')

    print('\n----Goldfeld-Quandt test ----')
    name = ['F statistic', 'p-value']
    test = sms.het_goldfeldquandt(lm.resid, lm.model.exog)
    print(lzip(name, test))
    print('\n----Residuals plots ----')

homoscedasticity_test(result)

#预测结果
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
