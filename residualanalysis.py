lm = sm.OLS(y_train,x_train).fit()
y_pred=lm.predict(x_test)
resid = y_test - y_pred.to_frame('price')
fig = plt.figure(figsize=(9,6))
sns.distplot(resid, bins = 20)
fig.suptitle('Error Terms', fontsize = 20)   

####残差的正态分布检验####
plt.xlabel('Errors', fontsize = 18)
plt.show()
plt.figure(figsize=(9,9))
plt.scatter(y_pred, resid)
plt.hlines(0,-2,4)
plt.suptitle('Residuals vs Predictions', fontsize=16)
plt.xlabel('Predictions')
plt.ylabel('Residuals')
plt.show()

######残差的独立性检验######
plt.figure(figsize=(15,9))
plt.scatter(resid.index, resid.values)
plt.hlines(0,0,200)
plt.suptitle('Residuals by order', fontsize=16)
plt.xlabel('Order')
plt.ylabel('Residuals')
plt.show()


####残差的同方差检验######
import seaborn as sns 
import matplotlib.pyplot as plt
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
sns.set_style('darkgrid')
sns.mpl.rcParams['figure.figsize'] = (15.0, 9.0)

def homoscedasticity_test(model):
    fitted_vals = model.predict()
    resids = model.resid
    sns.regplot(x=fitted_vals, y=resids, lowess=True, line_kws={'color': 'red'})
    plt.suptitle('Residus vs Predictions', fontsize=16)
    plt.xlabel('Predictions')
    plt.ylabel('Residus')
    print('\n----Goldfeld-Quandt test ----')
    name = ['F statistic', 'p-value']
    test = sms.het_goldfeldquandt(lm.resid, lm.model.exog)
    print(lzip(name, test))
    print('\n----Residuals plots ----')

homoscedasticity_test(lm)
