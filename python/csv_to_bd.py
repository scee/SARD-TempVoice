import csv
import sqlite3
from datetime import datetime
import os

CSV_FILE = "registos.csv"
DB_FILE = "sard.db"

def conectar_bd():
    """
    Cria a conexão com a base de dados SQLite
    """
    conn = sqlite3.connect(DB_FILE)
    return conn

def criar_tabela(conn):
    """
    Cria a tabela caso não exista
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperatura REAL,
            pressao REAL,
            humidade REAL,
            condicao TEXT
        )
    """)
    conn.commit()

def importar_csv(conn):
    """
    Lê o CSV e insere os dados na base de dados
    """
    cursor = conn.cursor()

    with open(CSV_FILE, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            timestamp = row["Timestamp"]

            temperatura = float(row["Temperatura"]) if row["Temperatura"] else None
            pressao = float(row["Pressao"]) if row["Pressao"] else None
            humidade = float(row["Humidade"]) if row["Humidade"] else None
            condicao = row["Condicao"]

            cursor.execute("""
                INSERT INTO registos (timestamp, temperatura, pressao, humidade, condicao)
                VALUES (?, ?, ?, ?, ?)
            """, (timestamp, temperatura, pressao, humidade, condicao))

    conn.commit()

def testar_conexao(conn):
    """
    Teste simples para confirmar inserção
    """
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM registos")
    total = cursor.fetchone()[0]
    print(f"Total de registos na base de dados: {total}")

def main():
    if not os.path.exists(CSV_FILE):
        print("❌ Ficheiro CSV não encontrado.")
        return

    conn = conectar_bd()
    criar_tabela(conn)
    importar_csv(conn)
    testar_conexao(conn)
    conn.close()

    print(" Importação concluída com sucesso.")

if __name__ == "__main__":
    main()
