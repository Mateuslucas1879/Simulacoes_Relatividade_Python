import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Constantes

c= 3e8 # velocidade da luz
g = 9.80 # aceleração da gravidade
R_terra = 6.371e6 # raio da Terra (m)

# Função para a dilatação do tempo
def dilatacao_temporal(velocidade, tempo_terra):
    fator_lorentz = np.sqrt(1-(velocidade**2/c**2))
    tempo_satelite = tempo_terra * fator_lorentz
    return tempo_satelite, fator_lorentz

# Função para a correção gravitacional
def correcao_gravitacional(altura,tempo_terra):
    fator_gravitacional = 1 + (g*altura) / (c**2)
    tempo_gravitacional = tempo_terra * fator_gravitacional
    return tempo_gravitacional,fator_gravitacional

# Função para cálculo total de tempo
def calcular_diferenca_total(velocidade, altura, tempo_terra):
    tempo_rr, fator_lorentz = dilatacao_temporal(velocidade, tempo_terra)
    tempo_gravitacional, fator_gravitacional = correcao_gravitacional(altura, tempo_terra)

    diferenca_total = (tempo_rr + tempo_gravitacional) - tempo_terra
    return diferenca_total, fator_lorentz, fator_gravitacional


# Exemplo: Parâmetros de um satélite GPS
velocidade_satelite = 3.87e3  # Velocidade média do satélite
altura_satelite = 2.0e7 # Altura do satélite
tempo_terra = 1 # Tempo na Terra em segundos

# Cálculo dos efeitos relativísticos
diferenca_tempo, fator_lorentz, fator_gravitacional = calcular_diferenca_total(velocidade_satelite, altura_satelite, tempo_terra)

# Exibição dos resultados
print(f"Fator de Lorentz (RR - Relatividade Restrita): {fator_lorentz:.10f}")
print(f"Fator Gravitacional (RG - Relatividade Geral): {fator_gravitacional:.10f}")
print(f"Diferença total de tempo no satélite comparado à Terra: {diferenca_tempo:.10f} segundos")

# Visualização gráfica da diferença de tempo em relação à altura e velocidade do satélite
alturas = np.linspace(1e7,3e7,100)
velocidade = np.linspace(1e3,1e4,100)

# Cálculo da dilatação do tempo e correção gravitacional
tempos_rr = [dilatacao_temporal(v, tempo_terra)[0] for v in velocidade]
tempos_gravitacional = [correcao_gravitacional(h, tempo_terra)[0] for h in alturas]
diferencas_totais = [calcular_diferenca_total(v, altura_satelite, tempo_terra)[0] for v in velocidade]

# Gráficos
plt.figure(figsize=(12, 6))


# Gráfico da Dilatação Temporal (Relatividade Restrita)
plt.subplot(1, 3, 1)
plt.plot(velocidade / 1e3, tempos_rr, label="Dilatação (RR)", color='b')
plt.xlabel('Velocidade do Satélite (km/s)')
plt.ylabel('Tempo dilatado (s)')
plt.title('Dilatação Temporal - Relatividade Restrita')
plt.grid(True)
plt.legend()

# Gráfico da Correção Gravitacional (Relatividade Geral)
plt.subplot(1, 3, 2)
plt.plot(alturas / 1e6, tempos_gravitacional, label="Correção (RG)", color='g')
plt.xlabel('Altura do Satélite (x10⁶ m)')
plt.ylabel('Tempo corrigido (s)')
plt.title('Correção Gravitacional - Relatividade Geral')
plt.grid(True)
plt.legend()

# Gráfico da Diferença Total de Tempo
plt.subplot(1, 3, 3)
plt.plot(velocidade / 1e3, diferencas_totais, label="Diferença Total de Tempo", color='r')
plt.xlabel('Velocidade do Satélite (km/s)')
plt.ylabel('Diferença Total (s)')
plt.title('Diferença Total de Tempo (RR + RG)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


### CONCLUSÃO

# O primeiro gráfico mostra como o tempo desacelera para o satélite à medida que sua velocidade aumenta.
# Quanto mais próximo o satélite estiver da velocidade da luz, maior será o efeito de dilatação temporal.
# A linha azul representa o tempo no satélite em função da velocidade.


# O segundo gráfico mostra o efeito da gravidade na passagem do tempo.
# A gravidade é mais fraca em maiores altitudes, o que faz com que o tempo passe mais rapidamente nos satélites.
# A linha verde mostra a correção gravitacional que precisa ser feita para compensar o tempo avançando
# mais rápido no satélite conforme ele se afasta da Terra.


# O terceiro grafico combina ambos os efeitos e mostra a diferença total de tempo entre o satélite e a Terra.

# A linha vermelha representa o resultado final, ou seja,
# quanto o tempo no satélite difere do tempo na Terra com base na velocidade.


# Esses gráficos são importantes para entender como a física relativística afeta a precisão do sistema GPS,
# já que sem essas correções, o tempo medido pelos satélites e na Terra ficaria fora de sincronia,
# causando grandes erros no cálculo de posicionamento