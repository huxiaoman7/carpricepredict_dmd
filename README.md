# DMD项目报告——《汽车价格预测及影响因素分析研究》
## 一、项目背景
### （一）简要问题描述
2017年，吉利汽车计划美国市场，当时面临着两个关键问题：
- (1）吉利旗下有众多品牌，选择什么品牌进入美国市场将决定它在美国市场的成败，为了做出正确的决策，吉利汽车在考虑是否请一家汽车咨询公司来帮助自己做出选择。
- (2）吉利汽车管理层希望了解在美国市场上车辆价格如何随着车辆配置变化而变化，从而他们可以相应地修改汽车的设计、制定适合美国市场的商业策略等。
### （二）解决方案
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

| 品牌   | 经济状态 |        |        |
| ------ | -------- | ------ | ------ |
| 增长   | 保持不变 | 下降   |        |
| 沃尔沃 | 40,000   | 20,000 | 10,000 |
| 领克   | 50,000   | 30,000 | 20,000 |
| 吉利   | 80,000   | 50,000 | 30,000 |

吉利汽车考虑与一家汽车咨询公司合作，预测美国明年的经济状态，以决策进入美国市场的主推品牌。咨询公司的预测结论有以下两种：好与差。下表为咨询专家在给定经济状态下得出不同预测结论的概率。咨询费用需要100万美元。

| 预测结论 | 经济状态 |      |      |
| -------- | -------- | ---- | ---- |
| 增长     | 保持不变 | 下降 |      |
| 好       | 0.9      | 0.5  | 0.1  |
| 差       | 0.1      | 0.5  | 0.9  |

首先考虑不与咨询公司合作的情况下，三个品牌的期望销售利润分别是：

- EMV（沃尔沃）=（40,000*40%+20,000*35%+10,000*25%）*1=25,500万美元

- EMV（领克）=（50,000*40%+30,000*35%+20,000*25%）*0.6=24,850万美元

- EMV（吉利）=（80,000*40%+50,000*35%+30,000*25%）*0.3=17,100万美元

其次考虑与咨询公司合作的情况下，决策树各个分叉的概率：

| 预测    | 经济状态                        | 先验概率①                            | 预测准确性②                              | ① * ②                                                    | 后验概率                                    |
| ------- | ------------------------------- | ------------------------------------ | ---------------------------------------- | -------------------------------------------------------- | ------------------------------------------- |
| 好（G） | 增长（U）  不变（S）  下降（D） | P（U）=0.4  P（S）=0.35  P（D）=0.25 | P（G/U）=0.9  P（G/S）=0.5  P（G/D）=0.1 | P（GU）=0.36  P（GS）=0.175  P（GD）=0.025  P（G）=0.56  | P（U/G）=0.64  P（S/G）=0.31  P（D/G）=0.05 |
| 差（W） | 增长（U）  不变（S）  下降（D） | P（U）=0.4  P（S）=0.35  P（D）=0.25 | P（W/U）=0.1  P（W/S）=0.5  P（W/D）=0.9 | P（W U）=0.04  P（WS）=0.175  P（WD）=0.225  P（W）=0.44 | P（U/W）=0.09  P（S/W）=0.40  P（D/W）=0.51 |

最后画出决策树，由决策树结果得知，吉利汽车应该与咨询公司合作，最优决策策略的EMV是26,212万美元。当咨询公司预测结论好时，吉利汽车应主推沃尔沃品牌；当咨询公司预测结论差时，吉利汽车应主推领克品牌。

此处有图片


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

 
## 三、数据分析
## 三、数据分析与建模

### （一）数据清洗


1). 将变量CarName分割成两列：CompanyName和CarModel

```python3
CompanyName = data['CarName'].apply(lambda x : x.split(' ')[0])
data.insert(3,"CompanyName",CompanyName)
data.drop(['CarName'],axis=1,inplace=True)
data.drop(['car_ID'],axis=1,inplace=True)
data.head()
```

输出结果如下：
|      | symboling | CompanyName | fueltype | aspiration | doornumber | carbody     | drivewheel | enginelocation | wheelbase | carlength | carwidth | carheight | curbweight | enginetype | cylindernumber | enginesize | fuelsystem | boreratio | stroke | compressionratio | horsepower | peakrpm | citympg | highwaympg | price   |
| :--- | :-------- | :---------- | :------- | :--------- | :--------- | :---------- | :--------- | :------------- | :-------- | :-------- | :------- | :-------- | :--------- | :--------- | :------------- | :--------- | :--------- | :-------- | :----- | :--------------- | :--------- | :------ | :------ | :--------- | ------- |
| 0    | 3         | alfa-romero | gas      | std        | two        | convertible | rwd        | front          | 88.6      | 168.8     | 64.1     | 48.8      | 2548       | dohc       | four           | 130        | mpfi       | 3.47      | 2.68   | 9.0              | 111        | 5000    | 21      | 27         | 13495.0 |
| 1    | 3         | alfa-romero | gas      | std        | two        | convertible | rwd        | front          | 88.6      | 168.8     | 64.1     | 48.8      | 2548       | dohc       | four           | 130        | mpfi       | 3.47      | 2.68   | 9.0              | 111        | 5000    | 21      | 27         | 16500.0 |
| 2    | 1         | alfa-romero | gas      | std        | two        | hatchback   | rwd        | front          | 94.5      | 171.2     | 65.5     | 52.4      | 2823       | ohcv       | six            | 152        | mpfi       | 2.68      | 3.47   | 9.0              | 154        | 5000    | 19      | 26         | 16500.0 |
| 3    | 2         | audi        | gas      | std        | four       | sedan       | fwd        | front          | 99.8      | 176.6     | 66.2     | 54.3      | 2337       | ohc        | four           | 109        | mpfi       | 3.19      | 3.40   | 10.0             | 102        | 5500    | 24      | 30         | 13950.0 |
| 4    | 2         | audi        | gas      | std        | four       | sedan       | 4wd        | front          | 99.4      | 176.6     | 66.4     | 54.3      | 2824       | ohc        | five           | 136        | mpfi       | 3.19      | 3.40   | 8.0              |            |         |         |            |         |

2). 检查类别变量是否有拼写错误，如有则改成正确名称

