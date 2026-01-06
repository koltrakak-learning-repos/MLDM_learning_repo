association rules -> attività unsupervised

- born in the area of data mining

market basket analysis

- we're interested in patterns in the data like: when someone buys item A, they also tend to buy item B
- the rules are not logic implications
- they represent cooccurence with a certain strength
  - the cooccurence relationship also has a direction (nota il verso della freccia)

support count non considera quello specifico itemset, considera anche insiemi più grandi che contengono quell'itemset

**NB**: an important characteristic of association rules is that **they are easily interpreted and explained**: we have an antecedent and a consequent

(there is a relationship between association rules and classifiers: an association rule can be interpreted as the output of a probabilistic classifier)

## support and confidence

- support
  - Fraction of transactions that contain an itemset
  - E.g. σ("ciao") = 2/5
  - support count è invece solo la frequenza dell'itemset (nell'esempio sopra 2)

- frequent itemset
  - itemset con supporto maggiore di una certa soglia minSup

- association rule
  - un'espressione con un'antecedente A e un conseguente C (entrambi sono itemset)

- Rule evaluation metrics
  - support
    - Fraction of the N transactions that contain both A and C
  - confidence
    - definito come: sup(A,C)/sup(A)
    - Measures how often all the items in C appear in transactions that contain A
    - confidence alta significa che nella maggior parte delle transazioni in cui sono presenti A, sono presenti anche C
    - equivalente ad un supporto ristretto al sottoinsieme delle transazioni in cui compare A

**low support**

- significa che gli itemset della mia association rule non sono molto presenti nel mio dataset
- gli oggetti nell'antecedente non compaiono insieme a quelli del conseguente? NO, magari sono solo oggetti rari

**low support and high confidence**

- caviar and champagne
- oggetti rari che però se compaiono vengono spesso comprati assieme

**low confidence**

- antecedente e conseguente tendono a non comparire assieme in una transazione -> la regola non è molto affidabile/utile

## Association Rule mining task

Given a set of transactions N, the goal of association rule mining is to find all rules having:

- support >= minsup threshold
  - vogliamo che la regola sia sufficentemente presente
  - magari rara (vedi caviale e champagne), ma non un qualcosa di totalmente casuale (trattore e finocchi)
- confidence >= minconf threshold
  - vogliamo che la regola sia affidabile e che effettivamente antecedente in genere implica conseguente

Un approccio naive a questo task è l'approccio a forza bruta, chiaramente questo è computazionalmente infattibile

Trovare le rules consiste in:

1. Frequent Itemset Generation
    - Generate all itemsets whose support is greater than minsup
2. Rule Generation
    - Generate high confidence rules from each frequent itemset, where each rule is a binary partitioning (tra A e C) of a frequent itemset
    - le rule provenienti dallo stesso itemset avranno tutte lo stesso support

# Frequent itemset generation (apriori algorythm)

dati D items, ci sono M = 2^D candidate itemset di cui bisogna controllare se sono frequent o meno

- controllare tutto con un approccio a forza bruta non è possibile

Complexity: O(N W M)

- per ognuno degli M candidate itemset (e già solo questi sono un puttanaio)
- devo scansionare N righe del db
- scansionare ogni riga significa controllare W colonne

## Pruning strategy

Apriori principle: If an itemset is frequent, then all of its subsets must also be frequent

viceversa, ed è questo il caso che ci interessa di più, se un itemset non è frequent, allora tutti i suoi subperset sono anch'essi non frequent

## riassumendo

per generare frequent itemsets:

1. parti con gli itemset che contengono un solo elemento
2. computi il loro support ed elimina quelli sotto la soglia
3. di quelli rimanenti calcoli gli itemset con un elemento in più ed elimini quelli che discendono da un itemset poco frequente
    - questi si possono ripresentare nonostante non stia combinando direttamente con un itemset poco frequente
4. a questo punto si hanno i candidate itemset frequenti con due elementi e si itera

# Association rule generation (apriori algorythm)

Ora che abbiamo un listone di itemset frequenti possiamo generare delle regole con un support altrettanto alto

TASK: Given a frequent itemset L, find all the non-empty subsets f app. L such that: the confidence of rule f -> (L \ f) is not less than the minimum confidence threshold

- in pratica, cerchiamo tutti i possibili binary split con una confidence sufficentemente alta
- i sottoinsiemi di un insieme (binary split) sono un numero esponenziale
- anche qua dobbiamo fare pruning

