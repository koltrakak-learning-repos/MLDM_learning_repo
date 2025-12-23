# Data

- Data: a collection of raw value elements
- Information: the result of collecting and organising data
  - relationships between data items
  - context
  - meaning
- Knowledge: understanding information based on recognising patterns
  - pensa ad association rules

Data exists independently from Data Mining and Machine Learning... **but you need Data Mining and Machine Learning techniques to derive interesting and actionable insight**

`Where does data come from?`

Data comes from events happening in the real world that get stored in a database

These events can be represented as:

- a transaction:
  - an event that modifies the state of stored data or generates a new entry
  - moving from one stable state to the other
- a signal:
  - the reading of a measure produced by a sensor

`How do we process data to transform it into knowledge?`

Different tools and techniques allow to gather increasing insights on data by adding structure and interpreting it

In questo campo i sistemi informativi giocano un ruolo fondamentale

# Carrellata sistemi informativi

## OLTP based systems

1. OLTP (OnLine Transaction Processing)
    - a class of software programs capable of supporting transaction-oriented applications and data storage
    - salvano transazioni (es: acquisti in un supermercato, checkin in un areoporto, ...)

2. ERP (Enterprise Resource Planning)
    - sistema centralizzato che integra tutte le fonti di dati in un unico database (virtuale?)

3. MIS (Management Information Systems)
    - standardized and fixed reporting systems built on existing OLTP
    - Provides structured, routine information for reporting and monitoring purposes
    - Serve per prendere **decisioni strutturate**
        - decisioni ripetitive e di routine per cui so già quali dati mi servono e che cosa ci devo fare
        - Esempio (magazzino)
            - Decisione: riordinare o no un prodotto
            - Procedimento noto:
                - leggo quantità in magazzino
                - confronto con la soglia minima
                - se quantità < soglia → riordino
                - altrimenti → non faccio nulla

4. DSS (Decision Support Systems)
    - interactive and user-friendly analytical system
        - serve a fare (what-if) analisi per capire che cosa potrebbe succedere prendendo una certa decisione
        - utilizza i dati per produrre modelli, simulazioni, ...
    - provides support for complex and **unstructured decisions**
        - decisioni poco frequenti per cui non so quali dati mi servono e come processarli
        - esempio (nuovo mercato)
            - Decisione: entrare o no in un nuovo mercato
            - quali dati userò? (vendite? concorrenza? rischi politici?)
            - quali pesano di più?
            - che modello applico?
            - esiste una soglia “giusta”?
            - Non c’è una sequenza fissa di passi, il procedimento si costruisce mentre si analizza il problema

**NB**: to enable structured and unstructured decisions in a data-driven way, we usually use:

- analytics for structured decisions
- data mining for unstructured decisions
  - through data mining we could also obtain insights to define new structured decisions (pensa di nuovo ad association rules)

5. EIS (Executive Information Systems)
    - integrano insieme MIS e DSS per decisioni di alto livello

## Buisness Intelligence (BI)

con Buisness Intelligence si intende l'unione di quanto elencato sopra

- BI integrates across all these, providing a unified platform that collects ERP data (and data from other sources), automates MIS reporting, enables DSS-style analysis, and presents EIS-level dashboards

## OLAP based systems

OLAP (On-Line Analytical Processing) technology is meant to allow an interactive analysis of multidimensional data from multiple perspectives.

- analyzing something from multiple perspectives example:
  - we can think of a manager from a company that sells goods, they might want to look at the sales trends
    - from the perspective of time
    - or along a geographical dimension
    - or based on the type of goods that are sold.

`Data Warehouse (DWH)`

A central piece of BI and OLAP technologies is called data warehouse: a copy of transaction data specifically structured for query and analysis

- a DWH extracts data from their sources, puts them in an intermediate area (staging), integrates it and gives it structure
- vedremo meglio dopo in che cosa consiste una DWH

# Big Data and Data mining

We can define big data as: `a collection of data so large and/or complex and/or fast changing that they are difficult to process using traditional DBMS or data processing applications.`

This huge amount of data is being generated today by:

- organizations
  - come sempre
- machines (e.g. IoT devices, sensors, e-commerce sites, wearable devices, …)
  - industria 4.0, agritech, smart cities, ...
- people (e.g. social media: Facebook, WhatsApp, YouTube, …)

The issue with big data is how to **extract value** from such massive amounts, as we need to:

