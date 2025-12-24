Riprendiamo il concetto di Buisness intelligence:

- abbiamo visto che è un termine ombrello che racchiude tutte le tecniche e tecnologie e sistemi informativi che abbiamo visto essere fondamentali per prendere decisioni
  - BI integrates across all these, providing a unified platform that collects ERP data, automates MIS reporting, enables DSS-style analysis, and presents EIS-level dashboards
- **Transforming raw data into useful information to support effective and efficient business strategies.**

The Data Warehouse (DWH) is one of the main tool to support BI

# What is a Data warehouse?

Informally, a DWH is an optimized repository that stores **information** (quindi organizza e analizza i raw data) for the decision-makingprocess.

- DWs are a specific type of DSS.

## Caratteristiche

At first glance DWs may seem like regular databases, the difference is that they can support different kinds of workloads that DBMSs are not fit to do, for example they:

- provide the ability to manage sets of **historical data**
  - normalmente quando faccio una UPDATE perdo il valore precedente
  - un servizio di DW mi mantiene dati sovrascritti per, ad esempio, 25 anni
  - non sovrascrivo dati ma piuttosto aggiungo entry più recenti
- provide the ability to perform **multidimensional analyses**
- they can present data at the **right level of granularity (aggregation)**

It also provides the following features:

- It is **subject oriented** as opposed to fact oriented
  - traditional DBMSs are fact oriented in the sense that they focus on making an application work by storing events (facts) that happened
    - the facts are spread across my information systems
  - being subject oriented means being more focused on analyzing subjects more broadly, integrating all information related to that subject
    - the DW collects the scattered facts about a subject in a single place
    - e.g. we may have customer as a subject and want to know what a customer has bought, when and how much they spent, etc..
    - vedi star schema e DFM dopo
- It is integrated and consistent:
  - **it integrates data from different and heterogeneous sources, providing a unified view of it all.**
- It **shows the evolution over time** and it is not volatile:
  - changes to the operational data stores are tracked and recorded, allowing to create reports that show changes over a period of time.
  - **once data is committed, it is never updated or deleted, it becomes read-only and it is retained for future use.**
  - è questo quello che significa riuscire a gestire historical data

## OLAP and DWs

DWs are an OLAP technology and as such they offer the ability to do multidimensional analyses by means of the data cube.

For example, we can consider a data cube in which the **dimensions**:  are date, product and shop.

- Each cell of the cube will then represent a certain product, in a certain shop, in a certain day
- and it will contain a set of **measures**, for example the number of sales or the profit.
- **NB**: distinguiamo quindi tra dimensions, che sono punti di vista da cui possiamo fare un'analisi, e measures, che sono valori numerici che possono essere aggregati su una o più dimensioni
  - adesso forse si capisce meglio cosa significa essere subject oriented: grazie al modello del data cube possiamo fare query del tipo
    - “which products maximize the profit?”, “what is the total revenue per product category and state?”
    - comprimendo in questo modo alcune delle dimensioni del data cube
    - (nella pratica stiamo facendo delle group by)
  - vedi meglio dopo con star model e DFM

data cubes also support the idea of **hierarchy**:

- the product “apple” may be part of the sub-category “fruit”, which is part of the “edible” category of items
- possiamo quindi fare query a diversi livelli di granularità

## Differenze tra Database normali e DWs

DB:

- supporta transazioni che modificano una manciata di record in tabelle che hanno semplici relaizoni tra di loro
- le query sono read/write dato che l'obiettivo è far funzionare un'applicazione salvandone le transazioni
- usa schemi normalizzati per evitare ridondanza

DW:

- supporta analisi multidimensionale di dati provenienti da un numero enorme di record aggregati insieme in base al tipo di query
- le query sono più che altro read-only dato che l'obiettivo è l'analisi
- usa schemi denormalizzati, accettando ridondanza per facilità di analisi

## Data Marts

A Data Mart is a subset of the data stored to a primary data warehouse.

It includes a set of information pieces relevant to a specific business area, corporate department, or category of users.

- DMs are used as building blocks while incrementally developing DWs.
- DMs mark out the information required by a specific group of users to solve queries.
- DMs can deliver better performance because they are smaller than primary DWs.

# OLAP Analyses

OLAP analyses allow users to interactively navigate the data warehouse information.

Data is typically analyzed at different levels of aggregation (we can chooseto see more or less details), by applying subsequent **OLAP operators**

Data warehouses, being an OLAP technology, support OLAP operators

## Roll-up

causes an increase in data aggregation and removes a detail level from a hierarchy

