# Meaning of the test error

Abbiamo già visto con i DT che **training set error is the lower bound of the error we can expect when classifying new data**

Abbiamo anche visto che usiamo l’errore del test set come stima del run time error

- ci interessa più che altro un ***upper bound del run time error***
- **If the test set error ratio is x, we should expect a run-time error x ± ???**
  - quanto fidarsi del training error? quanto può variare rispetto al runtime error?

Usiamo metodi statistici!

Il simbolo x ± ??? rappresenta l’intervallo di confidenza, cioè un range di valori dentro cui ci aspettiamo che cada il vero errore, con una certa probabilità (ad esempio 95%).

Ogni predizione può essere vista come un esperimento Bernoulliano:

- Successo = predizione corretta
- Fallimento = errore
- Se hai N elementi nel test set, hai N esperimenti indipendenti con probabilità di successo p (cioè probabilità che il modello indovini).
- f = errore empirico = S / N; con **S = numero di errori nel test set**
  - è una stima della vera probabilità di errore p

è chiaro che p (errore reale) non è esattamente uguale ad f (errore osservato)

- magari il test set non è perfettamente rappresentativo dei dati che verranno osservati a run-time
  - vedi dimensione del test set troppo piccola
- tutte le cause che portano a differenza tra f e p vengono raggrupato in un **rumore statistico.**
  - cominciamo ad intravedere un qualcosa con cui fare +-

Se il test set è grande (N ≥ 30), la distribuzione del rumore può essere approssimata con una distribuzione normale (grazie al teorema del limite centrale).

- Abbiamo la conferma guardando la formula: abbiamo un N a denominatore.
- Questo significa che maggiore è la dimensione del test set, minore è l'incertezza del mio intervallo di confidenza (+- part piccola)

Definiamo quindi un intervallo di confidenza centrato in f in cui ricade p con un certo livello di confidenza (1-alpha)

- where α is typically .05 or 0.01
- il livello di confidenza di questo intervallo (1-alpha) ci dice la probabilità che p (true error frequency) ricada in questo intervallo centrato in f

Il **pessimistic error** si ottiene prendendo il valore più alto dell’intervallo (+ invece di ±) e, come dice il nome, rappresenta la stima pessimistica della mia probabilità di errore p

- Il pessimistic error è l'errore che è bene utilizzare nella stima della bontà di un modello

Alcune conseguenze di questa modellazione statistica:

- se voglio un higher confidence level (1-alpha grande)
  - l'intervallo di confidenza cresce
  - e quindi anche l'errore pessimistico cresce
- al contrario, se mi basta una confidenza minore
  - l'intervallo di confidenza si stringe così come l'errore pessimistico
- in entrambi i casi, se facciamo crescere la dimensione del test set N,
  - l'intervallo di confidenza e quindi l'errore pessimistico diminuiscono
  - (inoltre, la differenza tra confidence level diversa si attenua)

**riassumendo**:

Hai ottenuto un errore empirico f dal test set ma vuoi sapere quanto è affidabile questa stima.

Costruisci un intervallo di confidenza intorno a f imponendo un certo livello di confidenza

- questo ti dice: “Con probabilità 1 − α (es. 95%) il vero errore reale p cade dentro questo intervallo.”

Esempio numerico:

- N = 1000 esempi nel test set
- f = 0.08 (8% di errore)
- confidenza = 95% → z = 1.96

Usando la formula del Wilson interval: Errore reale p ∈ [ 0.065 , 0.097 ]

cioè: “Stimiamo che l’errore reale sia 8%, ma con il 95% di confidenza è tra 6.5% e 9.7%.”

# Model selection for a classifier | train/test process

the model selection includes the selection of the learning algorithm and its (hyperparameter) optimisation

accuracy (e altre misure) vengono utilizzate in due modi:

- ottimizzazione:
  - otteniamo una misura con cui confrontare modelli diversi e configurazioni diverse degli iperparametri
- performance:
  - ottenere una stima di quanto il nostro modello sbaglia

