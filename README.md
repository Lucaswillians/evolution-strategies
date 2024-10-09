# Algoritmo de Otimização por Evolução

Este projeto implementa um algoritmo de otimização baseado em estratégias evolutivas. O objetivo é minimizar uma função objetiva, que neste caso é a soma dos quadrados dos elementos de um vetor. O algoritmo utiliza mutações para explorar o espaço de busca e encontrar soluções eficientes.

## Tabela de Conteúdos

- [Descrição do Algoritmo](#descrição-do-algoritmo)
- [Como Funciona](#como-funciona)
- [Exemplo de Saída](#exemplo-de-saída)

## Descrição do Algoritmo

O algoritmo é uma implementação básica de otimização estocástica que utiliza mutações para explorar soluções em um espaço de busca contínuo. As principais etapas do algoritmo são:

1. **Inicialização da População**: Criação de uma população de vetores aleatórios dentro de um espaço de busca definido.
2. **Avaliação da Aptidão**: Cálculo da aptidão de cada vetor usando uma função objetiva, que neste caso é a soma dos quadrados dos elementos.
3. **Mutação**: Geração de novos vetores (filhos) a partir dos vetores existentes (pais) por meio de perturbações aleatórias. As perturbações são baseadas em distribuições gaussianas.
4. **Seleção**: Combinação dos vetores filhos e pais, seguida pela seleção dos melhores indivíduos para a próxima geração.
5. **Iteração**: Repetição das etapas de mutação e seleção por um número pré-definido de gerações.

## Como Funciona

O algoritmo é dividido em várias funções principais:

- `objective_function(vector)`: Calcula a soma dos quadrados dos elementos do vetor.
- `random_vector(minmax)`: Gera um vetor aleatório dentro dos limites especificados.
- `random_gaussian(mean=0.0, stdev=1.0)`: Gera um número aleatório com distribuição gaussiana.
- `mutate_problem(vector, stdevs, search_space)`: Aplica mutações ao vetor e garante que os novos valores permaneçam dentro do espaço de busca.
- `mutate_strategy(stdevs)`: Ajusta a estratégia de mutação com base na variabilidade das perturbações.
- `init_population(minmax, pop_size)`: Inicializa a população com vetores e estratégias aleatórias.
- `search(max_gens, search_space, pop_size, num_children)`: Executa o algoritmo de busca por um número máximo de gerações.

## Exemplo de saída

<img width="382" alt="Captura de Tela 2024-10-08 às 21 07 36" src="https://github.com/user-attachments/assets/5775a83b-9e22-48c7-90ec-ec97c6752241">