- we reduce the number of elements in the data cube dato che stiamo aggregando più elementi insieme
- esempio: considero le vendite (misura) di categorie di prodotti e non i singoli prodotti

## Drill-down

è il contrario di roll-up. It reduces data aggregation and adds a new detail level to a hierarchy (e.g., from category to subcategory).

- stavolta aumentiamo il numero di elementi nel datacube

## Slice and Dice

The slicing operator reduces the number of cube dimensions after setting one of them to a specific value (e.g. Category = “Food and Beverages”)

- stavolta la granularità rimane la stessa ma ciò che cambia è il numero di dimensioni -> stiamo prendendo una fetta del datacube

The dicing operator reduces the set of data being analyzed by a selection criterion (e.g. Category.startWith("F"))

- il numero di dimensioni e la granularità rimangono gli stessi, stiamo selezionando un sottoinsieme degli elementi del data cube -> stiamo prendendo un sottocubo

# How do we build a DW? Extraction Transformation and Loading (ETL)

ETL process extracts, integrates and cleans data from operational data sources, in order to feed it to the data warehouse layer.

The process consists of:

- Accessing the data sources.
- Cleaning the data, as there may be missing values, duplicate value, inconsistencies (UNIBO e Unibo) or mistakes.
  - (non so perchè non c'è nella sigla)
  - **NB**: this operation is very costly and time consuming but leads to better data, and thus to better ML models, and thus to better insights
- Transforming the data, as it may be too detailed or there may be different ways of representing data (e.g. decimals separated with a dot or a comma).
- Loading the data into the data warehouse
  - **NB**: Since the ETL process is complex and time-consuming, data are loaded periodically in batches.
    - c'è una latenza prima che i dati presenti nelle sorgenti arrivino nella DW
  - As a result, a data warehouse usually contains historical, integrated and clean data, but not real-time data.
    - a DW privilegia la qualità e la coerenza dei dati rispetto alla freschezza.
  - This is acceptable because data warehouses support analytical and strategic decisions rather than operational tasks
    - DW serve per prendere decisioni strategiche, non per decisioni (strutturate) in tempo reale

# DW Architectures

Data warehouses have a series of requirements, among which we find:

- **Separation**: analytical and transactional processing should be kept apart as much as possible, since OLAP queries might impact normal, day-to-day OLTP operations.
  - questo significa che la DW deve essere veramente separata dalle sorgenti OLTP, e non solo una vista su qust'ultime
- Scalability: hardware and software architectures should be easy to upgrade as demands increase.
- Extensibility: the architecture should be able to host new applications and technologies without redesigning the whole system.

In base a come viene implementata l'archiettura della DW questi requisiti possono essere più o meno rispettati

## Single layer architecture

la DW è solo un middleware che offre una vista sulle sorgenti dati

- non dobbiamo preoccuparci di copiare i dati in un altro posto
- non rispettiamo il requisito di separazione e quindi day-to-day OLTP operations sono affette dalle OLAP queries

## Two layer architecture

Formata da: sources, data staging layer, data warehouse layer

- It has separation between physically available sources and data warehouses.
- the Data Warehouse layer stores information into one logically centralized single repository that can be directly accessed or it can be used as source for creating data marts
- Data Staging: is where the ETL procedures happen

ha problemi di scalabilità ed estensibilità

## Three layer architecture

introduce un altro layer chiamato: reconciliation layer che in qualche modo risolve i problemi della two layer architecture

abbiamo tanta ridondanza dato che lo stesso dato viene immagazzinato in:

- source layer
- reconciled layer
- data warehouse

# Data warehouse drawbacks

- **Latency in Data Availability**
  - Data in a DW is not real-time; it often comes with a delay due to the batch processing nature of ETL processes.
- Complex and costly setup
- **Limited Flexibility in Data Formats**
  - DWs are typically designed for structured data and may not handle unstructured or semi-structured data well, such as text, images, ...
  - This can limit the types of data that can be mined or used for training machine learning models.
- ETL Bottlenecks and Processing Overheads
  - The ETL process is often time-consuming and resource-intensive, creating bottlenecks, especially when dealing with large datasets or frequent updates.
  - Data scientists may face delays in accessing updated data, affecting the agility of the machine learning and data mining processes
- **Difficulty in Handling Rapidly Evolving Data**
  - collegato a sopra
  - DWs are often not well-suited for rapidly changing data or sources, as updating the schema and data models can be too time-consuming.
    - DWs should be mostly read-only
  - This lack of flexibility makes it difficult to integrate new types of data or sources quickly into the machine learning pipeline.