- Process the growing VOLUME of data in a cost-efficient way
- Respond to the increasing VELOCITY of data generation
- Collectively analyze the broadening VARIETY of data
  - dati provenienti da sorgenti diverse possono avere:
    - struttura diversa: structured, unstructured, semi-structured
    - formati diversi per le stesse informazioni -> preprocessing, data cleaning
    - granularità diverse -> feature engineering
    - ...

These are the three Vs of big data

It is also important to introduce a high-level taxonomy of data, dividing it in three categories:

- Structured data:
  - data with a fixed schema (e.g. relational tables, spreadsheets or data which could easily fit in them).
- Semi-structured data:
  - data that may have a schema but that could also change over time (e.g. XML, JSON).
- Unstructured data:
  - data that does not have an associated data model, making up roughly 80% of the total available data (e.g. audio, images and videos).

**To solve big data issues we need data mining**

We refer to data mining as an iterative discovery process that allows us to extract insights ( == knowledge == value) from big data.

- We start from data sources that could be either internal or external to our organization
- we store this data in a more or less structured storage facility, like data warehouses or data lakes
- by selecting interesting data and preprocessing it we obtain high-quality prepared data
- We can now use machine learning to find patterns and models that we can interpret and evaluate in order to gain knowledge.
- This will allow us to take actions, which will then be measured and adjusted.

In questo senso:

- data mining is a discovery **process** of knowledge hidden in data
- machine learning for data mining refers to algorythms and statistical models to derive patterns and models from the data
  - it's the algorythmic part of the data mining process

---

# Differenze tra data mining e machine learning (chatgpt stuff)

### 🔹 Data Mining come processo

- **Data mining** non è solo applicare un algoritmo, ma un **processo più ampio di scoperta di conoscenza** (spesso inserito nel ciclo KDD – *Knowledge Discovery in Databases*).
- Include diverse fasi:

  1. Raccolta e preparazione dei dati (pulizia, integrazione, trasformazione).
  2. Scoperta di pattern, regole, relazioni.
  3. Interpretazione e valutazione dei risultati.
  4. Traduzione in **conoscenza utile e azionabile** (decisioni, strategie, applicazioni).

👉 Quindi data mining = *framework concettuale* per “tirare fuori valore dai dati”.

### 🔹 Machine Learning dentro il Data Mining

- **Machine learning** fornisce gli **strumenti matematici e algoritmici** per individuare e apprendere i pattern nascosti.
- In altre parole:

  - Data mining = il *processo di scoperta*.
  - Machine learning = l’insieme di *tecniche* usate per fare la parte centrale del lavoro (estrazione di regole, modelli predittivi, clustering, ecc.).

👉 Non tutti i metodi di data mining usano machine learning (alcuni usano statistiche classiche o regole euristiche), ma oggi ML è spesso il cuore del processo.

### 🔹 Esempio pratico

- **Data mining (processo)**:
  Un’azienda vuole capire i comportamenti dei clienti per ottimizzare le campagne di marketing.
- **Machine learning (tecniche)**:
  - Usa clustering per segmentare i clienti in gruppi.
  - Usa classificazione per prevedere chi risponderà a una campagna.
  - Usa regole di associazione per scoprire quali prodotti vengono comprati insieme.
- **Data mining (valore finale)**:
  Trasforma i risultati in azioni concrete → campagne mirate, offerte personalizzate, ottimizzazione del catalogo.

## 🔹 1. Data mining include machine learning (ma non solo)

- **Data mining** è un processo più ampio: parte dalla raccolta dei dati, passa per la loro preparazione e analisi, e arriva alla scoperta di conoscenza utile.
- Per l’analisi e la scoperta di pattern può usare **machine learning**, ma anche:

  - tecniche statistiche tradizionali,
  - metodi di visualizzazione ed esplorazione interattiva,
  - regole euristiche (es. algoritmi per *market basket analysis*).

👉 Quindi **ML è uno strumento del data mining, ma non l’unico**.

## 🔹 2. Machine learning può servire per data mining (ma non solo)

- **Machine learning** nasce per far apprendere modelli dai dati.
- Una parte dei suoi usi è proprio nel **data mining** → scoprire pattern, classificare, raggruppare, prevedere.
- Ma il suo campo è più vasto:

  - **Computer vision**: riconoscere volti, oggetti, scene.
  - **Natural Language Processing**: traduzione automatica, chatbot, sentiment analysis.
  - **Reinforcement learning**: robot, auto a guida autonoma, agenti che prendono decisioni in ambienti complessi.
  - **Generative AI**: modelli che creano testo, immagini, musica, codice (come me!).

👉 Quindi **ML può essere usato per data mining, ma va molto oltre**.
