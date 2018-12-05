
#Make Scatter Plot
import matplotlib.pyplot as plt
Ave_scatter= plt.scatter(Ave_Heights_Weights[:,0], Ave_Heights_Weights[:,1])

plt.xlabel('Average Height (Inches)')
plt.ylabel('Average Weight (lbs)')
plt.title('Average Height and Weight of All Breeds')
plt.savefig(Ave_scatter.png)
plt.show()



#Make Histogram
Ave_Height_Hist= plt.hist(Ave_Heights_Weights[:,0])
plt.xlabel('Average Height (Inches)')
plt.ylabel('# Dogs')
plt.title('Average Height of All Breeds')
plt.savefig(Ave_Height_Hist.png)
plt.show()


Ave_Weight_Hist=plt.hist(Ave_Heights_Weights[:,1])
plt.xlabel('Average Weight (lbs)')
plt.ylabel('# Dogs')
plt.title('Average Weight of All Breeds')
plt.savefig(Ave_Weight_Hist.png)
plt.show()

#Make pairplot
pairplot=sns.pairplot(Characteristics_Total_df)
plt.suptitle('Dog Breed Characteristics', fontsize=30)
plt.subplots_adjust(top=1,wspace=.3)


