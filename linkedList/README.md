LINKED LIST

What is a linked list?
- A linked list is a collection of information located in non-consecutive memory.

Why is it useful?
- The primary strength of a linked list comes from the way its information is stored. The items in a linked list are stored with references to one another spread across non-consecutive memory. This makes it more memory efficient than arrays, which rely on consecutive memory chunks.

What is non-consecutive-memory?
- Non-consecutive memory is exactly that, memory chunks that are not necessarily adjacent to one another.

Types of linked lists
- Singly
  - One directional. Each item contains a reference to the next item in the list.
  - Useful for first-in-first-out applications such as purchase orders or notification systems; applications in which order matters.
- Doubly
  - Bi-directional. Each item contains both a reference to the next item in the list, and the previous item in the list.
  - Useful for applications in which you need to go forwards and backwards within the list. An example of this is the forward and back buttons in the browser.
- Circular
  - One directional or bi-directional. The defining characteristic here is that the last item in the list contains a reference to the first item in the list.
  - Useful in applications in which you need to traverse the list in a continuous loop. An example of this is a game of Uno. Each person goes in order, sometimes reversing, until the game is complete.

Typical features of a linked list
- As stated, items in the list reference each other.
- There is a "head" (the beginning of the list), and a "tail" (the end of the list)
- Helper information
  - size
- Helper functions
  - insert
  - insertAt
  - indexOf
  - removeElement


Code examples
- general linked list examples
- singly linked list
- doubly linked list
- circular linked list (singly)
- circular linked list (doubly, faster search for insertAt)