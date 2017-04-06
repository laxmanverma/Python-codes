import matplotlib.pyplot as plt
#pyplot is a sub-package of matplotlib, hence the dot.

a=[-2,-1,2,3,4,5,6]
b=[4,1,4,9,16,25,36]
plt.plot(a,b)      #plot(line view) provides all the info for plotting but  
plt.show()         #python displays the graph only when show() func is called
plt.clf()          #cleans the graph again so you can start afresh.
plt.scatter(a,b)   #scatter(dot view/ individual point view)
plt.show()
