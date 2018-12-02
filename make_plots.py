import matplotlib.pyplot as plt
import seaborn as sns

#Make Scatter Plot

Ave_scatter= plt.scatter(Ave_Heights_Weights[:,0], Ave_Heights_Weights[:,1])

plt.xlabel('height')
plt.ylabel('weight')
plt.title('Average Height and Weight of All Breeds')
plt.show()

#Make Histogram
Ave_Height_Hist= plt.hist(Ave_Heights_Weights[:,0])
plt.show()

Ave_Weight_Hist=plt.hist(Ave_Heights_Weights[:,1])
plt.show()

#Make Pairplot
pairplot=sns.pairplot(Characteristics_Total_df)
plt.title('Dog Breed Characteristics')
plt.show()