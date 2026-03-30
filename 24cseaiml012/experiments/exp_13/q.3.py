import matplotlib.pyplot as plt
categories=[1,2,3,4]
values=[5,7,6,8]
plt.scatter(categories,values,color='g',label="bar plot")
plt.title("bar plot")
plt.xlabel("categories")
plt.ylabel("values")
plt.legend()
plt.show() 