# Make Histogram average height
import matplotlib.pyplot as plt
Ave_Height_Hist= plt.hist(Ave_Heights_Weights[:,0],color='skyblue', bins=20)
# Axis Labels
plt.xlabel('Average Height (Inches)')
plt.ylabel('# Dogs')
plt.title('Average Height of All Breeds')
# Save Image
plt.savefig('Ave_Height_Hist.png')
