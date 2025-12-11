association rules -> attività unsupervised

- born in the area of data mining

market basket analysis

- we're interested in patterns in the data like: when someone buys item A, they also tend to buy item B
- the rules are not logic implications
- they represent cooccurence with a certain strength
  - the cooccurence relationship also has a direction (nota il verso della freccia)

support count non considera quello specifico itemset, considera anche insiemi più grandi che contengono quell'itemset

## support and confidence

low support

low support and high confidence: caviar and champagne

...

# Frequent itemset generation

sono tanti...

## Pruning strategy

...

# Association rule generation

### how can i decide the threshold?

start with a high threshold, if the number of rules is too high, lower it, iterate

# other measures to evaluate found rules

f11: support of the rule A=>C and C=>A

confidence can be misleading

- confidence and conditional probability go in opposite directions
- coffee is very common by itself

**NB**: High confidence can be interesting, but we should also look at other measures

- confidence can be misleading when the marginals are very different

## statistical measures

when should someone choose lift as a measure?

- it's the case where things are not so common but together cooccur a lot
- we're chasing for rare events with a strong positive correlation

# Association rules vs classification

Perché sia le association rules sia i classificatori cercano relazioni tra variabili, spesso rappresentate come:

“Se accade A e B → allora probabilmente accade C”

Questa struttura somiglia a una regola di classificazione, ma:

nel machine learning supervisionato C è un target scelto a priori;

nelle association rules le conclusioni sono scoperte dal modello senza target predefinito.

# Multidimensional association rules

...

# Multilevel association rules

...

# What is an important characteristic of association rules?

they are easily interpreted and explained: we have an antecedent and a consequent

#

...

there is a relationship between association rules and classifiers: an association rule can be interpreted as the output of a probabilistic classifier
