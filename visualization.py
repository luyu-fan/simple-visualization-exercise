from matplotlib.pyplot import figure
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# museum_data = pd.read_csv("./datasets/museum_visitors.csv",index_col="Date",parse_dates = True)
# print(museum_data.head())
# print(museum_data.describe())

# # lines
# fig = plt.figure(figsize = (18,8),dpi = 200)
# sns.lineplot(data = museum_data)
# plt.title("Number of visitors")
# plt.xlabel("Date")
# plt.show()

# bars
# ign_data = pd.read_csv("./datasets/ign_scores.csv",index_col="Platform")
# fig = plt.figure(figsize = (18,8),dpi = 200)
# # 只能画一组条形图
# sns.barplot(x = ign_data.index,y = ign_data["Racing"],label = "Racing")
# plt.title("Racing Score")
# plt.xlabel("Platform")
# plt.show()
# # heatmap
# fig = plt.figure(figsize = (18,8),dpi = 120)
# sns.heatmap(data = ign_data,annot = True)
# plt.title("Racing Score")
# plt.xlabel("Platform")
# plt.show()


candy_data = pd.read_csv("./datasets/candy.csv",index_col="id")
print(candy_data.head())

# # scatter
# plt.figure(figsize=(10,10),dpi =120)
# # hue 表示不同的组别，不同的颜色编号
# sns.scatterplot(x = "sugarpercent",y = "winpercent", hue = "chocolate", data = candy_data)
# plt.title("Simple Scatter")
# plt.xlabel("sugarpercent")
# plt.ylabel("winpercent")
# plt.show()

# # regplot 对二维散点进行回归拟合
# plt.figure(figsize=(10,10),dpi =120)
# # hue 表示不同的组别，不同的颜色编号
# sns.regplot(x = "sugarpercent",y = "pricepercent", data = candy_data)
# plt.title("Simple Regression Scatter")
# plt.xlabel("sugarpercent")
# plt.ylabel("pricepercent")
# plt.show()

# lmplot对不同组别的散点分别进行回归拟合
# plt.figure(figsize=(10,10),dpi =120)
# # hue 表示不同的组别，不同的颜色编号
# sns.lmplot(x = "pricepercent",y = "winpercent",hue = "chocolate", data = candy_data)
# plt.title("Regression Scatter")
# plt.xlabel("sugarpercent")
# plt.ylabel("winpercent")
# plt.show()

# swarmplot描述整体组别数据信息
# plt.figure(figsize=(10,10),dpi =120)
# sns.swarmplot(x = "chocolate",y = "winpercent", data = candy_data)
# plt.title("Swarm Scatter")
# plt.xlabel("chocolate")
# plt.ylabel("winpercent")
# plt.show()

data_b = pd.read_csv("./datasets/cancer_b.csv",index_col="Id")
data_m = pd.read_csv("./datasets/cancer_m.csv",index_col="Id")
# print(data_b.head())
# print(data_m.head())

# # 直方图
# plt.figure(figsize=(6,6),dpi = 120)
# sns.distplot(a = data_b["Perimeter (mean)"],label = "B",kde = True)
# sns.distplot(a = data_m["Perimeter (mean)"],label = "M",kde = True)
# plt.legend(["B","M"])
# plt.show()

# # 密度曲线图
# plt.figure(figsize=(6,6),dpi = 120)
# sns.kdeplot(data = data_b["Perimeter (mean)"],label = "B")
# sns.kdeplot(data = data_m["Perimeter (mean)"],label = "M")
# plt.legend(["B","M"])
# plt.show()

# 不同的绘图风格 Style
# (1) "darkgrid", (2)"whitegrid", (3)"dark", (4)"white", and (5)"ticks"
# # 两个变量的联合概率密度曲线
fig = plt.figure(figsize=(10,10),dpi = 160)
sns.set_style("darkgrid")
sns.jointplot(x =data_b["Perimeter (mean)"],y = data_b["Concavity (worst)"],kind = "kde",fig = fig )
plt.show()


