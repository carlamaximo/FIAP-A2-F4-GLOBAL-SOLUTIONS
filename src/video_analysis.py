import os
import cv2
import math
import numpy as np


def salvar_video(video):
    os.makedirs("data", exist_ok=True)

    caminho = "data/video_upload.mp4"

    with open(caminho, "wb") as arquivo:
        arquivo.write(video.read())

    return caminho


def detectar_movimento_com_opencv(video_path):
    cap = cv2.VideoCapture(video_path)

    posicoes = []

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(gray, 50, 150)

        coords = np.column_stack(np.where(edges > 0))

        if len(coords) > 0:
            y, x = np.mean(coords, axis=0)
            posicoes.append((x, y))

    cap.release()

    return posicoes


def calcular_distancia(posicoes):
    distancia = 0

    for i in range(1, len(posicoes)):
        x1, y1 = posicoes[i - 1]
        x2, y2 = posicoes[i]

        distancia += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distancia


def calcular_velocidade_media(distancia, tempo_segundos=60):
    if tempo_segundos <= 0:
        return 0

    return distancia / tempo_segundos