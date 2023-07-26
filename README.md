# DMD项目报告——《汽车价格预测及影响因素分析研究》

## 一、项目背景

### （一）简要问题描述

2017年，吉利汽车计划美国市场，当时面临着两个关键问题：

- (1）吉利旗下有众多品牌，选择什么品牌进入美国市场将决定它在美国市场的成败，为了做出正确的决策，吉利汽车在考虑是否请一家汽车咨询公司来帮助自己做出选择。
- (2）吉利汽车管理层希望了解在美国市场上车辆价格如何随着车辆配置变化而变化，从而他们可以相应地修改汽车的设计、制定适合美国市场的商业策略等。

### （二）项目解决方案

本次关于是否请咨询公司的决策，以及汽车价格影响因素的分析研究，涉及到DMD课程所学知识如下： 

- （1）决策树分析
- （2）回归分析

### （三）项目简要分析

**时间（When）：2017年**

**地点（Where）：美国**

**人物（Who）：吉利汽车**，是中国市场销售量第一的国产品牌，旗下有多个品牌，包括吉利汽车、吉利新能源、领克、宝腾、路特斯、极氪，同时还收购了沃尔沃品牌。吉利汽车也是布局海外市场较早的中国品牌之一。

**事件（What）：吉利汽车在考虑是否进入美国市场。**在美国市场吉利汽车需要和日系、美系、欧系车厂直接竞争，因此需要在决定进入美国市场之前对于市场进行全面调研，确定新市场的销售策略和定价策略。具体而言，吉利汽车现在面临两个问题：**1）选择什么品牌进入美国市场？2）有哪些因素决定了美国市场上汽车的定价？**

**原因（Why）**：中国市场竞争非常激烈，不少厂商也看到国内市场呈现相对饱和的态势，“内卷”化的竞争愈演愈烈，甚至时常陷入过度依靠低价的恶性市场竞争。受益于中国汽车产业链韧性较强的优势以及中国品牌竞争力放的不断提升，**吉利汽车希望通过进入美国市场消化转移国内过剩的产能，找到新的增长点**。

**方式（How）**：针对事件**问题（1）**，吉利汽车旗下有多个汽车品牌，目前正在考虑从高中低三个品牌，分别是沃尔沃、领克、吉利，三个品牌中选一个进入美国市场。因为不同档位汽车销量根据经济情况波动不同，直接影响到销售额，所以选择哪一个品牌进入市场就极大依赖于吉利汽车对于美国市场经济形式的判断，而吉利汽车对美国市场并不了解，因此在考虑是否请咨询公司。为了解决吉利汽车这个问题，我们将使用**决策树分析**的方法。

针对事件**问题（2）**，进入一个新的市场，吉利汽车很关心什么汽车配置可以影响到汽车的定价，从而对于汽车配置进行调整，使吉利品牌的车在美国同一个价位的车中更有竞争力。为此，我们了收集205款车的价格和25项数据变量，将使用**回归分析**帮助吉利汽车解决问题。

## 二、数据分析

### （一）问题一：吉利汽车是否需要与咨询公司合作，以决策进入美国市场的主推品牌？

吉利汽车希望进入美国市场，旗下有三大品牌，从高到低依次是：沃尔沃（利润1万美元/辆）、领克（利润0.7万美元/辆）、吉利（利润0.3万美元/辆）。汽车销量取决于美国经济的状态，吉利汽车预测美国下一年的经济状态为：增长（概率为40%）、保持不变（概率为35%）、下降（概率为25%）。每种经济状态下各品牌的销售量为：

| 品牌名称 | 经济增长 | 经济保持不变 | 经济下降 |
| -------- | -------- | ------------ | -------- |
| 沃尔沃   | 40,000   | 20,000       | 10,000   |
| 领克     | 50,000   | 30,000       | 20,000   |
| 吉利     | 80,000   | 50,000       | 30,000   |

吉利汽车考虑与一家汽车咨询公司合作，预测美国明年的经济状态，以决策进入美国市场的主推品牌。咨询公司的预测结论有以下两种：好与差。下表为咨询专家在给定经济状态下得出不同预测结论的概率。咨询费用需要100万美元。

| 预测结论 | 经济增长 | 经济保持不变 | 经济下降 |
| -------- | -------- | ------------ | -------- |
| 好       | 0.9      | 0.5          | 0.1      |
| 差       | 0.1      | 0.5          | 0.9      |

首先考虑不与咨询公司合作的情况下，三个品牌的期望销售利润分别是：

- EMV（沃尔沃）=（40,000×40%+20,000×35%+10,000×25%）×1=25,500万美元

- EMV（领克）=（50,000×40%+30,000×35%+20,000×25%）× 0.6=24,850万美元

- EMV（吉利）=（80,000×40%+50,000×35%+30,000×25%）× 0.3=17,100万美元

其次考虑与咨询公司合作的情况下，决策树各个分叉的概率：

|  预测   |                           经济状态                           |              先验概率①               |                  预测准确性②                   |                            ① × ②                             |                  后验概率                   |
| :-----: | :----------------------------------------------------------: | :----------------------------------: | :--------------------------------------------: | :----------------------------------------------------------: | :-----------------------------------------: |
| 好（G） | 增长(U)                       不变（S）                      下降（D） | P（U）=0.4  P（S）=0.35  P（D）=0.25 | P（G/U）=0.9  P（G/S）=0.5        P（G/D）=0.1 | P（GU）=0.36      P（GS）=0.175      P（GD）=0.025      P（G）=0.56 | P（U/G）=0.64  P（S/G）=0.31  P（D/G）=0.05 |
| 差（W） | 增长（U）                      不变（S）                      下降（D） | P（U）=0.4  P（S）=0.35  P（D）=0.25 |    P（W/U）=0.1  P（W/S）=0.5  P（W/D）=0.9    |   P（W U）=0.04  P（WS）=0.175  P（WD）=0.225  P（W）=0.44   | P（U/W）=0.09  P（S/W）=0.40  P（D/W）=0.51 |

最后画出决策树，由决策树结果得知，吉利汽车应该与咨询公司合作，最优决策策略的EMV是26,212万美元。当咨询公司预测结论好时，吉利汽车应主推沃尔沃品牌；当咨询公司预测结论差时，吉利汽车应主推领克品牌。

![image-20230726223335493](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230726223335493.png)


### （二）问题二：有哪些因素决定了美国市场上汽车的定价？

#### 1.自变量/因变量说明

#####  自变量：

| **变量名**       | **变量类型** | **取值范围**                                   | **含义描述**                                                 |
| ---------------- | ------------ | ---------------------------------------------- | ------------------------------------------------------------ |
| car_ID           | 整数型       | 1~205                                          | 样本号                                                       |
| symboling        | 整数型       | -3,  -2, -1, 0, 1, 2, 3.                       | 分类标记系统（评估车辆风险和安全性，3表示高风险，-3表示低风险) |
| CarName          | 分类变量     | alfa-romero, audi, etc                         | 汽车品牌                                                     |
| fueltype         | 分类变量     | diesel, gas                                    | 燃料类型                                                     |
| aspiration       | 分类变量     | std,  turbo                                    | 进气方式 （标准进气，涡轮增压）                              |
| doornumber       | 分类变量     | four, two                                      | 车门数量                                                     |
| carbody          | 分类变量     | hardtop, wagon, sedan, hatchback,  convertible | 车身类型 （旅行车、轿车等）                                  |
| drivewheel       | 分类变量     | 4wd, fwd, rwd                                  | 驱动方式 （四轮驱动，前轮驱动等）                            |
| enginelocation   | 分类变量     | front, rear                                    | 发动机位置                                                   |
| wheelbase        | 连续数值型   | 86.6~ 120.9                                    | 轴距                                                         |
| carlength        | 连续数值型   | 141.1~ 208.1                                   | 车长                                                         |
| carwidth         | 连续数值型   | 60.3~72.3                                      | 车宽                                                         |
| carheight        | 连续数值型   | 47.8 ~ 59.8                                    | 车高                                                         |
| curbweight       | 连续数值型   | 1488 ~ 4066                                    | 整备质量                                                     |
| enginetype       | 分类变量     | dohc, dohcv, l, ohc, ohcf, ohcv, rotor         | 发动机类型 （双顶置凸轮轴等）                                |
| cylindernumber   | 分类变量     | eight, five, four, six, three, etc.            | 缸数                                                         |
| enginesize       | 连续数值型   | 61 ~ 326                                       | 发动机排量                                                   |
| fuelsystem       | 分类变量     | 1bbl, 2bbl, 4bbl, idi, mfi, mpfi etc           | 燃油系统 (单体化油器，多点燃油喷射等)                        |
| boreratio        | 连续数值型   | 2.54 ~ 3.94                                    | 缸径比                                                       |
| stroke           | 连续数值型   | 2.07 ~ 4.17                                    | 冲程                                                         |
| compressionratio | 连续数值型   | 7 ~ 23                                         | 压缩比                                                       |
| horsepower       | 连续数值型   | 48 ~ 288                                       | 马力                                                         |
| peakrpm          | 连续数值型   | 4150 ~ 6600                                    | 最大转速                                                     |
| citympg          | 连续数值型   | 13 ~ 49                                        | 城市道路燃油经济性（每加仑英里数）                           |
| highwaympg       | 连续数值型   | 16 ~ 54                                        | 高速公路燃油经济性（每加仑英里数）                           |

##### 因变量：

| **变量名** | **变量类型** | **取值范围** | **含义描述** |
| ---------- | ------------ | ------------ | ------------ |
| price      | 连续数值型   | 5118 ~ 45400 | 价格         |


## 三、数据分析与建模

### （一）数据清洗

1). 将变量CarName分割成两列：CompanyName和CarModel,并检查类别变量是否有拼写错误:详见[dataetl.py](https://github.com/huxiaoman7/carpricepredict_dmd/blob/main/README.md)

调用预处理函数：

```python3
metadata = get_meta_data(data)
list_potential_categorical_type(metadata,data)
```

处理后数据如下：

```shell
*********colonnes de type de données catégoriques potentielles*********
               Datatype Valeurs_Uniques_Count  Valeurs_Uniques
index
fuelsystem       object                     8  [mpfi, 2bbl, mfi, 1bbl, spfi, 4bbl, idi, spdi]
enginetype       object                     7  [dohc, ohcv, ohc, l, rotor, ohcf, dohcv]
cylindernumber   object                     7  [four, six, five, three, twelve, two, eight]
symboling         int64                     6  [3, 1, 2, 0, -1, -2]
carbody          object                     5  [convertible, hatchback, sedan, wagon, hardtop]
drivewheel       object                     3  [rwd, fwd, 4wd]
fueltype         object                     2  [gas, diesel]
aspiration       object                     2  [std, turbo]
doornumber       object                     2  [two, four]
enginelocation   object                     2   [front, rear]
```

处理CompanyName变量，首先检测变量中是否有重复字符：

```python3
data.CompanyName.unique()
```

输出结果：

```shell
array(['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda',
       'isuzu', 'jaguar', 'maxda', 'mazda', 'buick', 'mercury',
       'mitsubishi', 'Nissan', 'nissan', 'peugeot', 'plymouth', 'porsche',
       'porcshce', 'renault', 'saab', 'subaru', 'toyota', 'toyouta',
       'vokswagen', 'volkswagen', 'vw', 'volvo'], dtype=object)
```

分析输出结果发现部分公司名称应该相同，但拼写错误，比如：

```shell
'maxda' and 'mazda' ================> mazda
'porsche' and 'porcshce' ===========> porsche
'toyota' and 'toyouta' =============> toyota
'vokswagen' and 'volkswagen','vw' ==> volkswagen
'Nissan' and 'nissan' ==============> nissan
```

因此将错误名称更改为正确的公司名称：

```python3
data = data.replace(to_replace ="maxda", value ="mazda") 
data = data.replace(to_replace ="porcshce", value ="porsche") 
data = data.replace(to_replace ="toyouta", value ="toyota") 
data = data.replace(to_replace ="vokswagen", value ="volkswagen") 
data = data.replace(to_replace ="vw", value ="volkswagen")
data = data.replace(to_replace ="Nissan", value ="nissan")
data.CompanyName.unique()
```

输出结果：

```shell
array(['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda',
       'isuzu', 'jaguar', 'mazda', 'buick', 'mercury', 'mitsubishi',
       'nissan', 'peugeot', 'plymouth', 'porsche', 'renault', 'saab',
       'subaru', 'toyota', 'volkswagen', 'volvo'], dtype=object)
```

### （二）数据分析

由于因变量Price是连续数值变量，有多个自变量，因此我们采取多元线性回归模型，首先要满足以下假设：

a.因变量Y(即价格)与自变量X具有线性关系，必须确保XY的散点图是线性的。

b.多元回归方程中的各个自变量X之间不存在多重共线性。为了检验这一点，将会采用VIF（方差膨胀系数）或者相关系数矩阵来检验。

建立回归方程后，将会检测三点来验证模型的有效性：a.误差分布的正态性 b.误差的独立性 c.同方差性

#### 1）分析因变量Price：

```python3
plt.title('Car Price Spread')
sns.boxplot(y=data.price)
plt.show()
print(data.price.describe())
plt.title('Car Price Distribution Plot')
sns.distplot(data.price)
plt.show()
print(data.price.describe())
```

输出结果：
![image-20230723220653992](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723220653992.png)

```shell
count      205.000000
mean     13276.710571
std       7988.852332
min       5118.000000
25%       7788.000000
50%      10295.000000
75%      16503.000000
max      45400.000000
Name: price, dtype: float64
```

数据显示，Price的平均值约为13K，中位数约为10k，最贵的车值为45k，最便宜的车值为5k。 由于均值>中位数，因此数据分布是非对称的，直方图中可观察到，吉利公司提供的价格大部分都很低，其中75%的价格在16k左右，25%的价格在17k - 45k这个范围区间内。

#### 2）分析自变量

- a. 检测因变量Price和数值型自变量的线性关系，详见：详见[analysis.py](https://github.com/huxiaoman7/carpricepredict_dmd/blob/main/README.md)

**Price VS Wheelbase - curbweight - boreratio**
![image-20230723221312116](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723221312116.png)

```shell
Coefficient of Correlation between Price and wheelbase: 57.781559829215 %
Correlation coefficient between Price and curbweight: 83.53048793372966 %
Correlation coefficient between Price and boreratio:  55.31732367984436 %
```

同理，可分析

**Price VS carlength - carwidth - carheight**

![image-20230723221507877](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723221507877.png)

```shell
Correlation coefficient between Price and carlength: 68.2920015677962 %
Correlation coefficient between Price and carwidth:  75.93252997415114 %
Correlation coefficient between Price and carheight:  11.933622657049444 %
```

**Price VS enginesize - horsepower - stroke**
![image-20230723221558874](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723221558874.png)

```shell
Correlation coefficient between Price and enginesize:  87.41448025245117 %
Correlation coefficient between Price and horsepower:  80.81388225362217 %
Correlation coefficient between Price and stroke:  7.944308388193101 %
```


**Price VS compressionratio - peakrpm - symboling**

![image-20230723221711929](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723221711929.png)

```shell
Correlation coefficient between Price and compressionratio:  6.798350579944266 %
Correlation coefficient between Price and peakrpm:  -8.526715027785684 %
Correlation coefficient between Price and symboling:  -7.997822464270351 %
```

**Price VS citympg - highwaympg**

![image-20230723221907538](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723221907538.png)

```shell
Correlation coefficient between Price and citympg:  -68.57513360270397 %
Correlation coefficient between Price and highwaympg:  -69.75990916465565 %
```

由数据可得出结论：

i.与价格Price正相关的自变量:**wheelbase, carlenght, carwidth, curbweight, enginesize, boreratio, horesepower** 

ii.与价格Price负相关的自变量: **citympg, highwaympg**

这些变量可以保留用于构建模型，其他与价格Price不相关的自变量可忽略

- b).检验上述相关自变量与价格Price之间是否具有高相关性：详见correlation.py，运行后相关系数矩阵热力图如下：

![image-20230723222625500](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723222625500.png)

i. 检查与汽车尺寸相关的变量之间的相关性，如**weight, height** 等

```python
def heatmap1(x,y,dimention,dataframe):
	plt.figure(figsize=(x,y))
	n_variables = dimention
	pc = dataframe[dimention].corr(method='pearson')
	cols= dimention
	sns.heatmap(pc,annot=True,yticklabels=cols,xticklabels=cols,annot_kws={'size':10},cmap='coolwarm')
	plt.show()

heatmap1(10,10,dimension_col_list,data.filter(dimension_col_list))
```

输出相关系数矩阵：

![image-20230723233436116](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723233436116.png)

**Wheelbase** , **carlength**, **carwidth**和**curbweight** 的相关系数非常相近，因此我们仅需保留其中一个自变量即可。

同理，可以检测汽车性能自变量（**Horsepower** 、**boreratio**、**enginesize** ），每加仑燃料所行英里数mpg（**citympg**、**highwaympg**）的相关系数，运行代码后如图所示：

![image-20230723234734659](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230723234734659.png)

根据相关系数矩阵数据分析，删除相关性高的变量中的一个，保留与价格相关性更高的变量，其中高于0.85的为高相关性，因此删除的变量有**wheelbase**、**carlength**、**carweight**、**citympg**

删除相关性高的自变量：

```python3
data = data.drop(['carheight' ,'stroke' ,'compressionratio' ,'peakrpm' ,'carlength' ,'carwidth' ,'curbweight' ,'enginesize' ,'highwaympg'], axis=1)
data.head()
```

输出结果：

|      | symboling | CompanyName | fueltype | aspiration | doornumber | carbody     | drivewheel | enginelocation | wheelbase | enginetype | cylindernumber | fuelsystem | boreratio | horsepower | citympg | price   |
| :--- | :-------- | :---------- | :------- | :--------- | :--------- | :---------- | :--------- | :------------- | :-------- | :--------- | :------------- | :--------- | :-------- | :--------- | :------ | ------- |
| 0    | 3         | alfa-romero | gas      | std        | two        | convertible | rwd        | front          | 88.6      | dohc       | four           | mpfi       | 3.47      | 111        | 21      | 13495.0 |
| 1    | 3         | alfa-romero | gas      | std        | two        | convertible | rwd        | front          | 88.6      | dohc       | four           | mpfi       | 3.47      | 111        | 21      | 16500.0 |
| 2    | 1         | alfa-romero | gas      | std        | two        | hatchback   | rwd        | front          | 94.5      | ohcv       | six            | mpfi       | 2.68      | 154        | 19      | 16500.0 |
| 3    | 2         | audi        | gas      | std        | four       | sedan       | fwd        | front          | 99.8      | ohc        | four           | mpfi       | 3.19      | 102        | 24      | 13950.0 |
| 4    | 2         | audi        | gas      | std        | four       | sedan       | 4wd        | front          | 99.4      | ohc        | five           |            |           |            |         |         |

### （三）数据准备

#### 1） 创造dummy 变量

由于部分自变量的值为字符串，为了能够成功拟合回归线，需要将字符串转换为数值格式，可以使用哑变量将它们转换为1和0。如：

```shell
fueltype {" gas ": 1, " diesel ": 0}
suction {" std ": 1, " turbo ": 0}
doornumber {" two ": 1, " oven ": 0}
enginelocation {" front ": 1, " rear ": 0}
```

执行dummy.py代码，输出结果得到新数据，均为数值变量：

|      | wheelbase | boreratio | horsepower | citympg | price   | symboling_-1 | symboling_0 | symboling_1 | symboling_2 | symboling_3 | CompanyName_audi | CompanyName_bmw | CompanyName_buick | CompanyName_chevrolet | CompanyName_dodge | CompanyName_honda | CompanyName_isuzu | CompanyName_jaguar | CompanyName_mazda | CompanyName_mercury | CompanyName_mitsubishi | CompanyName_nissan | CompanyName_peugeot | CompanyName_plymouth | CompanyName_porsche | CompanyName_renault | CompanyName_saab | CompanyName_subaru | CompanyName_toyota | CompanyName_volkswagen | CompanyName_volvo | fueltype_gas | aspiration_turbo | doornumber_two | carbody_hardtop | carbody_hatchback | carbody_sedan | carbody_wagon | drivewheel_fwd | drivewheel_rwd | enginelocation_rear | enginetype_dohcv | enginetype_l | enginetype_ohc | enginetype_ohcf | enginetype_ohcv | enginetype_rotor | cylindernumber_five | cylindernumber_four | cylindernumber_six | cylindernumber_three | cylindernumber_twelve | cylindernumber_two | fuelsystem_2bbl | fuelsystem_4bbl | fuelsystem_idi | fuelsystem_mfi | fuelsystem_mpfi | fuelsystem_spdi | fuelsystem_spfi |
| :--- | :-------- | :-------- | :--------- | :------ | :------ | :----------- | :---------- | :---------- | :---------- | :---------- | :--------------- | :-------------- | :---------------- | :-------------------- | :---------------- | :---------------- | :---------------- | :----------------- | :---------------- | :------------------ | :--------------------- | :----------------- | :------------------ | :------------------- | :------------------ | :------------------ | :--------------- | :----------------- | :----------------- | :--------------------- | :---------------- | :----------- | :--------------- | :------------- | :-------------- | :---------------- | :------------ | :------------ | :------------- | :------------- | :------------------ | :--------------- | :----------- | :------------- | :-------------- | :-------------- | :--------------- | :------------------ | :------------------ | :----------------- | :------------------- | :-------------------- | :----------------- | :-------------- | :-------------- | :------------- | :------------- | :-------------- | :-------------- | --------------- |
| 0    | 88.6      | 3.47      | 111        | 21      | 13495.0 | 0            | 0           | 0           | 0           | 1           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 1              | 0               | 0                 | 0             | 0             | 0              | 1              | 0                   | 0                | 0            | 0              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 0               | 0               | 0              | 0              | 1               | 0               | 0               |
| 1    | 88.6      | 3.47      | 111        | 21      | 16500.0 | 0            | 0           | 0           | 0           | 1           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 1              | 0               | 0                 | 0             | 0             | 0              | 1              | 0                   | 0                | 0            | 0              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 0               | 0               | 0              | 0              | 1               | 0               | 0               |
| 2    | 94.5      | 2.68      | 154        | 19      | 16500.0 | 0            | 0           | 1           | 0           | 0           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 1              | 0               | 1                 | 0             | 0             | 0              | 1              | 0                   | 0                | 0            | 0              | 0               | 1               | 0                | 0                   | 0                   | 1                  | 0                    | 0                     | 0                  | 0               | 0               | 0              | 0              | 1               | 0               | 0               |
| 3    | 99.8      | 3.19      | 102        | 24      | 13950.0 | 0            | 0           | 0           | 1           | 0           | 1                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 0              | 0               | 0                 | 1             | 0             | 1              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 0               | 0               | 0              | 0              | 1               | 0               | 0               |
| 4    | 99.4      | 3.19      | 115        | 18      | 17450.0 | 0            | 0           | 0           | 1           | 0           | 1                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 0              | 0               | 0                 | 1             | 0             | 0              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 1                   | 0                   | 0                  | 0                    | 0                     | 0                  | 0               | 0               | 0              | 0              | 1               | 0               | 0               |

#### 2）划分训练集和测试机

i.将67%的数据用于训练，33%的数据用于测试进行划分：

```python3
from sklearn.model_selection import train_test_split
cars_train, cars_test= train_test_split(data, train_size=0.67, test_size=0.33, random_state = 0)
```

ii.特征归一化

```python
from sklearn.preprocessing import StandardScaler,scale
sc = StandardScaler() 

col_to_scale = ['wheelbase','boreratio','horsepower','citympg','price',]

cars_train[col_to_scale] = sc.fit_transform(cars_train[col_to_scale])
cars_test[col_to_scale] = sc.fit_transform(cars_test[col_to_scale])

cars_train.head()
```

输出结果：

|      | wheelbase | boreratio | horsepower | citympg  | price     | symboling_-1 | symboling_0 | symboling_1 | symboling_2 | symboling_3 | CompanyName_audi | CompanyName_bmw | CompanyName_buick | CompanyName_chevrolet | CompanyName_dodge | CompanyName_honda | CompanyName_isuzu | CompanyName_jaguar | CompanyName_mazda | CompanyName_mercury | CompanyName_mitsubishi | CompanyName_nissan | CompanyName_peugeot | CompanyName_plymouth | CompanyName_porsche | CompanyName_renault | CompanyName_saab | CompanyName_subaru | CompanyName_toyota | CompanyName_volkswagen | CompanyName_volvo | fueltype_gas | aspiration_turbo | doornumber_two | carbody_hardtop | carbody_hatchback | carbody_sedan | carbody_wagon | drivewheel_fwd | drivewheel_rwd | enginelocation_rear | enginetype_dohcv | enginetype_l | enginetype_ohc | enginetype_ohcf | enginetype_ohcv | enginetype_rotor | cylindernumber_five | cylindernumber_four | cylindernumber_six | cylindernumber_three | cylindernumber_twelve | cylindernumber_two | fuelsystem_2bbl | fuelsystem_4bbl | fuelsystem_idi | fuelsystem_mfi | fuelsystem_mpfi | fuelsystem_spdi | fuelsystem_spfi |
| :--- | :-------- | :-------- | :--------- | :------- | :-------- | :----------- | :---------- | :---------- | :---------- | :---------- | :--------------- | :-------------- | :---------------- | :-------------------- | :---------------- | :---------------- | :---------------- | :----------------- | :---------------- | :------------------ | :--------------------- | :----------------- | :------------------ | :------------------- | :------------------ | :------------------ | :--------------- | :----------------- | :----------------- | :--------------------- | :---------------- | :----------- | :--------------- | :------------- | :-------------- | :---------------- | :------------ | :------------ | :------------- | :------------- | :------------------ | :--------------- | :----------- | :------------- | :-------------- | :-------------- | :--------------- | :------------------ | :------------------ | :----------------- | :------------------- | :-------------------- | :----------------- | :-------------- | :-------------- | :------------- | :------------- | :-------------- | :-------------- | --------------- |
| 155  | -0.534054 | -1.097737 | -1.103524  | 0.333598 | -0.583062 | 0            | 1           | 0           | 0           | 0           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 1                  | 0                      | 0                 | 1            | 0                | 0              | 0               | 0                 | 0             | 1             | 0              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 1               | 0               | 0              | 0              | 0               | 0               | 0               |
| 97   | -0.723234 | -0.725116 | -0.921031  | 1.008180 | -0.680192 | 0            | 0           | 1           | 0           | 0           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 1                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 0              | 0               | 0                 | 0             | 1             | 1              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 1               | 0               | 0              | 0              | 0               | 0               | 0               |
| 54   | -0.943944 | -0.985950 | -0.947101  | 1.008180 | -0.755502 | 0            | 0           | 1           | 0           | 0           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 1                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 0              | 0               | 0                 | 1             | 0             | 1              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 1               | 0               | 0              | 0              | 0               | 0               | 0               |
| 184  | -0.281814 | -1.246785 | -1.364229  | 2.020054 | -0.680691 | 0            | 0           | 0           | 1           | 0           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 0                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 1                      | 0                 | 0            | 0                | 0              | 0               | 0                 | 1             | 0             | 1              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 0               | 0               | 1              | 0              | 0               | 0               | 0               |
| 51   | -0.943944 | -1.172261 | -0.947101  | 1.008180 | -0.917592 | 0            | 0           | 1           | 0           | 0           | 0                | 0               | 0                 | 0                     | 0                 | 0                 | 0                 | 0                  | 1                 | 0                   | 0                      | 0                  | 0                   | 0                    | 0                   | 0                   | 0                | 0                  | 0                  | 0                      | 0                 | 1            | 0                | 1              | 0               | 1                 | 0             | 0             | 1              | 0              | 0                   | 0                | 0            | 1              | 0               | 0               | 0                | 0                   | 1                   | 0                  | 0                    | 0                     | 0                  | 1               | 0               | 0              | 0              | 0               | 0               | 0               |

数据集准备：

```python3
y_train = cars_train.loc[:,cars_train.columns == 'price']
X_train = cars_train.loc[:, cars_train.columns != 'price']

y_test = cars_test.loc[:,cars_test.columns == 'price']
X_test = cars_test.loc[:, cars_test.columns != 'price']
```



### （四）构建模型

```python
model = LinearRegression()
model.fit(x_train,y_train)
result = sm.OLS(y_train,x_train).fit()
result.summary()
```

输出结果：

```shell
 OLS Regression Results
==============================================================================
Dep. Variable:                  price   R-squared:                       0.971
Model:                            OLS   Adj. R-squared:                  0.951
Method:                 Least Squares   F-statistic:                     50.29
Date:                Mon, 24 Jul 2023   Prob (F-statistic):           1.79e-45
Time:                        00:42:21   Log-Likelihood:                 47.394
No. Observations:                 137   AIC:                             15.21
Df Residuals:                      82   BIC:                             175.8
Df Model:                          54
Covariance Type:            nonrobust
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
wheelbase       0.2190      0.068      3.237      0.002       0.084       0.354
boreratio       0.0297      0.071      0.417      0.678      -0.112       0.171
horsepower      0.3052      0.101      3.037      0.003       0.105       0.505
citympg        -0.0443      0.072     -0.614      0.541      -0.188       0.099
···省略完整输出结果···
mfi             0.1241      0.356      0.349      0.728      -0.583       0.832
mpfi            0.1690      0.213      0.795      0.429      -0.254       0.592
spdi            0.0672      0.256      0.262      0.794      -0.443       0.577
spfi            0.6605      0.386      1.710      0.091      -0.108       1.429
==============================================================================
Omnibus:                       11.674   Durbin-Watson:                   1.881
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               17.756
Skew:                           0.433   Prob(JB):                     0.000139
Kurtosis:                       4.537   Cond. No.                     1.49e+16
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 2.4e-30. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
"""
```

由运行结果可得，R²的值为0.971说明模型效果不错。



### （五）模型分析与检验

#### 1）残差分析:

- i.检验残差是否符合正态分布，运行residualanalysis.py,输出结果：

![image-20230724005652641](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230724005652641.png)

结果分析：计算得出的残差值基本均匀分布在0周围，只有少数一些离群值

- ii.残差的独立性检验，运行residualanalysis.py,输出结果：



![image-20230724010423137](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230724010423137.png)

- iii.同方差性检验

对于自变量的值，残差的方差必须是相似的。我们可以通过绘制残差与预测值的拟合曲线来验证。若是同方差，点的位置应该是随机的，不应该有趋势性，图中的红色回归线应该尽可能平坦，而不会呈现拱形。

如果P-value <= 0.05 ==>说明残差不符合同方差性，若P-Value> 0.05 ==> 说明残差为同方差性，运行residualanalysis.py，输出结果：

```shell
----Goldfeld-Quandt test ----
[('F statistic', 1.878640320632787), ('p-value', 0.07034410207973114)]
```

![image-20230724011212791](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230724011212791.png)

由于P-Value>0.05，因此残差符合同方差性。经过三项检验后，均已通过检验认证，说明模型有效。

最后用预测值验证拟合效果：

```python
fig = plt.figure(figsize=(11,5))
plt.scatter(y_test,y_pred)
plt.xlabel('y_test', fontsize=18)
plt.ylabel('y_pred', fontsize=16)

f = lambda x: x

x = np.array(y_test)

plt.plot(x,f(x),lw=2.5, c="orange")
```

输出结果：

![image-20230724011603448](/Users/huxiaoman/Library/Application Support/typora-user-images/image-20230724011603448.png)

检验一下预测值的R^2：

```python
from sklearn.metrics import r2_score 
r2_score(y_test, y_pred)
```

输出结果：

```shell
0.8611118434205732
```

打印完整你和结果：

```shell
OLS Regression Results
==============================================================================
Dep. Variable:                  price   R-squared:                       0.971
Model:                            OLS   Adj. R-squared:                  0.951
Method:                 Least Squares   F-statistic:                     50.29
Date:                Mon, 24 Jul 2023   Prob (F-statistic):           1.79e-45
Time:                        01:20:41   Log-Likelihood:                 47.394
No. Observations:                 137   AIC:                             15.21
Df Residuals:                      82   BIC:                             175.8
Df Model:                          54
Covariance Type:            nonrobust
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
wheelbase       0.2190      0.068      3.237      0.002       0.084       0.354
boreratio       0.0297      0.071      0.417      0.678      -0.112       0.171
horsepower      0.3052      0.101      3.037      0.003       0.105       0.505
citympg        -0.0443      0.072     -0.614      0.541      -0.188       0.099
···省略完整输出结果
mfi             0.1241      0.356      0.349      0.728      -0.583       0.832
mpfi            0.1690      0.213      0.795      0.429      -0.254       0.592
spdi            0.0672      0.256      0.262      0.794      -0.443       0.577
spfi            0.6605      0.386      1.710      0.091      -0.108       1.429
==============================================================================
Omnibus:                       11.674   Durbin-Watson:                   1.881
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               17.756
Skew:                           0.433   Prob(JB):                     0.000139
Kurtosis:                       4.537   Cond. No.                     1.49e+16
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 2.4e-30. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
```

我们可以发现Notes[2]中表示，该模型违反多重共线性假设，自变量之间存在着本应该删除的相关变量,因此我们可以对模型进行改进，采用RFE模型（Recursive Feature Elimination）



### （五）模型优化

由模型的输出结果来看，部分自变量的P-value大于0.05，因此这些自变量无法通过显著性检验，建议删除后再构建模型，因此我们尝试使用新模型RFE（Recursive Feature Elimination），并且通过统计检验选择合适的自变量来构建模型。运行modeloptimize.py,得

```shell
                           OLS Regression Results
==============================================================================
Dep. Variable:                  price   R-squared:                       0.877
Model:                            OLS   Adj. R-squared:                  0.869
Method:                 Least Squares   F-statistic:                     114.2
Date:                Wed, 26 Jul 2023   Prob (F-statistic):           1.75e-54
Time:                        21:22:33   Log-Likelihood:                -50.790
No. Observations:                 137   AIC:                             119.6
Df Residuals:                     128   BIC:                             145.9
Df Model:                           8
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1786      0.036     -5.017      0.000      -0.249      -0.108
horsepower     0.5382      0.041     13.235      0.000       0.458       0.619
bmw            1.1231      0.157      7.143      0.000       0.812       1.434
buick          2.0168      0.160     12.590      0.000       1.700       2.334
jaguar         1.4072      0.241      5.839      0.000       0.930       1.884
porsche        0.5133      0.213      2.405      0.018       0.091       0.936
subaru        -0.4947      0.112     -4.430      0.000      -0.716      -0.274
hardtop       -0.3326      0.176     -1.891      0.061      -0.681       0.015
rear           0.8189      0.147      5.572      0.000       0.528       1.110
ohcf           0.3242      0.085      3.797      0.000       0.155       0.493
==============================================================================
Omnibus:                       25.676   Durbin-Watson:                   1.978
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               35.312
Skew:                           1.014   Prob(JB):                     2.15e-08
Kurtosis:                       4.439   Cond. No.                     2.65e+16
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is  2e-31. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
```



| Features   | VIF      |
| ---------- | -------- |
| porcshe    | inf      |
| subaru     | inf      |
| rear       | inf      |
| ohcf       | inf      |
| horsepower | 1.640000 |
| hardtop    | 1.390000 |
| jaguar     | 1.250000 |
| buick      | 1.100000 |
| bmw        | 1.040000 |

由图中我们可以看到，自变量hardtop的p-value大于0.05，因此需删除该自变量，删除后再检测模型运行效果:

```python
X_train_rfe = X_train_rfe.drop(["hardtop"], axis = 1)
X_train_rfe.head()
lm = statsmodel_summary(y_train,X_train_rfe)
```

运行结果为：

```shell
                            OLS Regression Results
==============================================================================
Dep. Variable:                  price   R-squared:                       0.874
Model:                            OLS   Adj. R-squared:                  0.867
Method:                 Least Squares   F-statistic:                     127.4
Date:                Wed, 26 Jul 2023   Prob (F-statistic):           8.59e-55
Time:                        22:56:28   Log-Likelihood:                -52.677
No. Observations:                 137   AIC:                             121.4
Df Residuals:                     129   BIC:                             144.7
Df Model:                           7
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1874      0.036     -5.260      0.000      -0.258      -0.117
horsepower     0.5388      0.041     13.119      0.000       0.458       0.620
bmw            1.1315      0.159      7.129      0.000       0.817       1.446
buick          1.9697      0.160     12.325      0.000       1.654       2.286
jaguar         1.4145      0.243      5.813      0.000       0.933       1.896
porsche        0.5348      0.215      2.484      0.014       0.109       0.961
subaru        -0.4283      0.107     -4.000      0.000      -0.640      -0.216
rear           0.6955      0.133      5.230      0.000       0.432       0.959
ohcf           0.2671      0.081      3.311      0.001       0.108       0.427
==============================================================================
Omnibus:                       24.715   Durbin-Watson:                   1.930
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               33.213
Skew:                           0.996   Prob(JB):                     6.14e-08
Kurtosis:                       4.361   Cond. No.                     2.64e+16
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is  2e-31. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
```

| Features   | VIF      |
| ---------- | -------- |
| subaru     | inf      |
| rear       | inf      |
| ohcf       | inf      |
| porsche    | 3.000000 |
| horsepower | 1.640000 |
| jaguar     | 1.250000 |
| buick      | 1.060000 |
| bmw        | 1.040000 |

由数据可得，所有自变量的p-value均小于0.05，但subaru、rear、和ohcf的VIF>10,故需删除这三个自变量后再运行模型，结果如下:

```shell
 OLS Regression Results
==============================================================================
Dep. Variable:                  price   R-squared:                       0.864
Model:                            OLS   Adj. R-squared:                  0.859
Method:                 Least Squares   F-statistic:                     166.6
Date:                Wed, 26 Jul 2023   Prob (F-statistic):           5.57e-55
Time:                        23:02:46   Log-Likelihood:                -57.681
No. Observations:                 137   AIC:                             127.4
Df Residuals:                     131   BIC:                             144.9
Df Model:                           5
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1807      0.035     -5.121      0.000      -0.250      -0.111
horsepower     0.5809      0.040     14.546      0.000       0.502       0.660
bmw            1.0915      0.163      6.715      0.000       0.770       1.413
buick          1.9255      0.164     11.773      0.000       1.602       2.249
jaguar         1.2976      0.247      5.247      0.000       0.808       1.787
porsche        1.3780      0.292      4.715      0.000       0.800       1.956
==============================================================================
Omnibus:                       22.035   Durbin-Watson:                   1.982
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               27.711
Skew:                           0.947   Prob(JB):                     9.61e-07
Kurtosis:                       4.126   Cond. No.                         9.59
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

| Features   | VIF      |
| ---------- | -------- |
| horsepower | 1.460000 |
| jaguar     | 1.220000 |
| porsche    | 1.150000 |
| buick      | 1.050000 |
| bmw        | 1.040000 |

由数据可得，所有自变量的p-value均小于0.05，并且VIF均小于5，输出结果Notes中未提示自变量中存在多重共线性问题，因此通过显著性检验的自变量有五个，分别为horsepower（马力）、bmw（宝马）、buick（别克）、jaguar（捷豹）、porsche（保时捷）。

最终预测模型的多元线性回归模型方程为Price=0.5809 × horsepower + 1.0915 × bmw +1.9255 × buick + 1.2976 × jaguar + 1.3780 × porsche +误差e



## 四、项目总结与建议

### （一）项目总结

以上是针对吉利汽车进入美国市场场景开展的分析研究，充分运用《数据、模型与决策》中所学知识，对吉利公司首次进入美国市场所选择的汽车品牌进行了决策，并对其在美国市场的定价及其影响因素进行了分析。

首先考虑是否与咨询公司合作以获得对市场预测和品牌建议的专业咨询报告。运用决策树分析，为获得预期市场利润最大化，吉利汽车应该与咨询公司合作，并且选择沃尔沃作为进入美国市场的品牌，在此最优决策策略下期望在美国市场的利润是26,212万美元。

然后考虑如何对汽车定价以在美国市场中更有竞争力，并分析出影响汽车价格的关键因素。运用回归分析，将车身类型、发动机类型、发动机排量等22项汽车配置数据作为自变量，通过数据清洗、数据建模、逐次回归等一系列数据分析，得出horsepower（马力）、bmw（宝马）、buick（别克）、jaguar（捷豹）、porsche（保时捷）等5个自变量是影响汽车价格的关键因素，均对价格起到正向影响。尽管初始模型运行后计算的R^2为0.971，模型优化后的R^2下降为0.864，但自变量个数从59个下降为5个，拟合度更好，说明我们在分析问题时应该及时检验模型是否能通过显著性检验，来判断自变量是否存在多重共线性等问题，再来删除无关变量。以上研究分析结果为吉利公司进入美国市场的战略规划提供了辅助依据，为拓展美国市场奠定了基石。


### （二）项目建议

本案例可以作为吉利汽车美国市场战略的一般性分析决策使用，但是由于分析是基于汽车配置参数均为固定值的情况，实际生产经营中有可能发生行业技术革新引发配置大幅提升的情况。此外还要考虑在实际市场发展中，需要根据竞品公司的市场战略动态调整策略，以及价格会受到监管部门约束、行业风向等多种外部因素的影响。所以如果遇到上述变化因素的情况，可以引入新的变量以及新的条件来进行相应决策和回归分析。
