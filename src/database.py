import sqlite3
import pandas as pd


DB_PATH = "data/astroperformance.db"


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        astronauta TEXT,
        missao TEXT,
        ambiente TEXT,
        distancia REAL,
        velocidade REAL,
        bpm REAL,
        temperatura REAL,
        oxigenio REAL,
        fadiga TEXT,
        risco TEXT,
        relatorio TEXT
    )
    """)

    conn.commit()
    conn.close()


def salvar_analise(
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
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analises (
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
    ))

    conn.commit()
    conn.close()


def listar_analises():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM analises", conn)
    conn.close()
    return df