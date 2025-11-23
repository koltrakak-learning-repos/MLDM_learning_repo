# idea di k-means

let's assume we have an oracle that tells us the number of clusters

partiamo con centri a caso

assegnamo ad ogni datapoint una label corrispondente al centro più vicino

- per ogni punto dobbiamo computare quindi k distanze

iteriamo varie volte ricomputando ogni volta i centroidi dei cluster

# K-means più nel dettaglio

## What are we trying to optimize?

in transmission i have distortion: the original signal and the transmitted one are different

DEF: distortion/inertia come la somma delle squared differences tra punto originale e il decoded one

A cluster j with high SSEj has low quality

- i datapoint all'interno del cluster sono molto diversi tra di loro

### minimal distortion

ci chiediamo which properties are requested to c1, . . . , cK (decode(1), ..., decode(k); con 1, ..., k le label) for the minimal distortion?

1. xi must be encoded with the nearest center
     - otherwise the distortion (che ricordiamo essere la sommatoria delle squared differences tra centroidi e decode degli encode dei punti) could be reduced by substituting encode(xi) with the nearest center

2. The partial derivative of distortion w.r.t. the position of each center must be zero
    - vediamo la distorsione come funzione della posizione dei centroidi
    - nei punti di minimo le derivate devono valere 0
    - ma svolgendo i passaggi, questo ci fa notare che per avere la distorsione minima: each center must be the centroid of the points it owns

Le due proprietà ci danno l'algoritmo iterativo per diminuire la distorsione che abbiamo abbozzato spiegando l'idea di k-means

## Is termination guaranteed?

If after one iteration the state changes (i.e. abbiamo calcolato un nuovo centro), the distortion is reduced per la proprietà 2

Since distortion is reduced at each iteration we're guaranteed that we're not going to be getting stuck in a loop going back and forth between already explored states

- uno stato è una specifico labeling dei datapoints

Therefore each change of state bring to a state which was never visited before

There is only a finite number of ways to partition N objects into K groups (states)

## Are we sure that the best clustering scheme is found (optimal)?  Which is the definition of best clustering scheme?

the optimal solution is NOT guaranteed

- there is the possibility of getting stuck in a local minimum
- evitiamo però l'approccio a forza bruta in cui proviamo tutte le combinazioni di labelling (troppe)

## How should we start?

the starting point is crucial for not getting stuck in a local minimum

we can just try with a set of many starting points and see what gives us the best solution

## How can we find the number of clusters?

Siamo partiti con l'oracolo, ma k-means si chiama così proprio perchè k è un parametro da dare all'algoritmo. Come scegliamo il numero di cluster k?

di nuovo un approccio pragmatico è provare diversi valori

**Tuttavia, abbiamo un problema**

- mentre nel caso di varie configurazioni di starting point, possiamo scegliere come migliore quella che produce la distorsione minore (? è vera questa cosa?)
- nella scelta di k, la distorsione, detta anche SSE non è una buona misura per questo scopo dato che diminuisce al crescere del numero di cluster scelto a prescindere dalla bontà di questo numero

we need a value that measures how good a certain number of clusters is

- the best value finds the optimal compromise between the **minimization of intra-cluster distances** and the **maximization of the inter cluster distances**

### Outliers

are points with high distance from their centroid -> high contribution to SSE

potrebbe essere una buona idea rimuoverli

## Complexity of k-means

circa (nella pratica) lineare in N

- in ogni caso è veloce

o( T(NKD + ND) )

- NKD per labeling
- ND per calcolare i nuovi centroidi

## pro e contro

pro:

- veloce

contro:

- it is very sensitive to outliers
- does not deal with noise
- this algorythm doesn't work well when the points aren't distributed circularly wrt the centroids
  - when there are concavities in the clusters (non-convex clusters)
