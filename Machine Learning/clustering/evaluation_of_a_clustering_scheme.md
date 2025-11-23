# Evaluation of a clustering scheme

since clustering in not supervised, evaluation is more difficult

- we don't have a ground truth to compare with to abtain a notion of error/loss

we need one or more score function to measure various properties of the clusters and of the clustering scheme as a whole

- ad esempio, vorremmo uno score utile a capire il parametro k in k-means

It is related only to the result, not to the clustering technique

# Cohesion and separation measures

## SSE

SSE/SSW misura la **coesione dei cluster**: quanto ogni punto è vicino al centro del suo cluster.

- SSE alto significa cluster poco compatti

## Sum of Squares Between clusters (SSB)

Misura quanto i centroidi dei cluster sono lontani dalla media globale del dataset

- è una **misura della separazione tra cluster**
- SSB alta → i cluster sono molto lontani tra loro → buona separazione
- SSB bassa → i cluster sono vicini → separazione debole o cluster molto simili

## Total Sum of Squares (TSS)

sum of squared distances of the points from the global centroid

- **NB**: al contrario delle due misure precedenti **non dipende dal clustering scheme**, è una proprietà del dataset

TSS misura la **sparsity of the dataset**

- TSS alta, abbiamo datapoints molto sparsi rispetto al centro
- TSS bassa, abbiamo datapoints molto vicini al centro

vale sempre che: TSS = SSE + SSB

A good clustering scheme

- deacreses (minimizes) SSE -> maximizes intracluster cohesion
- and this increases (maximizes) SSB -> maximizes cluster separation
- basta farne uno e l'altro viene da se: miminize SSE == maximize SSB

# Silhouette score as a score for evaluation of a clustering scheme

Requirements for a clustering quality score:

- values are in a standard range, e.g. [1, 1]
- increases with the separation between clusters
- decreases for clusters with low cohesion or, in other words, with high sparsity

Notiamo che la distorsione non è una misura adatta per valutare un clustering

- it doesn't have an upper bound
- it doesn't take into account separation between clusters
- it INCREASES for clusters with low cohesion
- if we tried to measure clusters with high cohesion, the distorsion would always get lower with a larger number of clusters

Silhouette score è invece un buon clustering quality score:

- Considers the INDIVIDUAL contribution of each object, say xi, to cluster sparsity and separation from other clusters
- For the global score of a cluster/clustering scheme compute the average score over the cluster/dataset

**Intuition**:

- when the score is less than zero for an object, it means that there is a dominance of objects in other clusters at a distance smaller than objects of the same cluster
  - sparsity domina
- altrimenti, il contrario
  - separation domina

Viene da se che vogliamo un silhouette score positivo più grande possibile

NB: elbows in the graph of inertia are a suggestion that that number of clusters is significant

- one of these points is frequently a plausible value for K

## Looking for the best number of clusters | elbow method

silhouette score seems more promising but it's more computationally intensive

inizialmente possiamo usare l'elbow method con SSE

se non c'è un clear elbow possiamo passare a silhouette score

# Partial supervision with gold standard

partition è un termine che crea confusione

**il gold standard è un insieme di etichette per il mio dataset**

perchè usare il gold standard? To validate a clustering technique which can be applied later to new, unlabelled data

- confrontiamo il mio clustering scheme con quello del gold standard per capire se sto raggruppando bene o male