è chiaro che vogliamo che le misure che usiamo per le valutazioni del nostro modello siano il più possibile affidabili e rappresentative delle performance a runtime.

A questo scopo abbiamo a disposizione diverse strategie con cui fare train e test tutte però con questi elementi in comune:

- several train/test loops are in general necessary to find the best set of values for the hyperparameters
- train and test should be done using different portions of the supervised data available
- in every step the data should be representative of the data that will be classified run–time
  - **NB**: It may happen that the proportion of classes in the supervised dataset X is altered in the Training, validation and Test sets, to prevent such cases the statistical sampling technique of **stratification** ensures the maintenance of the proportion of classes
  - stratify=y in scikit-learn

## holdout method | train/test split

- semplice e veloce
- Bisogna trovare un tradeoff tra training set e test set
  - più entry ci sono nel training set, meglio il modello impara
  - più entry ci sono nel test set, migliore è la stima dell'errore
- non permette tuning degli iperparametri
  - se controllo solo cosa mi migliora ler performance sul test set, sto overfittando gli iperparametri sul quello specifico test set

## holdout method | train/validation/test split

- Alleni il modello sul training set.
- Misuri l’errore sul validation set.
- Cambi iperparametri (es. learning rate, profondità, ecc.) finché le prestazioni migliorano.
- Quando hai trovato la configurazione migliore, testi una sola volta sul test set per stimare l’errore reale.

## crossvalidation

Cross-validation serve ad ottenere una stima dell'errore più affidabile, utilizzando in maniera più efficace l'intero dataset. Tutti i dati vengono usati sia per allenare che per testare, ma in momenti diversi.

- dividiamo il dataset in k folds e facciamo k iterazioni di train con test
  - ad ogni iterazione cambiamo la fold con cui facciamo il test
- ad ogni permutazione di fold otteniamo una stima dell'errore
- finite le k iterazioni, abbiamo k stime dell'errore
  - questi diversi errori sono stati ottenuti guardando diverse porzioni dell'intero dataset
  - facendone la media è più o meno come se avessimo usato l'intero dataset come test set
  - otteniamo una stima dell'errore più affidabile rispetto ad holdout method che considera solo una porzione del dataset nel test set
    - anche se dovrebbe essere comunque rappresentativa dell'intero dataset con stratification
- ottenuta la stima dell'errore, possiamo utilizzare l'intero training set per fare un ultimo training ed ottenere un modello leggermente migliore

ogni elemento del dataset viene usato:

- k-1 volte per il training
- e una volta per il testing
- optimal use of the supervised data

- **NB**: the error generated by crossvalidation is more reliable since it's less prone to randomness/configurazioni fortunate/sfortunate nel test set (facciamo una media)

**NB**: Nell'ottimizzazione degli iperparametri si potrebbe pensare di applicare crossvalidation tante volte con varie configurazioni degli iperparametri in maniera da trovare la configurazione migliore.

- tuttavia, se utilizziamo crossvalidation sull'intero dataset, siamo suscettibili ad overfitting degli iperparametri come lo eravamo nel caso del semplice train/test split
- come prima stiamo utilizzando gli stessi dati per training and testing finale, potrei quindi star ottimizzando gli iperparametri per questa mia specifica istanza di dataset senza accorgermi di non star generalizzando

## crossvalidation only on the training set

La soluzione è quella di introdurre di nuovo un test set che verrà utilizzato solo alla fine

- faccio un train/test split
- per ogni configurazione di iperparametri che voglio testare applico crossvalidation sul training set
  - stavolta ho dei fold di validation e non di test
  - ho le stesse proprietà di prima ma sul validation error
    - ho un validation error più affidabile dato che è stato ottenuto come media sull'intero training set
    - meno probabile che io ottenga un validation error alto/basso a causa di validation set sfortunato/fortunato
- scelgo la configurazione degli iperparametri che mi da crossvalidation error minore e alleno il modello finale sull'intero training set
- alla fine di tutto faccio l'ultima verifica di performance sul test set che ho messo da parte così da **ottenere una misura delle performance del modello veritiera anche per il mondo reale, su cui posso fare affidamento per capire se il modello sta generalizzando**

