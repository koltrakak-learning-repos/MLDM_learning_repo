# conceptual modeling | Dimensional Fact Model

We want to start modeling the data (at a very high level) in order to store it in the data warehouse and to discuss the various hierarchies, features, ..., measures needed by the business owners.

The DFM is a conceptual model created specifically to function as data mart design support (serve a modellare i dati da mettere in un datamart). It is based on the multidimensional model.

- strumento simile ad E/R in quanto conceptual model
- più adatta per DW dato che si adatta al modello dell'analisi multidimensionale con data cube (ci sono attributi che sono misure e attributi che sono dimensioni)

## DFM Concepts

- Fact -> cosa succede?
  - something that happens in the real world
  - It is a concept relevant to decision-making processes.
  - It typically models a set of events taking place within
  - es: Sales, purchases, orders

- Measure -> quanto?
  - It is a numerical property of a fact and describes a quantitative aspect that is relevant to analysis.
  - es: Quantity, revenue, discount

- Dimension -> secondo quale prospettiva?
  - It is a property of a fact with a **finite and discrete domain** that describes the fact from a particular point of view
  - Date, product, store

- Dimensional Attribute -> come descrivo una prospettiva?
  - attributes that describe dimensions, always with discrete values.

- Hierarchy
  - It is a directed tree whose nodes are dimensional attributes and whose arcs model **many-to-one associations between dimensional attribute pairs.**
    - il lato 1 è quello più vicino al fatto;
    - es: Date → Month → Year
      - per ogni data abbiamo un solo mese, che appartiene a un solo anno
  - It includes a dimension, positioned at the tree’s root and all of the dimensional attributes that describe it
  - es Date->Month->Year

skip da slide 56 in poi ...
