euclidean distance, e le altre distanze a seguito, must be calculated tenendo conto della scala delle features

- se le scale sono diverse la distanza dipende solo dalle feature con scala maggiore
- **standardization/rescaling è necessario**

# Minkowski distance

generalizzazione della distanza euclidea

possiamo considerare r come iperparametro da ottimizzare

- r=1 -> manhattan
- r=2 -> euclidean
- r=inf -> supremum distance -> considera solo gli attributi con distanza maggiore

# Manhattan distance

facciamo Sum of Absolute Values

what's the advantage?

- works better in high dimensional spaces
- with a large number of dimensions euclidean distance has a low effect on the final distance, whereas with manhattan distance the effect of a epsilon difference is entirely translated in the final distance

# Mahalanobis distance

the previous distances don't depend on the data.

we can consider the distribution of the data

- the distribution is described by the covariance matrix
- the distance between two points is greater if its along a direction with low variance e viceversa

---

#

metric spaces

time of the day is a non-metric space

- if we consider the distance of two events that occur in different days

---

# similarity between binary vectors

Per misurare la similarity tra binary vectors, consider the counts below

- M00 the number of attributes where p is 0 and q is 0
- M01 the number of attributes where p is 0 and q is 1
- M10 the number of attributes where p is 1 and q is 0
- M11 the number of attributes where p is 1 and q is 1

**Simple Matching Coefficient**

SMC = number of matches / number of attributes = (M00+M11) / M00+M01+M10+M11

**Jaccard Coefficient**

JC = M11 / M01+M10+M11

- utile dato che dire che due datapoints don't have a property non significa che siano simili
- di solito è utile quando il vettore binario è sparso (ovvero quando ci sono pochi uni)

# Cosine similarity

coseno tra due vettori di dati

ignores magnitude of the data, cares only about direction

Utile ad esempio in document similarity

- Doc B is just a shorter version of Doc A (same topic, fewer words)

# Use cases

- Manhattan distance for sparse, high dimensional data
- cosine similarity for checking document, image similarity
  - Rule of thumb:
    - Manhattan: "How different are the values?"
      - Use Manhattan when rating scale/magnitude matters
    - Cosine: "How similar are the patterns?"
      - Use Cosine when you care about proportional similarity, not absolute counts
