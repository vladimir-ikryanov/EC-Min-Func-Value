import random

# Номер у журналі групи: 9
# Мета оптимізації: min
# Інтервал для пошуку рішення: [210, 273]
RANGE_START = 210
RANGE_END = 273

# Функція пристосованості.
def fitness(x):
    return -8 - 3*x - 12*x**2 + 5*x**3

# Фукнція турніру для вибору батьківської особи
def tournament(population, fitnesses, tournament_size):
    tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
    return min(tournament, key=lambda x: x[1])[0]

# Розмір популяції
POPULATION_SIZE = 100
# Кількість поколінь
GENERATIONS = 1000
# Фактор мутації
MUTATION_RATE = 0.06
# Кількість турнірів
TOURNAMENT_SIZE = 4

# Рандомно створюємо початкову популяцію
population = [random.uniform(RANGE_START, RANGE_END) for _ in range(POPULATION_SIZE)]
print("Початкова популяція: ", population)

for gen in range(GENERATIONS):
    # Обчислюємо фукцію простосованості для особи
    fitnesses = [fitness(individual) for individual in population]
    next_population = []
    for _ in range(POPULATION_SIZE):
        # Обираємо батьківські особи для схрещення
        parent1 = tournament(population, fitnesses, TOURNAMENT_SIZE)
        parent2 = tournament(population, fitnesses, TOURNAMENT_SIZE)
        # Проводимо схрещення
        child = (parent1 + parent2) / 2
        # Застосовуємо мутацію
        child += random.uniform(-MUTATION_RATE, MUTATION_RATE)
        # Зводимо дитину до заданого інтервалу
        child = max(min(child, RANGE_END), RANGE_START)
        # Додаємо до наступної популяції
        next_population.append(child)
    # Робимо наступну популяцію поточною
    population = next_population

print("Популяція після 1000 поколінь: ", population)
print()
# Показуємо значення найкращої особи у фінальній популяції
best_individual = min(population, key=fitness)
print("Найкращя особа у популяції: ", best_individual)
print("Значення функції пристосованості для особи: ", fitness(best_individual))