mentre per la generazione degli itemset frequenti si faceva pruning in base al support dell'itemset, **per la generazione di association rules si fa pruning usando la confidence della regola**

ricorda che conf(A, C) = sup(A,C) / sup(A)

In particolare abbiamo che per regole generate dallo stesso itemset:

- meno item ci sono nell'antecedente, più il denominatore della confidence è alto -> più la confidence è bassa (il numeratore rimane lo stesso)
- questo significa che se una regola ha confidence bassa, tutte le altre regole discedenti da quest'ultima in cui si è spostato qualcosa da sinistra a destra avranno anch'esse una confidence bassa
  - **i discendenti di una regola con confidence bassa hanno confidence bassa**
- abbiamo la nostra strategia di pruning
  - per ogni itemset si crea una lattice in cui si parte con tutto a sinistra e ad ogni livello si sposta un elemento a destra
  - se un elemento ha confidence bassa, tutti i suoi discendenti avranno confidence bassa

esempio:

- itemset = {ABCD}
- conf(ABC -> D) = sup(ABCD)/sup(ABC)
- conf(AB -> CD) = sup(ABCD)/sup(AB)
- e così via ...
- il numeratore rimane lo stesso, ma il denominatore ha un elemento in meno ogni volta
  - sup(ABC) <= sup(AB)
  - conf(ABC -> D) >= conf(AB -> CD)

## riassummendo

per generare le association rules:

1. considera un frequent itemset alla volta e parti con le association rules che hanno tutti gli elementi tranne uno a sinistra
2. calcola la confidence di queste regole ed elimina quelle sotto soglia
3. di quelle rimanenti calcola le association rule figlie spostando un elemento da sinistra verso destra, ed elimina quelle regole che discendono da una con confidence bassa
4. a questo punto si hanno regole con alta confidence con un elemento in meno a sinistra e si itera
5. finito di esplorare un frequent itemset si passa al successivo

# other measures to evaluate found rules

Association rule algorithms tend to produce too many rules

- many of them are uninteresting or redundant
- Redundant if {A, B, C} -> {D} and {A, B} -> {D} have same support and confidence
  - tutte le volte che c'è ABCD c'è anche ABD -> basta ABD

Interestingness measures (other than support and confidence) can be used to prune/rank the derived rules

## contingency tables (tabella di contingenza)

È una tabella che mostra la distribuzione congiunta di due (o più) variabili, in cui:

- le righe rappresentano le categorie di una variabile
- le colonne rappresentano le categorie di un’altra variabile
- le celle contengono le frequenze (counts)

f11: support of the rule A=>C and C=>A

i marginali mi dicono il support di tea e di qualcosa diverso da tea

in basso a destra ho il numero totale di transazioni

**NB**:  confidence and conditional probability go in opposite directions

- p(A|B) == conf(B -> A)
- se confidence considera il marginale sull'asse orizzontale, conditional probability considera il marginale verticale; e viceversa

### esempio motivante sulla necessità di altre misure | confidence can be misleading

Nell'esempio abbiamo che tea -> coffee ha alta confidence

tuttavia, la probabilità condizionata ci dice che l'assenza di tea ci da una probabilità maggiore di avere coffee

- contraddizione
- questo ci dice l'esatto opposto della regola, ovvero che se prendiamo il tea si tende a non prendere il coffee

Il problema è che la confidence non considera che **coffee is very common by itself** (90% delle transazioni)

- di conseguenza, sarà presente anche in molte transazioni in cui il tea è presente
- ma non perchè avere il tea implica avere coffee, anzi sembra essere il contrario da quello che ci dice la probabilità condizionata

**conclusioni**:

- High confidence can be interesting, but we should also look at other measures
- confidence can be misleading when the marginals are very different

## statistical measures

Innanzitutto ricorda che:

- P(s, b) = P(s) * P(b)  -> statistical indipendence
- P(s, b) >= P(s) * P(b) -> positively correlated
- P(s, b) <= P(s) * P(b) -> negatively correlated

Le seguenti misure considerano la deviazione della cooccorrenza di antecedente e conseguente rispetto all'indipendenza statistica

### Lift

Lift(A -> C) = P(A, C) / P(A) * P(C) = conf(A,C) / sup(C)

- insensitive to rule direction

Il lift risponde a questa domanda: “Quanto è più (o meno) probabile osservare C quando avviene A, rispetto a quanto sarebbe probabile se A e C fossero indipendenti?”

