# Hierarchical clustering

Generates a nested structure of clusters

Due strategie principali:

- Agglomerative (bottom up)
  - as a starting state, each data point is a cluster
  - in each step the two less separated clusters are merged into one
  - **a measure of separation between pairs of clusters is needed**
- Divisive (top down)
  - as a starting state, the entire dataset is the only cluster
  - in each step, the cluster with the lowest cohesion is split
  - a measure of cluster cohesion and a split procedure are needed

Agglomerative clustering è il metodo più usato (e l'unico che abbiamo visto)

Le misure di separation che abbiamo visto sono quattro:

- single linkage: la distanza tra i due punti più vicini dei cluster
- ...

the strategy we use to compute the separation between clusters is an **hyperparameter**

# density-based clustering

questi metodi funzionano bene anche con cluster non convessi

- sappiamo già che k-means non funziona bene nel riconoscere cluster di questo tipo

## how do we compute density?

object-centered view

- guardiamo quanta gente c'è nell'intorno di raggio **epsilon** (hypersphere) di un punto
- define a **threshold** to categorize that point as dense or sparse

### border points vs outliers/noise

a border point doesn't have enought neighbours to be classified as dense, but has in its neighbourhood at least one core point

a noise point doesn't even have a core point in its neighbourhood

## reachability

reachability is not symmetric

- e.g. a border point is reachable from a dense point but not vice-versa

## DBSCAN

A cluster is a maximal set of points connected by density

"Each unclassified point attempts to start a cluster."

- **non bisogna fornire il numero di cluster!**
- ogni punto vede quali punti riesce a raggiungere tramite density connection
- quando non trova più alcun punto density connected il cluster si è formato
- tuttavia, abbiamo epsilon e la threshold come iperparametri

considerazioni:

- Finds clusters of any shape
- Is robust w.r.t. noise
- Problems if clusters have widely varying densities
- richiede tuning preciso di epsilone e del threshold minpoints

### How to set epsilon e minPoints

If epsilon is too small/minPoints is too high -> everything becomes noise

If epsilon is too high/minPoints is too small -> everything becomes one big cluster

Il primo approccio è di nuovo quello del gridsearch, seguito da analisi di score come distorsione o silhouette per confrontare la bontà tra clustering diversi

# Model based clustering

decision trees, kmeans, DBSCAN sono metodi non parametrici (c'è da capire di che parametri sta parlando il prof)

Estimate the parameters of a statistical model to maximize the ability of the model to explain the data

The main technique is to use the mixture models view the data as a set of observation from a mixture of different probability distributions (tipicamente mixture of gaussians)

- model based techniques work well only if the model is not too far from the reality
- if the data is skewed a mixture of gaussians wouldn't work well

we want to assign the parameters (mu e sigma) to the mixture of gaussians in a way that best fits the data

...

conclusione importante: the threshold is interesting

**NB**: **kmeans gives decent results but doesn't have any notion of model of the data**

- if there is a dataset that has a model behind, a model based clustering works better

# quick sketch of other clustering algorythms present in scikit-learn

don't care that much

...

interessante la comparison finale tra i vari metodi
