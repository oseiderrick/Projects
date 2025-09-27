# Chick-fill-A Food Ordering Simulator (Java)

A Java project that simulates a restaurant-style food ordering system.
Customers place orders which are managed using a custom generic dynamic
queue. The system supports adding menu items, creating orders, and
processing them in a first-come, first-served manner.

------------------------------------------------------------------------

Why this project is interesting

-   Demonstrates the use of object-oriented programming with classes
    like MenuItem and Order.
-   Implements a custom dynamic queue (enqueue, dequeue, resize,
    circular indexing).
-   Simulates real-world restaurant order processing in a console-based
    system.
-   Combines algorithmic thinking with a practical application domain.

------------------------------------------------------------------------

Project structure

    src/
    └─ Chick-Fil-A/
       ├─ MenuItem.java             # Represents food menu items
       ├─ order.java                # Represents an order placed by a customer
       ├─ dynamic_Queue.java        # Generic, resizing queue implementation
       └─ food_ordering_system.java # CLI driver program with main()

The current package is `prob2`. Place these under `src/prob2` for
compilation.

------------------------------------------------------------------------

Key features

-   Add menu items with name and price
-   Place orders containing menu items
-   Manage all orders in a dynamic queue
-   Process orders in FIFO order
-   Console-based user interface with menu options

------------------------------------------------------------------------

How to run

``` bash
# From the repo root
mkdir -p out
javac -d out src/prob2/*.java
java -cp out prob2.food_ordering_system
```

------------------------------------------------------------------------

Design notes

-   Uses a reusable dynamic_Queue`<T>`{=html} class to handle incoming
    orders.
-   Orders can contain multiple MenuItems, enabling simple cart-like
    functionality.
-   Highlights how data structures support real-world workflows.

------------------------------------------------------------------------

Possible improvements

-   Add persistence to save menu and orders between runs
-   Track total revenue and statistics
-   Add JUnit tests for queue and order processing
-   Expand to support priority orders (e.g., VIP, delivery vs dine-in)
-   Build a GUI or web front-end

------------------------------------------------------------------------

License

MIT
