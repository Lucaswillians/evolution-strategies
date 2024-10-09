import numpy as np

# Função objetivo: calcula a soma dos quadrados dos elementos do vetor.
def objective_function(vector):
    return np.sum(np.square(vector))

# Gera um vetor aleatório dentro dos limites fornecidos.
def random_vector(minmax):
    return np.array([np.random.uniform(low, high) for low, high in minmax])

# Gera um número aleatório com distribuição gaussiana (normal).
def random_gaussian(mean=0.0, stdev=1.0):
    while True:
        u1 = np.random.uniform(0, 1)  # Gera um número aleatório u1 entre 0 e 1
        u2 = np.random.uniform(0, 1)  # Gera um número aleatório u2 entre 0 e 1
        w = u1 * u1 + u2 * u2  # Calcula a soma dos quadrados
        if w < 1:  # Verifica se w é menor que 1 para continuar
            break
    # Calcula a variável aleatória usando a transformação Box-Muller
    w = np.sqrt(-2.0 * np.log(w) / w)
    return mean + (u2 * w) * stdev  # Retorna o número aleatório com média e desvio padrão especificados

# Realiza a mutação do vetor, garantindo que os valores estejam dentro do espaço de busca.
def mutate_problem(vector, stdevs, search_space):
    child = np.zeros_like(vector)  # Cria um vetor filho inicializado com zeros
    for i, v in enumerate(vector):
        # Adiciona uma perturbação ao valor do vetor original, usando uma distribuição gaussiana
        child[i] = v + stdevs[i] * random_gaussian()
        # Restringe o valor dentro do espaço de busca
        if child[i] < search_space[i][0]:
            child[i] = search_space[i][0]  # Clampa o valor ao limite inferior
        elif child[i] > search_space[i][1]:
            child[i] = search_space[i][1]  # Clampa o valor ao limite superior
    return child  # Retorna o vetor mutado

# Ajusta a estratégia de mutação com base na variabilidade dos padrões.
def mutate_strategy(stdevs):
    tau = np.sqrt(2.0 * len(stdevs)) ** -1.0  # Calcula tau para controlar a variância
    tau_p = np.sqrt(2.0 * np.sqrt(len(stdevs))) ** -1.0  # Calcula tau para controlar a estratégia
    # Cria um novo vetor de estratégias mutadas
    child = np.array([stdevs[i] * np.exp(tau_p * random_gaussian() + tau * random_gaussian()) 
                      for i in range(len(stdevs))])
    return child  # Retorna o novo vetor de estratégias

# Realiza a mutação de um indivíduo da população, gerando um novo filho.
def mutate(par, minmax):
    child = {}
    child['vector'] = mutate_problem(par['vector'], par['strategy'], minmax)  # Mutação do vetor
    child['strategy'] = mutate_strategy(par['strategy'])  # Mutação da estratégia
    return child  # Retorna o filho mutado

# Inicializa a população com indivíduos aleatórios.
def init_population(minmax, pop_size):
    # Cria um vetor de estratégias com base no espaço de busca
    strategy = np.array([(0, (high - low) * 0.05) for low, high in minmax])
    population = []  # Lista para armazenar a população
    for _ in range(pop_size):
        individual = {}
        individual['vector'] = random_vector(minmax)  # Gera um vetor aleatório para o indivíduo
        individual['strategy'] = random_vector(strategy)  # Gera uma estratégia aleatória
        individual['fitness'] = objective_function(individual['vector'])  # Avalia a aptidão do indivíduo
        population.append(individual)  # Adiciona o indivíduo à população
    return population  # Retorna a população inicializada

# Executa o algoritmo de busca, iterando por um número máximo de gerações.
def search(max_gens, search_space, pop_size, num_children):
    population = init_population(search_space, pop_size)  # Inicializa a população
    best = min(population, key=lambda x: x['fitness'])  # Encontra o melhor indivíduo da população
    
    for gen in range(max_gens):
        # Gera filhos mutantes a partir dos indivíduos da população
        children = [mutate(population[i], search_space) for i in range(num_children)]
        # Avalia a aptidão de cada filho
        for child in children:
            child['fitness'] = objective_function(child['vector'])
        
        # Une filhos e população
        union = children + population
        # Atualiza o melhor indivíduo se encontrado um com melhor aptidão
        best = min(union, key=lambda x: x['fitness'])
        # Seleciona os melhores indivíduos para a nova geração
        population = sorted(union, key=lambda x: x['fitness'])[:pop_size]

        # Imprime a evolução do melhor indivíduo em cada geração
        print(f" > gen {gen}, fitness={best['fitness']}")
    
    return best  # Retorna o melhor indivíduo encontrado

# Executa o programa principal
if __name__ == "__main__":
    # Configuração do problema
    problem_size = 2  # Define o tamanho do problema
    search_space = [(-5, 5) for _ in range(problem_size)]  # Define o espaço de busca

    # Configuração do algoritmo
    max_gens = 100  # Número máximo de gerações
    pop_size = 30  # Tamanho da população
    num_children = 20  # Número de filhos gerados por geração

    # Executa o algoritmo
    best = search(max_gens, search_space, pop_size, num_children)
    # Exibe a melhor solução encontrada
    print(f"done! Solution: f = {best['fitness']}, s = {best['vector']}")
