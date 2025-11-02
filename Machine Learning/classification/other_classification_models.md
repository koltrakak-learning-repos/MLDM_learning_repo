# premessa

con tutte queste varianti di modelli viene spontaneo chiedersi quale sia il migliore...

purtroppo, la risposta è dipende (nel senso che il migliore non esiste)

# Naive Bayes Classifier

Approccio probabilistico di classificazione. Chiamato in questo modo dato che is basa sul teorema di Bayes di probabilità

Abbiamo visto che i decision tree non sono un parametric classifier

- we don't make any probabilistic assumption

...

l'ipotesi è l'appartenenza ad una classe

l'evidence è una serie di attributi con determinati valori

noi siamo interessati a P(H|E) -> la probabilità di una classe dati quei valori degli attributi

**IMPORTANTE**: facciamo l'ipotesi (facilemente non vera) che gli attributi sono tutti indipendenti e quindi la probabilità che due attributi abbiano determinati valori è il prodotto delle probabilità

- per questo motivo si chiama naive, l'assunzione è molto simplicistica, però funziona!

**Problema**:
attributi con valore 0 fanno crollare la probabilità di una determinata classe a 0 (abbiamo un prodotto)

- per risolvere applichiamo Laplace smoothing

Problema:
se ho dei valori reali non posso calcolarne la frequenza
