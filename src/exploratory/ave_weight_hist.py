# Make Histagram of Average Weight
import matplotlib.pyplot as plt
Ave_Weight_Hist=plt.hist(Ave_Heights_Weights[:,1], color="skyblue", bins=20, )
#Axis Labels
plt.xlabel('Average Weight (lbs)')
plt.ylabel('# Dogs')
plt.title('Average Weight of All Breeds')
# Save Image
plt.savefig('Ave_Weight_Hist.png')