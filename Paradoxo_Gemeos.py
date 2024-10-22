import numpy as np
import matplotlib.pyplot as plt

# Constantes
c = 3e8  # Velocidade da luz

# Função para calcular a dilatação temporal (fator de Lorentz)
def dilatacao_do_tempo(velocidade, tempo_terra):
    fator_lorentz = np.sqrt(1 - (velocidade**2 / c**2))
    tempo_gemeo_espaco = tempo_terra * fator_lorentz
    return tempo_gemeo_espaco

# Função para calcular a diferença de idade entre os gêmeos
def paradoxo_gemeos(velocidade, tempo_terra):
    tempo_gemeo_espaco = dilatacao_do_tempo(velocidade, tempo_terra)
    diferenca_idade = tempo_terra - tempo_gemeo_espaco
    return diferenca_idade, tempo_gemeo_espaco

# Parâmetros: Viagem de 10 anos na Terra
tempo_terra = 10  # Tempo medido na Terra (em anos)
velocidades = np.linspace(0, 0.99 * c, 100)  # Velocidades de 0 a 99% da velocidade da luz

# Cálculos de diferenças de idade e tempos percebidos pelo gêmeo no espaço
diferencas_idade = []
tempos_gemeo_espaco = []
for v in velocidades:
    diferenca, tempo_espaco = paradoxo_gemeos(v, tempo_terra)
    diferencas_idade.append(diferenca)
    tempos_gemeo_espaco.append(tempo_espaco)

# Gráfico aprimorado
plt.figure(figsize=(10,6))
plt.plot(velocidades / c, diferencas_idade, label="Diferença de idade (gêmeo na Terra - gêmeo no espaço)", color='b')
plt.plot(velocidades / c, tempos_gemeo_espaco, label="Tempo percebido pelo gêmeo no espaço", color='g')
plt.axhline(y=tempo_terra, color='r', linestyle='--', label="Tempo na Terra (10 anos)")

# Detalhes do gráfico
plt.xlabel('Fração da velocidade da luz (v/c)', fontsize=12)
plt.ylabel('Tempo (anos)', fontsize=12)
plt.title('Paradoxo dos Gêmeos: Diferença de Idade e Tempo Percebido', fontsize=14)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True)

# Exibição do gráfico
plt.tight_layout()
plt.show()


#EXPLICAÇÔES
# Diferença de Idade (linha azul): Mostra como a diferença de envelhecimento entre os gêmeos aumenta conforme
# a velocidade do gêmeo viajante se aproxima da velocidade da luz.

# Tempo Total na Terra (linha vermelha): Mostra o tempo total que passou na Terra, que é o mesmo em todas as velocidades.

# Tempo Total no Espaço (linha verde): Mostra como o tempo percebido pelo gêmeo no espaço
# desacelera à medida que ele viaja em velocidades mais altas.