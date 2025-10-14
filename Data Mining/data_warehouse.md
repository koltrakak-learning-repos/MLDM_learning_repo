data warehouse is designed to produce the data at the right level. It's the main tool to support BI

BI pyramid
- width is proportional to the amount of data

integrano più fonti di dati in un unico posto

... guarda meglio cosa si intende con DW (ero occupato a cambiare tema)


- historical data
    - normalmente quando faccio una UPDATE perdo il valore precedente
    - un servizio di DW mi mantiene dati sovrascritti per, ad esempio, 25 anni
    - non sovrascrivo dati ma piuttosto aggiungo entry più recenti

DW are subjcet oriented
- relational databases are more fact oriented
- the facts are spread across my information system
- the DW collects them


Consistent

...

Multidimensional model
- spazio discreto

...


# architectures

...

reconciled layer

data quality is a challenge for BI, ma a noi ci interessa per ML
- garbage in = garbage out

abbiamo ridondanza dato che lo stesso dato viene immagazzinato in
- source layer
- reconciled layer
- data warehouse


# conceptual modeling | DFM model
simile ad E/R
- sembra essere più adatta per DW dato che si adatta al modello del data cube (ci sono attributi che sono misure e attributi che sono dimensioni e granularità)

its important to be able to read this for ML purposes... Noi useremo solo plain csv files, ti interessa solo fino ad un certo punto

### esempio
sale è una collection of facts (a recording of something that has happened in the world)

ogni ramo distinto è assimiliabile ad una dimensione del data cube dell'oggetto in considerazione


...


slide 62-64 da saltare

slide 74-77 da saltare


# pros and cons of DW for MLDM
what had data warehouse have to do with data mining and machine learning?