```python3
def get_variable_type(element) :
    if element==0:
        return "Not Known"
    elif element < 20 and element!=0 :
        return "Categorical"
    elif element >= 20 and element!=0 :
        return "Contineous"
    
def predict_variable_type(metadata_matrix):
    metadata_matrix["Variable_Type"] = metadata_matrix["Valeurs_Uniques_Count"].apply(get_variable_type).astype(str)
    metadata_matrix["frequency"] = metadata_matrix["Null_Count"] - metadata_matrix["Null_Count"]
    metadata_matrix["frequency"].astype(int)
    return metadata_matrix 

def get_meta_data(dataframe) :
    metadata_matrix = pd.DataFrame({
                    'Datatype' : dataframe.dtypes.astype(str), # types de données de colonnes
                    'Non_Null_Count': dataframe.count(axis = 0).astype(int), # nombre total d'éléments dans les colonnes
                    'Null_Count': dataframe.isnull().sum().astype(int), # total des valeurs nulles dans les colonnes
                    'Null_Percentage': dataframe.isnull().sum()/len(dataframe) * 100, # pourcentage de valeurs nulles
                    'Valeurs_Uniques_Count': dataframe.nunique().astype(int) # nombre de valeurs uniques
                     })
    
    metadata_matrix = predict_variable_type(metadata_matrix)
    return metadata_matrix

def list_potential_categorical_type(dataframe,data) :
    print("*********colonnes de type de données catégoriques potentielles*********")
    metadata_matrix_categorical = dataframe[dataframe["Variable_Type"] == "Categorical"]
    
    length = len(metadata_matrix_categorical)
    if length == 0 :
        print("Aucune colonne catégorique dans un jeu de données donné.")  
    else :    
        metadata_matrix_categorical = metadata_matrix_categorical.filter(["Datatype","Valeurs_Uniques_Count"])
        metadata_matrix_categorical.sort_values(["Valeurs_Uniques_Count"], axis=0,ascending=False, inplace=True)
        col_to_check = metadata_matrix_categorical.index.tolist()
        name_list = []
        values_list = []
        
        for name in col_to_check :
            name_list.append(name)
            values_list.append(data[name].unique())
        
        temp = pd.DataFrame({"index":name_list,"Valeurs_Uniques":values_list})
        metadata_matrix_categorical = metadata_matrix_categorical.reset_index()
        metadata_matrix_categorical = pd.merge(metadata_matrix_categorical,temp,how='inner',on='index')
        print(metadata_matrix_categorical.set_index("index"))
```

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



## 四、项目总结与建议

### （一）项目总结

以上是针对吉利汽车进入美国市场场景开展的分析研究，充分运用《数据、模型与决策》中所学知识，对吉利公司首次进入美国市场所选择的汽车品牌进行了决策，并对其在美国市场的定价及其影响因素进行了分析。

首先考虑是否与咨询公司合作以获得对市场预测和品牌建议的专业咨询报告。运用决策树分析，为获得预期市场利润最大化，吉利汽车应该与咨询公司合作，并且选择沃尔沃作为进入美国市场的品牌，在此最优决策策略下期望在美国市场的利润是26,212万美元。

然后考虑如何对汽车定价以在美国市场中更有竞争力，并分析出影响汽车价格的关键因素。运用回归分析，将车身类型、发动机类型、发动机排量等22项汽车配置数据作为自变量，通过数据清洗、数据建模、逐次回归等一系列数据分析，得出xxxx、xxxxxx、xxxxxx是影响汽车价格的关键因素，其中xxxx对价格起到正向影响，xxx对价格起到负向影响作用。

以上研究分析结果为吉利公司进入美国市场的战略规划提供了辅助依据。

 
### （二）项目建议

本案例可以作为吉利汽车美国市场战略的一般性分析决策使用，但是由于分析是基于汽车配置参数均为固定值的情况，实际生产经营中有可能发生行业技术革新引发配置大幅提升的情况。此外还要考虑在实际市场发展中，需要根据竞品公司的市场战略动态调整策略，以及价格会受到监管部门约束、行业风向等多种外部因素的影响。所以如果遇到上述变化因素的情况，可以引入新的变量以及新的条件来进行相应决策和回归分析。
