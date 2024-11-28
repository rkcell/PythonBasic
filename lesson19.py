import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4,5]
# y = [4,5,6,7,8]
#
# plt.scatter(x,y)
# plt.title("Scatter Plot")
# plt.show()


# dist = np.array([20,40,25,15])
# names = ["Salome", "Ana", "David", "Giorgi"]
# plt.pie(dist, labels=names, wedgeprops={"edgecolor":"black"}, autopct="%1.2f%%", explode=[0.1,0,0,0])
# plt.show()

# names = ["Salome", "Ana", "David"]
# grades = [65,68,97]
#
# plt.figure(figsize=(6,4), dpi=100)
# barchart = plt.bar(names, grades)
# barchart[0].set_hatch("/")
# barchart[1].set_hatch("*")
# barchart[2].set_hatch("X")
# plt.show()

# x_1=np.linspace(0,5,100)
# y_1= x_1**2
#
# y_2 = x_1 * np.cos(x_1)
#
# y_3 = x_1* np.sin(x_1)
#
# plt.subplot(1,3,1)
# plt.plot(x_1, y_1)
# plt.title("First")
#
# plt.subplot(1,3,2)
# plt.plot(x_1, y_2, color="red")
# plt.title("Second")
#
# plt.subplot(1,3,3)
# plt.plot(x_1, y_3, color="black")
# plt.title("Third")
#
# plt.tight_layout()
# plt.show()

# x = [1,2,3,4,5]
# y = [4,5,6,7,8]
# plt.plot(x, y, label="hello-graph", color="cyan",linestyle="--", linewidth=2, marker="o", markersize=10)
#
# x2 = np.arange(1, 4.5, 0.5)
# x_1 = np.linspace(0,5,100)
#
# plt.plot(x2, x2**2, marker=".")
# print(x2)
# plt.title("გრაფიკი", fontdict={"fontsize":30})
# plt.xlabel("Time", fontdict={"fontsize":20})
# plt.ylabel("Money", fontdict={"fontsize":20})
# # plt.xticks([1,2,3])
# plt.legend()
# #plt.savefig("mygraph", dpi=200)
# plt.show()






import pandas as pd
try:
    data = pd.read_csv("foods.csv")
    data_spend=data["Spend"]

    print(data_spend)
    data_spend_filter=data["Spend"] > 30
    # print(data[data_spend_filter])
    # print(len(data.loc[data_spend_filter, "First Name"].tolist()))
    # print(len(data.loc[data_spend_filter, "First Name"].unique()))
except FileNotFoundError:
    print("File doesn't exist")