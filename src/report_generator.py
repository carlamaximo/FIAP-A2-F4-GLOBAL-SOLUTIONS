class AstroMindAI:

    def gerar_relatorio(
        self,
        astronauta,
        missao,
        ambiente,
        distancia,
        velocidade,
        bpm,
        temperatura,
        oxigenio,
        fadiga,
        risco
    ):
        texto = f"""
ASTROMIND AI - RELATÓRIO OPERACIONAL

Astronauta/Operador: {astronauta}
Missão: {missao}
Ambiente: {ambiente}

DADOS ANALISADOS:
- Distância estimada no vídeo: {distancia:.2f} px
- Velocidade média estimada: {velocidade:.2f} px/s
- Frequência cardíaca: {bpm} bpm
- Temperatura do ambiente/traje: {temperatura} °C
- Nível de oxigênio: {oxigenio} %

RESULTADO DA IA:
- Nível de fadiga previsto: {fadiga}
- Risco operacional: {risco}

RECOMENDAÇÕES:
"""

        if risco == "Crítico":
            texto += """
- Interromper imediatamente a atividade simulada.
- Acionar equipe de suporte da missão.
- Verificar sinais fisiológicos e condições do traje.
- Reduzir exposição ao ambiente extremo.
"""

        elif risco == "Alto":
            texto += """
- Reduzir a intensidade da atividade.
- Monitorar frequência cardíaca e oxigênio continuamente.
- Avaliar necessidade de pausa operacional.
- Reforçar acompanhamento da equipe de controle.
"""

        elif risco == "Médio":
            texto += """
- Manter o astronauta em observação.
- Controlar ritmo da atividade.
- Reavaliar dados fisiológicos nos próximos minutos.
"""

        else:
            texto += """
- Condição operacional estável.
- Manter rotina planejada.
- Continuar monitoramento preventivo.
"""

        texto += """

OBSERVAÇÃO:
Este sistema é uma Prova de Conceito acadêmica. Os dados fisiológicos podem ser simulados e o modelo de Machine Learning foi treinado com uma base fictícia para demonstrar a arquitetura da solução.
"""

        return texto