**NB**: notare che crossvalidation è un buon metodo per la stima degli iperparametri.

- se consideriamo il caso di gridsearch con holdout potrebbe capitare che una configurazione degli iperparametri risulti particolarmente buona solamente a causa di una istanza particolarmente fortunata del test set
  - **la configurazione degli iperparametri sarebbe overfitted sul test set**
- questo problema in gridsearch con crossvalidation viene mitigato dato che il test set è diverso per ogni fold
  - facendo la media tra i risultati dei vari fold otteniamo un risultato più affidabile che ci permette di scegliere degli iperparametri più generali
  - crossvalidation riduce per sua natura l'overfitting degli iperparametri su validation/test set dato che quest'ultimi diventano molto grandi
- se tengo un test set da parte posso anche anche accorgermi se sto overfittando gli iperparametri sul validation set
  - avrei una performance sul validation set che non si traduce nel test set

**NB**: The split should be as random as possible. Quando dividi un dataset in training, validation e test, l’obiettivo è che ogni insieme rappresenti bene la distribuzione reale dei dati e che non contenga bias dovuti all’ordine o ad altri fattori strutturali.

Se non usi la casualità (per esempio, prendi i primi 80% dei dati per il training e gli ultimi 20% per il test), rischi che:

- il modello “veda” solo un certo tipo di esempi in training,
- e che il test contenga casi molto diversi → valutazione non realistica.

**NB**: in generale l'obiettivo è ottenere misure nel training set e nel test set il più simili possibili.

- questo mi garantisce che il modello riuscirà a generalizzare anche nel mondo reale
- se avessi una accuracy nel test set molto diversa rispetto a quella del training set, ma comunque molto alta, quella misura non sarebbe per niente indicativa della accuracy nel mondo reale
- **quanto le performance su training set sono molto diverse rispetto a quelle sul test set, questo è il caso di overfitting**
  - quando si applica regularization in genere si tende a far avvicinare training error e test error, aumentando train error e diminuendo test error

## Tirando alcune somme su model selection

in pratica se si vuole fare tuning degli iperparametri le alternative sono due: holdout o crossvalidation

- crossvalidation è migliore in caso di dataset piccoli perché permette di evitare un validation set troppo piccolo il che riduce la probabilità di scegliere iperparametri overfittati sulla specifica istanza di validation set
- con dataset grandi, la differenza tra CV e semplice split si riduce molto dato che il validation set è sufficientemente grande
  - in questo caso conviene holdout dato che richiede meno iterazioni e addestramenti

---

# Performance measures

la più semplice è l'accuracy

questo permette di introdurre anche **confusion matrix**

Accuracy non è sufficiente come unica misura. A classification error can have different consequences, depending on the class of the individual

- when forecasting an illness a false positive can be less dangerous than a false negative
- consider the cost of retiring a machinery as damaged, while it is ok (false positive) is certainly preferable than the cost of an unpredicted failure (false negative)

**Abbiamo bisogno di altre misure che tengono più in conto di false negative/false positives**

- Precision: TP/(TP+FP)
  - the rate of true positives among the positive classifications
  - alto quando non classifico come positivi individui che non lo sono
- Recall: TP/(TP+FN)
  - the rate of true positives that i can catch
  - alto quando non classifico come negativi individui che non lo sono
- F1-score: 2*(prec*rec)/(prec+rec)
  - grande quando precision e recall sono simili (non sbilanciati)
  - alto quando ho pochi FP e FN, ovvero quando catturo la maggior parte dei casi positivi senza avere tanti FP

## what measure should we use

Accuracy gives an initial feeling of the effectiveness of the classifier, but **can be heavily misleading when classes are highly imbalanced**

- potrei sbagliare sempre le classi poco rappresentate

If the the costs of errors on positives and negatives are significantly different, then it is necessary to evaluate precision and recall.

