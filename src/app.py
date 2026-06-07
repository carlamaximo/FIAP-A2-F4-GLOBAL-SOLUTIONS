import streamlit as st
import plotly.express as px

from database import criar_tabela, salvar_analise, listar_analises
from ml_model import treinar_modelo, prever_fadiga, calcular_risco_operacional
from video_analysis import salvar_video, detectar_movimento_com_opencv, calcular_distancia, calcular_velocidade_media
from report_generator import AstroMindAI


st.set_page_config(
    page_title="AstroMind AI",
    page_icon="🚀",
    layout="wide"
)


criar_tabela()
modelo = treinar_modelo()


st.title("🚀 AstroMind AI")
st.subheader("Monitoramento Inteligente de Fadiga em Astronautas")

st.write("""
O AstroMind AI é uma Prova de Conceito para análise de fadiga e risco operacional
em astronautas ou operadores atuando em ambientes extremos, como simulações lunares,
missões orbitais, bases remotas e treinamentos espaciais.
""")


st.sidebar.header("Dados da missão")

astronauta = st.sidebar.text_input("Nome do astronauta/operador")

missao = st.sidebar.selectbox(
    "Tipo de missão",
    [
        "Simulação lunar",
        "Treinamento orbital",
        "Base remota",
        "EVA simulada",
        "Missão em ambiente extremo"
    ]
)

ambiente = st.sidebar.selectbox(
    "Ambiente operacional",
    [
        "Terra",
        "Lua",
        "Marte",
        "Microgravidade",
        "Ambiente extremo simulado"
    ]
)

bpm = st.sidebar.number_input(
    "Frequência cardíaca BPM",
    min_value=60,
    max_value=220,
    value=150
)

temperatura = st.sidebar.number_input(
    "Temperatura do ambiente/traje °C",
    min_value=-50,
    max_value=80,
    value=25
)

oxigenio = st.sidebar.number_input(
    "Nível de oxigênio %",
    min_value=0,
    max_value=100,
    value=95
)


st.header("Upload do vídeo da simulação")

video = st.file_uploader(
    "Envie um vídeo em formato MP4",
    type=["mp4"]
)


if video:
    st.video(video)

    if st.button("Analisar missão"):

        if not astronauta:
            st.warning("Informe o nome do astronauta/operador antes de analisar.")
        else:
            with st.spinner("Processando vídeo e analisando dados da missão..."):

                caminho_video = salvar_video(video)

                posicoes = detectar_movimento_com_opencv(caminho_video)

                distancia = calcular_distancia(posicoes)

                velocidade = calcular_velocidade_media(distancia)

                fadiga = prever_fadiga(
                    modelo,
                    velocidade,
                    distancia,
                    bpm,
                    temperatura,
                    oxigenio
                )

                risco = calcular_risco_operacional(
                    fadiga,
                    bpm,
                    temperatura,
                    oxigenio
                )

                gerador = AstroMindAI()

                relatorio = gerador.gerar_relatorio(
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
                )

                salvar_analise(
                    astronauta,
                    missao,
                    ambiente,
                    distancia,
                    velocidade,
                    bpm,
                    temperatura,
                    oxigenio,
                    fadiga,
                    risco,
                    relatorio
                )

            st.success("Análise concluída com sucesso!")

            col1, col2, col3 = st.columns(3)

            col1.metric("Fadiga prevista", fadiga)
            col2.metric("Risco operacional", risco)
            col3.metric("Velocidade média", f"{velocidade:.2f} px/s")

            st.subheader("Relatório operacional")
            st.text(relatorio)


st.header("Histórico de análises")

df = listar_analises()

if df.empty:
    st.info("Nenhuma análise registrada ainda.")
else:
    st.dataframe(df)

    st.subheader("Dashboards inteligentes")

    fig_velocidade = px.line(
        df,
        x="id",
        y="velocidade",
        title="Evolução da velocidade estimada"
    )
    st.plotly_chart(fig_velocidade, use_container_width=True)

    fig_bpm = px.line(
        df,
        x="id",
        y="bpm",
        title="Evolução da frequência cardíaca"
    )
    st.plotly_chart(fig_bpm, use_container_width=True)

    fig_fadiga = px.histogram(
        df,
        x="fadiga",
        title="Distribuição dos níveis de fadiga"
    )
    st.plotly_chart(fig_fadiga, use_container_width=True)

    fig_risco = px.histogram(
        df,
        x="risco",
        title="Distribuição dos riscos operacionais"
    )
    st.plotly_chart(fig_risco, use_container_width=True)