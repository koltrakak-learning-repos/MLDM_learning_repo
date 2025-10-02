data warehouse è nato in maniera indipendente dalla pipeline di machine learning
- nato in risposta ai bisogni dei manager

Circa 15 anni fa, ci si è accorti che buttare via i dati non è una buona idea
- se ho dei sensori e non riesco ad analizzare tutti i dati che producono
- non butto niente

Potrei mettere questi dati in un DW in quanto additiva
- ma questo è costoso
- devo pensare ad ETL
- allo schema
- ...

Data Lake serve come posto in cui mettere dati che non riesco a processare immediatamente ma che non voglio buttare via
- meno costoso di un DW
- butto dentro e me ne dimentico

Me ne dimentico si fa per dire, chiaramente prima o poi voglio recuperare i dati che messo dentro al DL. Per questo motivo ho bisogno di metadati che mi permettono di classificare e recuperare i dati che mi servono
- il recupero dei dati non deve essere veloce dato che questi dati non sono online

Data lake is one of the possible sources of information for the data mining pipeline


in DW si usa **schema-on-write**
- decido lo schema dei dati quando scrivo i dati dentro a DW

in DL si usa **schema-on-read**
- decido lo schema dei dati quando leggo i dati dal DL

DL complements DW for data science and ML, it doesn't substitute it


# architettura data lake
Problemi del data lake
- dati potrebbero arrivare in burst improvvisi e l'infrastruttura (dischi, cloud, ...) non è pronta ad accettare quest'ultimi
- non si vuole perdere i dati e quindi si prevedono delle code con cui fare buffering

- batch layer for data that arrives in batches
- speed layer for data that arrives in real-time

recently: lakehouse architecture

so we have two different kinds of data batch and real time

and we ingest them in separate pipelines


