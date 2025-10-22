A classifier algorythm is composed of two parts

- the general schema is the same for every classifier
- the parameters are learned through examples

Chiamiamo **predictors** gli attributi degli individuals che vogliamo classificare

How do we evaluate the performance of our model?

- we can subdivide the data set in
- a training set
- a testing set

even the best position of the straight line misclassifies some points

- this decision function is limited

 **Vapnik-Chervonenkis Dimension**: Given a dataset with N elements there are 2^N possible different learning problems

- consideriamo solo due classi
- il primo learning problem con tutti gli n elementi appartenenti alla prima classe, il secondo con tutti meno uno, ecc...

If a model M is able to shatter (classificare correttamente) all the possible learning problems for at least one set of N elements, we say that it has Vapnik-Chervonenkis Dimension equal to N

- The straight line has VC dimension 3
  - ricorda che basta UN set di 3 elementi; il caso dei tre punti allineati non è un problema -> (<https://datascience.stackexchange.com/questions/32557/what-is-the-exact-definition-of-vc-dimension>)

Don’t worry, frequently, in real cases, data are arranged in such a way that also a straight line is not so bad

Also, problem of **generalization**:

- we could imagine a perfect function that bends and curves as to classify correctly our dataset
- but the perfect function for a dataset would not be suitable for new data

One of the main tradeoffs for machine learning is to **balance the classification with generalization**

- the more parameters our model has, the less general it is with other data
- a good idea is to start with simple models, and then complicate as necessary

**Slide 12 molto importante**

Accuracy is just the starting point for model evaluation

- it's just one of the option
- giusto per avere un idea preliminare, possiamo pensare che a volte è peggio sbagliarsi dicendo vero che falso mentre altre volte il contrario

The model has two algorythms

- one for training
- one for executing
  - tipically this one is much simpler, it just considers the parameters

Two flavour of classification

- crisp
- probabilistic
- we'll see that depending on the case, one can be more appropriate than the other
