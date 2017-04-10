import matplotlib.pyplot as plt
import numpy as np

x=[1000,4000,10000,60000]
y=[12,26,23,56]
Y=np.array(y)
color=['red','green','blue','yellow']
plt.scatter(x, y, s=Y*25, c=color, alpha=0.5)#value of s decides the size of dots
#Alpha can be set from zero to one, where zero totally transparant,
#and one is not transparant.
plt.xlabel('k=thousand')
plt.xticks(x,['1k','4k','10k','60k'])
plt.yticks(y,['1','2','3','4'])
plt.text(10000,23,'ans') #mark the point (10000,23) and label it as ans
plt.grid(True) #shows the grid on the graph
plt.show()

"""plt.yticks([0,1,2], ["one","two","three"])
In this example, the ticks corresponding to the
numbers 0, 1 and 2 will be replaced by one, two and tree, respectively."""
