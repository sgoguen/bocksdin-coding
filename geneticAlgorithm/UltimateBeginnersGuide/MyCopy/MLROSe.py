import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


products = []
limit = 3

products.append(("Refrigerator A", 0.751, 999.90 ))
products.append(("Cell phone", 0.00000899, 2199.12 ))
products.append(("TV 55", 0.400, 4346.99 ))
products.append(("TV 50' ", 0.290, 3999.90 ))
products.append(("TV 42' ", 0.200, 2999.00 ))
products.append(("Notebook A", 0.00350, 2499.90 ))
products.append(("Ventilator", 0.496, 199.90 ))
products.append(("Microwave A", 0.0424, 308.66 ))
products.append(("Microwave B", 0.0544, 429.90 ))
products.append(("Microwave C", 0.0319, 299.29 ))
products.append(("Refrigerator B", 0.635, 849.00 ))
products.append(("Refrigerator C", 0.870, 1199.89 ))
products.append(("Notebook B", 0.498, 1999.90 ))
products.append(("Notebook C", 0.527, 3999.00 ))


def fitness_function(solution):
  cost = 0
  sum_space = 0

  for i in range(len(solution)):
    if solution[i] == 1:
      cost += products[i][2]
      sum_space += products[i][1]

  if sum_space > limit:
    cost = 1

  return cost

fitness = mlrose.CustomFitness(fitness_function)
problem = mlrose.DiscreteOpt(length=len(products), fitness_fn=fitness, maximize=True, max_val=2) # 0, 1

best_solution, best_fitness = mlrose.genetic_alg(problem, pop_size=20, mutation_prob=0.01)
print(best_solution)
print(best_fitness)