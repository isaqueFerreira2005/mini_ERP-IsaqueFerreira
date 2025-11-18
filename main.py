import sqlite3

DB_FILE = "estoque.db"

# -----------------------------------------------------
# Função para conectar ao banco e criar tabela 
# -----------------------------------------------------
def inicializar_banco():
    with sqlite3.connect(DB_FILE) as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        conexao.commit()


# -----------------------------------------------------
# Cadastro de produto
# -----------------------------------------------------
def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")

    nome = input("Nome do produto: ").strip()
    if not nome:
        print("❌ Nome não pode ficar vazio.")
        return

    categoria = input("Categoria: ").strip()
    if not categoria:
        print("❌ Categoria não pode ficar vazia.")
        return

    while True:
        preco_raw = input("Preço (R$): ").strip().replace(",", ".")
        qtd_raw = input("Quantidade inicial: ").strip()
        try:
            preco = float(preco_raw)
            quantidade = int(qtd_raw)
            if preco < 0:
                print("❌ Preço não pode ser negativo.")
                continue
            if quantidade < 0:
                print("❌ Quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("❌ Digite valores válidos para preço e quantidade.")

    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO produtos (nome, categoria, preco, quantidade)
                VALUES (?, ?, ?, ?)
            """, (nome, categoria, preco, quantidade))
            conexao.commit()
        print(f"\n✅ Produto '{nome}' cadastrado com sucesso!")
    except sqlite3.Error as e:
        print("❌ Erro ao cadastrar produto:", e)

