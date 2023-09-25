import random as rd

POPULATION_SIZE = 4		# 한 세대의 크기 (개체 집단의 크기)
MUTATION_RATE = 0.1		# 돌연변이 생성 확률
GENE_SIZE = 5			# 한 염색체의 유전자 수

SIMULATION_TIME = 10	# 세대 반복 횟수

class Chromosome :
	def __init__(self, gene = []) :
		if len(gene) == 0 :
			self.gene = [rd.randint(0, 1) for _ in range(GENE_SIZE)]
		else :
			self.gene = gene[:]

	def __str__(self) :
		return f'gene = {self.gene}, fitness = {self.get_fitness()}'
	
	def get_fitness(self) :
		x = int(''.join(map(str, self.gene)), 2)
		return x**2
	
def print_population(population) :
	for i in range(POPULATION_SIZE) :
		print(f'Chromosome #{i}. {population[i]}')

def print_generation(genCount, population) :
	population.sort(key=lambda x : -x.get_fitness())
	print(f"-- Gen #{genCount} -----")
	print_population(population)
	print()

def select_chromosome(population) :
	sum_value = sum([c.get_fitness() for c in population])
	pick = rd.randint(1, sum_value)

	cur = 0
	for c in population :
		cur += c.get_fitness()
		if pick <= cur :
			return c

def crossover_chromosome(populaion) :
	father = select_chromosome(populaion).gene
	mother = select_chromosome(populaion).gene

	cut_index = rd.randint(1, GENE_SIZE - 1)
	child1 = father[:cut_index] + mother[cut_index:]
	child2 = mother[:cut_index] + father[cut_index:]
	return child1, child2

def mutate_chromosome(chromosome) :
	for i in range(GENE_SIZE) :
		if rd.random() < MUTATION_RATE :
			chromosome.gene[i] = 0 if chromosome.gene[i] == 1 else 1


population = [Chromosome() for _ in range(POPULATION_SIZE)]
generation = 0
print_generation(generation, population)

for _ in range(SIMULATION_TIME) :
	nxt_population = []

	for _ in range(POPULATION_SIZE // 2) :
		child1, child2 = crossover_chromosome(population)
		nxt_population.append(Chromosome(child1))
		nxt_population.append(Chromosome(child2))
	
	if len(nxt_population) != POPULATION_SIZE :
		child1, child2 = crossover_chromosome(population)
		nxt_population.append(Chromosome(child1))
	
	population = nxt_population[:]

	for c in population :
		mutate_chromosome(c)

	generation += 1
	print_generation(generation, population)