- lift = 1 se A e C sono indipendenti
- lift > 1 se A rende più probabile C (rispetto al caso indipendente)
  - Esempio: lift = 2 → C è 2 volte più probabile dato A rispetto al caso indipendente.
- lift < 1 se A rende meno probabile C (...)

**NB: Il lift normalizza la confidence rispetto al support di C**

- confidence alta + lift ≈ 1 → regola poco interessante
- confidence alta + lift ≫ 1 → regola davvero informativa
- nell'esempio sopra C era il coffee ed aveva un sup molto alto che rendeva automaticamente alta la confidence di altre regole
- se computiamo il lift della regola notiamo che è < 1 e quindi la regola non è interessante

When should someone choose lift as a measure?

- it's the case where things are not so common, but cooccur together a lot
- we're chasing for rare events with a strong positive correlation

### Leverage

un po' la stessa cosa di lift

- insensitive to rule direction
- leverage evaluates to 0 for independence
- \> 0 per positive correlation
- <0 per negative correlation

### Conviction

anche questa è una variante sul tema

La conviction è il rapporto tra:

- gli errori attesi se A e C fossero indipendenti
- gli errori osservati ricordando che la regola predice “se A allora C”

- conviction = 1 se A e C sono indipendenti
- conviction > 1
  - la regola è informativa
  - La regola fa meno errori di quanto ci si aspetterebbe dal caso indipendente
  - Più è grande, più A “protegge” dall’assenza di C
  - es: conviction = 2 → la regola sbaglia la metà delle volte rispetto a quanto ci si aspetterebbe sotto indipendenza

- conviction < 1
  - la regola è fuorviante
  - A aumenta la probabilità che C NON accada

### Riassunto misure

- higher support -> rule applies to more records
- higher confidence -> chance that the rule is true for some record is higher
- higher lift (>1) -> chance that the rule is just a coincidence is lower
- higher conviction (>1) -> the rule is violated less often than it would be if the antecedent and the consequent were independent

**NMB**: bisogna sempre considerare confidence e almeno un'altra delle misure appena descritte

- A high confidence rule can have small lift if both sides are very frequent -> poco interessante
- A low confidence rule can have high lift if both sides are very infrequent

# Multidimensional association rules

Nel db non abbiamo più transazioni piuttosto abbiamo tuple con dei valori per una determinata dimensione della tabella

- in sostanza abbiamo uno schema e dei valori non solo itemset

c'è un'equivalenza tra i due ed è possibile passare da una rappresentazione all'altra

- da multidimensional a monodimensional
  - basta mettere i valori delle colonne in un unico set (transazione) in cui le posizioni rappresentano l'attributo del valore
- da monodimensional a multidimensional
  - abbiamo un one-hot-encoding dei valori presenti nella transazione
  - lo schema multidimensionale ha una colonna per ogni possibile oggetto che può essere presente in una transazione
  - ogni colonna ha come valore true se l'oggetto è presente nella transazione, false altrimenti
- **questo significa che possiamo rituilizzare gli algoritmi già visti trasformando la rappresentazione multidimensionale a quella monodimensionale**

**NB**: in questo contesto diventa importante **discretizzare** le variabili quantitative (numeriche) altrimenti avremmo troppi valori da considerare

- possiamo usare clustering o tecniche meno sofisticate, l'importante è dividere in intervalli i valori ed ottenere delle misure qualitative

# Multilevel association rules

(MBA = market basket analysis)

similmente a come si fa nella discretizzazione di variabili quantitative nel mining di association rules per dati multidimensionali, anche nel caso monodimensionale si possono avere troppi oggetti impossibili da considerare singolarmente

- computazionalmente proibitivo
- troppo dettagliato (non mi interessa latte qafshtama -> kellogs choco crave; mi interessa latte -> cereali), sarebbe pià utile poter ragionare a livelli di astrazione diversi

per risolvere il problema si ragiona per classi di oggetti

## cosa cambia?

quando si generalizza, il supporto delle regole aumenta e viceversa

- new rules can become interesting / uninteresting

quando si generalizza la confidence di una regola può aumentare o diminuire

If the specialized rule has (approximately) the same confidence as the general one, then it is redundant

## Come mino association rules multilivello?

Look for frequent itemsets at each level of abstraction, partendo da generale ed andando verso specializzato

- Decrease the support threshold in lower levels

Each level requires a new run of the rule discovery algorithm
