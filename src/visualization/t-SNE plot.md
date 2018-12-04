Plot t-SNE

```python
tsne_plot=plt.scatter(x,y, alpha=0.5, c=clusters)

for x,y,breed in zip(x,y,breedlist):
    .tsne_plot=plt.annotate(breed, (x,y), fontsize=4, alpha=0.5)
.tsne_plot=plt.show()

```

