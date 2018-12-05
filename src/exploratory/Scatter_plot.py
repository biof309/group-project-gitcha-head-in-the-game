#Make Scatter Plot
import matplotlib.pyplot as plt
Ave_scatter= plt.scatter(Ave_Heights_Weights[:,0], Ave_Heights_Weights[:,1], color='skyblue')
plt.xlabel('Average Height (Inches)')
plt.ylabel('Average Weight (lbs)')
plt.title('Average Height and Weight of All Breeds')
plt.savefig('Ave_scatter.png')