F1-score sempre interessante perchè mi da un'idea di quanto precision e recall siano bilanciati

## Multiclass case

Quando ho più di due classi si estende la confusion matrix aggiungendo oltre alle predizioni corrette le predizioni sbagliate e con quale classe è stata sbagliata

- es: FP_a-b ho predetto b al posto di a
- **NB**: adessono abbiamo solo true prediction (TP) e false prediction (FP); non abbiamo più false negatives

Accuracy adesso diventa:

- accuracy  = sum_su_tutte_le_classi(TP) / N

Le altre misure di performance adesso vanno distinte da classe a classe

- precision = TP_i / P_i
- recall    = TP_i / T_i
- f1-score uguale a prima

Abbiamo un problema, if we want to use scikit learn functions like gridsearchcv to optimize something other than accuracy in a multiclass model **we need a sort of average value of the measure for the classes**

- we need a single value to optimize
- if the classes are balanced it doesn't really matter, we can choose media aritmetica della misura across classes (macro avg)
- if they are unbalanced it matters

macroaverage da la stessa importanza a tutte le classi; underepresented o meno

weighted average fa una media pesata degli score across classes con peso pari alla frequenza della classe nel dataset

- mi permette di dare meno importanza alle classi meno rappresentate

microaverage ci interessa di meno

**NB**: the scoring is decided depending on your need! Ad esempio, è il buisness owner che ti viene a dire che lui vuole il weighted recall migliore possibile. NON possiamo scegliere lo scoring che ci dà il risultato migliore possibile

## Beyond pure counting

is our classifier making correct predictions by chance?

Example: early diagnosis

- let us consider a disease affecting 2% of patients
- a prediction saying always “no disease” has 98% precision, which, in general would be a good result
- è chiaro però che questo classifier è inutile

...

definiamo il Cohen k-score di un classifier C: k(C)

- un altra misura (insieme ad accuracy, precision, ...) che ci permette di trovare la miglior configurazione degli iperparametri per i nostri scopi
- misura che varia da -1 a 1;
  - se >0 siamo migliori rispetto al random assignment; se <0 siamo peggiori
  - se = 1 siamo perfetti
- nell'esempio della malattia: se C ha accuracy 98% -> k(c) = 0

k score becomes good after 0.6

## Cost sensitive learning

if before training we have more information such as

- the cost of errors
- the cost of good prediction
- the cost of bad prediction

we can influence the training of our models to try to reduce the more costly errors

Several alternatives:

- alterate the proportion of classes in the supervised data, duplicating the examples for which the classification error cost is higher
  - In this way, the classifier will became more able to classify the classes for which the classification error cost is higher
  - This solution is useful also when the classes are imbalanced, that is the frequencies of the class labels in X are not equal
- alcuni algoritmi di training permettono di dare un peso alle classi più importanti
  - class_weight nei DT permette di definire dei pesi per le classi che definiscono quali sono le classi più importanti da classificare correttamente
  - questo influenza il training (calcolo dell'impurità di un nodo immagino)

# Evaluation of a Probabilistic classifier

Many classifiers produce, rather than a class label (crisp prediction), a tuple of probabilities, one for each possible class, (probabilistic, or soft prediction)

- interessante utilizzare la probabilità predetta come strumento di ranking quando si lavora in batch-mode
- ho un batch di oggetti, filtro solo quelli che hanno una probabilità che rispetta una threshold ed ottengo un subset

### Lift chart

the lift tells us how much a predicted probability is better than a random choice

utile quando si lavora in batch mode

### ROC curve

qua non lavoro in batch mode ma caso per caso in una crisp mode

- here i want to transform the probabilistic output into a crisp one

voglio anche configurare quanto è facile/difficile data una probabilità, assegnare l'oggetto ad una classe

Calcolare la ROC curve mi permette di vedere come il variare della threshold mi fa crescere il numero di positives e false positives che catturo (e viceversa)

- molto utile se ad esempio false positives mi fanno molto male e magari false negatives non così tanto
