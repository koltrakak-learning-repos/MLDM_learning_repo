# Challenges today | motivation for data lakes

Circa 15 anni fa, ci si è accorti di avere un sacco di dati (**dark data**) inutilizzati, e che buttare via quest'ultimi non è una buona idea

- se ho dei sensori e non riesco ad analizzare tutti i dati che producono sto sprecando delle opportunità

Potrei pensare di mettere questi dati in un DW, ma vengono prodotti con alta frequenza (high velocity) e sono tipicamente non strutturati, difficili da gestire in DW tradizionale.

- devo pensare ad ETL che non funziona bene con high velocity e real-time decision making
- allo schema per questi dati non strutturati
- storage costoso

**Data Lake** come posto in cui mettere dati che non riesco a processare immediatamente ma che non voglio buttare via

- storage meno costoso di un DW
- butto dentro e me ne dimentico

A Data Lake is a centralized repository that **stores all types of data: Structured, semi-structured, and unstructured**

- Data is stored with minimal transformation (schema-on-read)

They are a repository of data stored in its natural/raw format, usually in the form of object blobs or files.

- As soon as data becomes available from any source, we store it, deferring the decision of what to do with it.
- Dive anywhere, flexible access, schema on read.
  - with schema on read we sacrifice ease of use by requiring additional processing to “frame” the data, in order to have important gains in versatility (data is simply dumped into the lake).
  - DBMSs and data warehouses operate following the opposite methodology, the “schema on write”, requiring the schema to be defined before inserting the data.
- **NB**: siccome viene utilizzato schema-on-read, senza preprocessing iniziale (vedi ETL), fare ingestion è molto facile e quindi **i data lake abilitano lo storage di streaming data!**

Data lakes provide a foundation for data science and AI

- one of the possible sources of information for the data mining pipeline
- enables use of unstructured data
- enables self-service data exploration

in DW si usa **schema-on-write**

- decido lo schema dei dati quando prima di scrivere i dati dentro a DW

in DL si usa **schema-on-read**

- decido lo schema dei dati quando leggo i dati dal DL

# Casi d'uso data lake

I Data lake abilitano:

- Ingestione veloce e flessibile dei dati
  - Non devo modellare prima lo schema
  - Posso accettare stream, file, immagini, log, raw IoT, ecc.
  - Posso mettere dentro tutto fin da subito
- Archivio storico a lungo termine
  - Economico rispetto al DW
  - Scalabile quasi illimitatamente (basta usare più cloud storage)
  - Mantiene i dati nel loro formato originale
- Base dati per analisi avanzata
  - Ottimo per data mining, machine learning, analytics esplorativa
  - Perfetto per addestrare (e riaddestrare) modelli su grandi dataset storici

Esempi di casi d'uso:

- Customer 360
  - ingest continuo dei touchpoint (app, web, negozi)
  - lo streaming aggiorna i profili in tempo quasi reale
  - data lake conserva tutto lo storico per training ML

- Real-time fraud detection
  - il motore stream analizza transazioni al volo con modelli ML
  - il lake conserva log completi per audit e retraining

- Predictive maintenance in manufacturing
  - sensori IoT generano dati in tempo reale
  - alert immediati se vibrazione/temperatura = anomalia
  - il lake immagazzina i dati grezzi per analisi storica

# architettura data lake

we have two different kinds of data: batch and real time. We ingest them in separate pipelines

- dati potrebbero arrivare in burst improvvisi e l'infrastruttura deve essere pronta ad accettare quest'ultimi
- non si vuole perdere i dati e quindi si prevedono delle code con cui fare buffering
- batch layer for data that arrives in batches
- streaming/speed layer for data that arrives in real-time
