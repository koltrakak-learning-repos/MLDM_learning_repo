Cos'è un decision tree?

- A run–time classifier structured as a decision tree is a **tree–shaped set of tests**
  - anche chiamato c4.5
- i nodi intermedi sono le domande
- le foglie sono le classification/decisioni
- The training process builds the tree
- The classification process walks the tree

# Decision tree model generation

Se il set non ha una classe univoca ma è _piccolo_, just take the majority

- ... cosa significa _small_ number?

I test conviene farli sempre binari

- non si guadagna granchè a scegliere dei test con più outcomes

...

We'll use information theory to find interesting patterns

Entropia:

- misura dell'information content
- segno - per correggere il logaritmo di numeri minori di 1
- guarda slide 33 in avanti

Entropia alta = confusione

- non so cosa mi arriva, probabilità simili

Entropia bassa = probabilità skewed

- mi aspetto che mi arrivi il simbolo con probabilità più alta

considereremo l'entropia delle classi

![come mai log2 per entropia?](img/log2_per_entropia.png)

after the split we have to subsets derived according to a rule

**with this we have a rule for defining the best split (the one that maximizes the information gain) if we choose an attribute**

slide 44 - in teoria l'ultimo predictor dovrebbe avere IG = 0

- non è così a causa di randomness
- the bigger is the dataset, the more attenuated this random effect is

che attributo usiamo? semplicemente quello che ci massimizza l'IG

slide 49 - dopo lo split l'entropia totale si è ridotta

- abbiamo eliminato un po' di confusione con il nostro split
- da un lato siamo puri
- dall'altro abbiamo praticamente solo due classi invece delle tre iniziali
- in generale, dopo lo split cio che si riduce è la weighted (by samples %) of the entropy of the descendants

When do i stop the recursion?

- when there's purity
- when we can't get any positivi information gain

l'implementazione scikit-learn chiama entropia -> impurità

###

Training set error of decision trees can be > 0

- decision trees by their nature can't discriminate data perfectly in any dimension
- they use only horizontal and vertical lines to discriminate classes
- that means that some cases can't be perfectly classified (ricorda VC dimension)

training set error is the lower bound of the error we can expect when classifying new data

the test set error is more indicative of the error with new data

# Overfitting

l'idea è che il modello si è troppo parametrizzato per il training set (che può ad esempio può non essere bilanciato) non riesce a generalizzare su new data

cause di overfitting

a good model has lower generalization error

## Pruning decision trees

A long hypothesis that fits the data is more likely to be a coincidence

...

high bias -> we're considering only a few parameters as our predictors

high variance -> we've learned noise

### hyperparameters

## other purity functions

gini index

# Complexity of decison tree induction (training)

# Characteristics of DTs induction (training)

redundant attributes do not cause any difficulty

- in DTs if we choose one or the other to partition the data it doesn't make that much of a difference because splitting considering one automatically split also with the other
- this is not true for other classification methods
