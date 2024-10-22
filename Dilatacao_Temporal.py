import numpy as np
import matplotlib.pyplot as plt

# Constantes
c = 3e8  # Velocidade da luz

# Função para calcular a dilatação temporal
def dilatacao_do_tempo(velocidade, tempo_terra):
    fator_lorentz = np.sqrt(1 - (velocidade**2 / c**2))
    tempo_objeto = tempo_terra * fator_lorentz
    return tempo_objeto

# Função para plotar e melhorar a visualização
def plot_dilatacao_temporal(velocidades, tempos_objeto, tempo_terra, unidade_tempo="dias"):
    # Gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(velocidades/c, tempos_objeto, label=f"Tempo no objeto ({unidade_tempo})", color='blue', lw=2)
    plt.axhline(y=tempo_terra, color='red', linestyle='--', label=f"Tempo na Terra ({unidade_tempo})", lw=2)

    # Adiciona anotações no gráfico
    v_especifico = 0.8 * c  # Escolher uma velocidade específica (80% da velocidade da luz)
    tempo_especifico = dilatacao_do_tempo(v_especifico, tempo_terra)
    plt.scatter([v_especifico/c], [tempo_especifico], color='green', zorder=5)
    plt.annotate(f"Velocidade = 80% da luz\nTempo = {tempo_especifico:.2f} {unidade_tempo}",
                 xy=(v_especifico/c, tempo_especifico),
                 xytext=(v_especifico/c - 0.1, tempo_especifico + 0.1*tempo_terra),
                 arrowprops=dict(facecolor='black', arrowstyle="->", lw=1.5))

    # Configurações do gráfico
    plt.xlabel('Fração da velocidade da luz (v/c)', fontsize=12)
    plt.ylabel(f'Tempo percebido ({unidade_tempo})', fontsize=12)
    plt.title(f'Dilatação Temporal Relativística ({unidade_tempo})', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True)
    plt.show()

# Parâmetros de uso
tempo_terra = 365  # Tempo na Terra
unidade_tempo = "dias"  # Unidades para o tempo

# Configurando velocidades de 0 até 99% da velocidade da luz
velocidades = np.linspace(0, 0.99 * c, 100)

# Calculando os tempos dilatados
tempos_objeto = [dilatacao_do_tempo(v, tempo_terra) for v in velocidades]

# Plotando os resultados
plot_dilatacao_temporal(velocidades, tempos_objeto, tempo_terra, unidade_tempo)

#CONCLUSÂO

# O gráfico ilustra como, à medida que a velocidade se aproxima da velocidade da luz,
# o tempo percebido pelo objeto desacelera drasticamente em comparação com o tempo na Terra.
#A linha pontilhada vermelha mostra o tempo na Terra, que permanece constante independentemente da velocidade.
# A curva azul mostra como o tempo se dilata para o objeto que viaja em velocidades relativísticas.