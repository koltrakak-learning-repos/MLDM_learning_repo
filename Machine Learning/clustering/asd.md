let's assume we have an oracle that tells us the number of clusters

partiamo con centri a caso

iteriamo varie volte ricomputando ogni volta i centroidi dei cluster

## What are we trying to optimize?

in transmission i have distortion: the original signal and the transmitted one are different

definiamo distortion/inertia come la somma delle squared differences tra punto originale e il decoded one

### minimal distortion

le due proprietà ci danno l'algoritmo iterativo per diminuire la distorsione

## Is termination guaranteed?

since distortion is reduced at each iteration we're guaranteed that we're not going to be getting stuck in a loop going back and forth

## Are we sure that the best clustering scheme is found (optimal)?  Which is the definition of best clustering scheme?

the optimal solution is NOT guaranteed

- there is the possibility of getting stuck in a local minimum
- evitiamo però l'approccio a forza bruta

## How should we start?

the starting point is crucial for not getting stuck in a local minimum

- we can just try with a set of many starting points and see what gives us the best solution

## How can we find the number of clusters?

siamo partiti con l'oracolo

di nuovo un approccio pragmatico è provare diversi valori

we need a value that measures how good a certain number of clusters is

la distorsione, detta anche SSE non è una buona misura per questo scopo dato che diminuisce al crescere del numero di cluster scelto a prescindere dalla bontà di questo numero

### Outliers

potrebbe essere una buona idea rimuoverli

## Complexity of k-means

linear in N (mi sembra pseudo polinomiale in realtà)

in ogni caso è veloce

o( T(NKD + ND) )

- ND per calcolare i nuovi centroidi
- NKD per labeling

##

this algorythm doesn't work well when the points aren't distributed circularly wrt the centroids

- when there are concavities in the clusters

# Evaluation of a clustering scheme

since clustering in not supervised evaluation is more difficult

- we don't have a ground truth to compare with

## TSS

TSS sparsity of the dataset

a better clustering scheme deacreses (minimizes) SSE and this increases (maximizes) SSB

## Other measures to express the quality of a cluster

inertia has a bad property: it doesn't have an upper bound

### Silhouette score

[-1, 1]

increases with the separation between clusters

decreases for clusters with low cohesion (sparsity)

good cohesion = small average distance

...

elbows in the graph of inertia are a suggestion that that number of clusters is significant

## Looking for the best number of clusters

silhouette score seems more promising but it's more computationally intensive

inizialmente possiamo usare l'elbow method con SSE

se non c'è un clear elbow possiamo passare a silhouette score

# Partial supervision with gold standard
