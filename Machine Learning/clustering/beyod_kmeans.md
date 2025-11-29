# Hierarchical clustering

...

the strategy we use to compute the separation between clusters is an hyperparameter

# density-based clustering

questi metodi funzionano bene anche con cluster non convessi

- sappiamo già che k-means non funziona bene nel riconoscere cluster di questo tipo
- come funzionano metodi gerarchici?

## how do we compute density?

- grid-based

- object-centered

define a threshold to categorize the point as dense or sparse

### border points vs outliers/noise

a border point has in its neighbourhood at least one core point

## reachability

reachability is not symmetric

- e.g. a border point is reachable from a dense point but not vice-versa

## DBSCAN

"Each unclassified point attempts to start a cluster." -> **non bisogna fornire il numero di cluster!**

tuttavia, abbiamo epsilon e la threshold come iperparametri

### How to set epsilon e minPoints

If epsilon is too small/minPoints is too high -> everything becomes noise

If epsilon is too high/minPoints is too small -> everything becomes one big cluster

Il primo approccio è di nuovo quello del gridsearch, seguito da analisi di score come distorsione o silhouette

Oppure utilizzare KNN

euristica: provare minPoint come il doppio con il numero di dimensioni

# Model based clustering

decision trees, kmeans, DBSCAN sono metodi non parametrici (c'è da capire di che parametri sta parlando il prof)

model based techniques work well only if the model is not too far from the reality

- here if the data is skewed a mixture of gaussians wouldn't work well

we want to assign the parameters to the mixture of gaussians in a way that best fits the data

...

conclusione importante:

the threshold is interesting

**NB**: **kmeans gives decent results but doesn't have any notion of model of the data**

- if there is a dataset that has a model behind, a model based clustering works better

# quick sketch of other clustering algorythms present in scikit-learn

don't care that much

...

interessante la comparison finale tra i vari metodi
