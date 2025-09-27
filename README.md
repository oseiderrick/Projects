# Warehouse Simulator (Java)

A small Java project that simulates a warehouse with perishable and
non-perishable items, priority based shipping by earliest expiry, and a
generic dynamic queue implemented from scratch. Includes a simple CLI
with a ticking "day" timer that automatically ages inventory and flags
items that are close to expiring.

------------------------------------------------------------------------

Why this project is interesting

-   Realistic constraints: Perishables lose value over time and can
    expire; shipping prefers items that will expire sooner.
-   Algorithms and data structures: Custom dynamic queue
    (`dynamic_Queue<T>`) with circular buffer and auto-resize plus
    PriorityQueue with a Comparator for time-to-expiry.
-   OOP modeling: Item → PerishableItem/NonPerishableItem, concrete
    items like Chips and Rice with randomized shelf life.
-   Systems thinking: A timer advances the simulation (days pass),
    triggers near-expiry warnings, and forces trade-offs.

------------------------------------------------------------------------

Project structure

    src/
    └─ warehouse-sim
       ├─ Item.java                 # Base product entity
       ├─ PerishableItem.java       # Adds expireInDays, price logic
       ├─ NonPerishableItem.java    # Static registry example
       ├─ Chips.java                # Perishable example (random expiry)
       ├─ Rice.java                 # Perishable example (random expiry)
       ├─ DateComparator.java       # Compare perishables by expireInDays
       ├─ dynamic_Queue.java        # Generic, resizing queue (from scratch)
       └─ Warehouse.java            # CLI, timer, inventory ops, main()

The current package is `prob2`. If you place these under `src/prob2`,
the commands below will work as-is.

------------------------------------------------------------------------

Key features

-   Buy inventory via CLI (perishable and non-perishable)
-   View inventory grouped by type
-   Auto-aging and warnings: A timer advances "days" and prints
    near-expiry alerts (e.g., ≤ 5 days left)
-   Process expired items (remove or zero-value)
-   Priority shipping: Ships earliest-expiring perishables first using
    PriorityQueue and DateComparator
-   Custom data structure: dynamic_Queue`<T>`{=html} (enqueue/dequeue,
    resize, circular indexing)

------------------------------------------------------------------------

How to run

``` bash
# From the repo root
mkdir -p out
javac -d out src/prob2/*.java
java -cp out prob2.Warehouse
```

You'll see a menu like:

    --- Warehouse Inventory System ---
    1. Buy Inventory
    2. View Current Inventory
    3. Process Expired Items
    4. Ship Items
    5. Exit
    6. Pause Simulation
    7. Resume Simulation
    Enter your choice (1-5):

Use 6/7 to pause/resume the "day" timer while adding or shipping items.

------------------------------------------------------------------------

Design notes

-   Perishable pricing: PerishableItem#getPrice() returns 0 once
    expired; otherwise defers to Item price.
-   Expiry modeling: DateComparator sorts by expireInDays to ensure FIFO
    by soonest expiry.
-   Dynamic queue: dynamic_Queue`<T>`{=html} demonstrates manual memory
    management patterns (resize/double capacity, modulo indices,
    underflow checks).

------------------------------------------------------------------------

Possible improvements

-   Persist inventory to a file or database between runs
-   Add JUnit tests for the queue and comparator behavior
-   Track costs and revenue to compute profit over time
-   Replace random expiry with seeded generation for reproducible demos
-   Add CSV import/export for bulk inventory

------------------------------------------------------------------------

License

MIT
