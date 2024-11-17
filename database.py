import sqlite3

def configurar_banco():
    conexao = sqlite3.connect("sistema_vendas.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        fornecedor TEXT,
        fabricante TEXT,
        valor REAL NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        total REAL NOT NULL,
        data TEXT NOT NULL
    )
    """)

    # Usuário admin padrão
    cursor.execute("SELECT * FROM usuarios WHERE nome = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (nome, senha, tipo) VALUES ('admin', 'admin', 'administrador')")

    conexao.commit()
    conexao.close()

configurar_banco()

