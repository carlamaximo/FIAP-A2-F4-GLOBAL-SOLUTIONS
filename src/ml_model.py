import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


MODEL_PATH = "data/modelo_fadiga.pkl"


def treinar_modelo():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    dados = pd.DataFrame({
        "velocidade": [2, 3, 4, 5, 6, 7, 8, 2, 3, 5, 6, 7],
        "distancia": [300, 600, 900, 1200, 1800, 2500, 3200, 400, 700, 1500, 2200, 2800],
        "bpm": [120, 135, 150, 160, 170, 180, 190, 145, 155, 175, 185, 195],
        "temperatura": [20, 22, 25, 30, 35, 40, 45, 28, 32, 38, 42, 48],
        "oxigenio": [98, 96, 95, 93, 90, 88, 85, 92, 89, 87, 84, 80],
        "fadiga": [
            "Baixa",
            "Baixa",
            "Moderada",
            "Moderada",
            "Alta",
            "Alta",
            "Crítica",
            "Moderada",
            "Alta",
            "Crítica",
            "Crítica",
            "Crítica"
        ]
    })

    X = dados[["velocidade", "distancia", "bpm", "temperatura", "oxigenio"]]
    y = dados["fadiga"]

    modelo = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    modelo.fit(X, y)

    joblib.dump(modelo, MODEL_PATH)

    return modelo


def prever_fadiga(modelo, velocidade, distancia, bpm, temperatura, oxigenio):
    entrada = [[velocidade, distancia, bpm, temperatura, oxigenio]]
    return modelo.predict(entrada)[0]


def calcular_risco_operacional(fadiga, bpm, temperatura, oxigenio):
    if fadiga == "Crítica":
        return "Crítico"

    if fadiga == "Alta" and (bpm > 175 or temperatura > 40 or oxigenio < 88):
        return "Alto"

    if fadiga == "Alta":
        return "Alto"

    if fadiga == "Moderada":
        return "Médio"

    return "Baixo"