#plot a graph of temp against tym
import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=[5, 2, 4, 4, 8, 7, 4, 8, 10, 9]
plt.plot(x,y)
plt.xlabel ('Times(s)')
plt.ylabel ('Temparature(degC)')
plt.show()