Doggo Project aka gitcha head in the game
==============================

[slides](slides.html)




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── imports.py         <- packages needed for this project
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download data and make features
    │   │   ├── read_data.py
    │   │   └── make_features.py
    │   │   
    │   ├── dog_pictures   <- Some dog pictures for the slides
    │   │ 
    │   ├── exploratory    <- Scripts for producing exploratory data analysis and visualization 
    │   │   ├── make_ave_columns.py
    │   │   ├── make_height_hist.py
    │   │   ├── make_weight_hist.py
    │   │   ├── pairplot.py
    │   │   └── Scatter_plot.py
    │   │
    │   ├── models         <- Scripts and output for KMeans clustering
    │   │   ├── scale_data.py
    │   │   ├── KMeans.py
    │   │   ├── clusters.png
    │   │   └── clustered_breeds.txt
    │   │
    │   └── visualization  <- Scripts to get t-SNE vizualiation, as well as all exploratory plots and plots of clusters
    │       ├── Ave_Height_Hist.png
    │       ├── Ave_scatter.png
    │       ├── Ave_Weight_Hist.png
    │       ├── pairplot.png
    │       ├── t-SNE.py
    │       ├── t-SNE_plt.py
    │       ├── tSNE.png
    │       ├── cluster0.png
    │       ├── cluster1.png
    │       ├── cluster2.png
    │       ├── cluster3.png
    │       └── cluster4.png
    │
    ├──slides.md           <-markdown for slides for project
    ├──make_slides.py      <-script to product html slides from md
    ├──slides.html         <-slides for viewing
    │
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
