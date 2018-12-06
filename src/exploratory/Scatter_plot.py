#Make Scatter Plot
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
Ave_scatter= plt.scatter(Ave_Heights_Weights[:,0], Ave_Heights_Weights[:,1], s=[70], marker='*',color='skyblue')
#label axis
plt.xlabel('Average Height (Inches)')
plt.ylabel('Average Weight (lbs)')
plt.title('Average Height and Weight of All Breeds')
# Set axis limits
plt.xlim(1, 60)
plt.ylim(1, 190)
# Add trendline
z = np.polyfit(Ave_Heights_Weights[:,0], Ave_Heights_Weights[:,1],1)
p = np.poly1d(z)
plb.plot(Ave_Heights_Weights, p(Ave_Heights_Weights), 'm--')
plt.show()


#save figure
plt.savefig('Ave_scatter.png')