# Make Histagram of Average Weight
import matplotlib.pyplot as plt
Ave_Weight_Hist=plt.hist(Ave_Heights_Weights[:,1])
plt.xlabel('Average Weight (lbs)')
plt.ylabel('# Dogs')
plt.title('Average Weight of All Breeds')
plt.savefig('Ave_Weight_Hist.png')