# Bootcamp Exercises

## Week 1

### Exercise 1: Deck of Cards

Build a Deck class that:

- Represents a standard 52-card deck
- Implements __len__ to return 52
- Implements __getitem__ to allow indexing and slicing
- Can be shuffled using random.shuffle()
- Can be iterated over with a for loop

### Exercise 2: 2D Vector Class

Create a 2D Vector class that:

- Implements __repr__ for debugging
- Implements __str__ for user display
- Implements __add__ for vector addition
- Implements __mul__ for scalar multiplication
- Implements __abs__ for vector magnitude

## Week 2

### Exercise 1 - Timing Decorator

- Implement basic timing decorator
- Test on sample functions
- Add to AST Analyzer codebase

### Exercise 2 - Logging Decorator

- Implement logging decorator with configurable levels
- Support decorator arguments `(@log(level='DEBUG'))`
- Add to AST Analyzer codebase

### Exercise 3 - File Processing Generator

- Create generator for reading large files line by line
- Add filtering and processing
- Test memory efficiency vs list approach

### Exercise 4 - Retry Decorator

- Build `@retry(max_attempts=3, delay=1)` decorator
- Implement exponential backoff
- Handle specific exception types
- Test with failing functions