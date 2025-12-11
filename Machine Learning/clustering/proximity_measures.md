euclidean distance must be calculated tenendo conto della scala delle features

- se le scale sono diverse la distanza dipende solo dalle feature con scala maggiore
- **standardization/rescaling è necessario**

# Minkowski distance

generalizzazione della distanza euclidea

possiamo considerare r come iperparametro da ottimizzare

## Manhattan distance

what's the advantage?

with a large number of dimensions euclidean distance has a low effect on the final distance, whereas with manhattan distance the effect of a epsilon difference is entirely translated in the final distance

# Mahalanobis distance

the previous distances don't depend on the data.

we can consider the distribution of the data

the distribution is described by the covariance matrix

#

metric spaces

time of the day is a non-metric space

- if we consider the distance of two events that occur in different days

# similarity between binary vectors

Jaccard Coefficient

- utile dato che dire che due datapoints don't have a property non significa che siano simili
- di solito è utile quando il vettore binario è sparso (ovvero quando ci sono pochi uni)

...

#

Rule of thumb:

Manhattan: "How different are the values?"

- Use Manhattan when rating scale/magnitude matters

Cosine: "How similar are the patterns?"

- Use Cosine when you care about proportional similarity, not absolute counts
