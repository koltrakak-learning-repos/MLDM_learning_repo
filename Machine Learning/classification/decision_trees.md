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
