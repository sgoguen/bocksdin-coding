# GENETIC ALGORITHM

### Outline
1. Introduction
    - Course Outline
2. What is a "genetic algorithm"?
    - Gene
    - Combinatorial
    - Benefits
        - Able to attempt many different combinations quickly
        - Can provide multiple "optimal" solutions
        - Requires less information than some other machine learning algorithms
    - Limitations
        - Complex problem = expensive fitness function
            - Better for small pieces of a larger problem
        - "Best solution" is relative
            - Best solution it found, not necessarily best solution possible
    - Possible use cases
    - Example rundown
        - Backpack packing
    - Pieces of implementation (https://www.ripublication.com/ijcir17/ijcirv13n7_15.pdf)
        - Individual
        - Population
        - Generation
        - Constraint
        - Value to max/min
        - Fitness function
        - Recombination
            - Single point crossover
            - Two point crossover
            - Uniform crossover
            - Sinusoidal Motion crossover
        - Mutation
3. Steps
    - Define constraint
    - Define value to max/min
    - Create initial population
    - Evaluate fitness of population
    - Select parents
    - Build children
    - Mutate children
    - Create new population
    - Reveal best solution


### Backpack Packing
1. Explain scenario
    - Hiking
    - Potential items
        - value
        - weight
    - Define constraint
        - 2.5kg
    - Define value
        - Max value added
2. Create items
    - Item Class
        - Name
        - Value
        - Weight
    - List of items
3. Create individual
    - Individual class
        - Init
        - Fitness
        - Crossover
            - Single point
        - Mutation
4. Initialize Population
    - GeneticAlgorithm class
        - Calculate fitness
        - Order population
        - Select best individual
        - Initialize population
5. Recombination
    - Sum values
    - Select parent
    - Crossover
    - Mutate
7. Solve
    - Run generations
    - New population
    - Calculate fitness
    - Order population
    - Select best individual
    - Visualize Generation
    - Visualize best solution
        - Generation found
        - Item names
        - Value added
        - Weight
8. Setup for other crossovers
    - Increase item list
    - Calculate stats
        - Run 100 times
        - Average # of generations needed
        - Best solution
    - Run calc stats on single point
9. Other crossovers
    - Two Point
    - Uniform
    - Sinusoidal Motion