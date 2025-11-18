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

# -----------------------------------------------------
# Exclusão de produto (segura e à prova de confusões)
# -----------------------------------------------------
def excluir_produto():
    print("\n--- EXCLUIR PRODUTO ---")
    entrada = input("Digite o NOME ou ID do produto que deseja excluir: ").strip()

    if not entrada:
        print("❌ Entrada inválida.")
        return

    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()

            if entrada.isdigit():
                cursor.execute("SELECT * FROM produtos WHERE id = ?", (int(entrada),))
                item = cursor.fetchone()
                if item:
                    print("\nProduto encontrado:")
                    print(f"ID: {item[0]} | Nome: {item[1]} | Categoria: {item[2]} | Preço: R$ {item[3]:.2f} | Quantidade: {item[4]}")
                    confirmar = input("Confirmar exclusão deste ID? (s/n): ").strip().lower()
                    if confirmar == "s":
                        cursor.execute("DELETE FROM produtos WHERE id = ?", (int(entrada),))
                        conn.commit()
                        print("✅ Produto excluído com sucesso!")
                    else:
                        print("Operação cancelada.")
                    return
            
            # Busca por nome 
            cursor.execute("SELECT * FROM produtos WHERE LOWER(nome) = LOWER(?)", (entrada,))
            resultados = cursor.fetchall()

            if not resultados:
                print("❌ Nenhum produto encontrado com esse nome ou ID.")
                return

            if len(resultados) > 1:
                print("\nForam encontrados vários produtos com esse nome:")
                for r in resultados:
                    print(f"ID: {r[0]} | Nome: {r[1]} | Categoria: {r[2]} | Preço: R$ {r[3]:.2f} | Quantidade: {r[4]}")
                id_escolhido = input("\nDigite o ID exato do produto que deseja excluir: ").strip()
                if not id_escolhido.isdigit():
                    print("❌ ID inválido.")
                    return
                if not any(r[0] == int(id_escolhido) for r in resultados):
                    print("❌ Esse ID não pertence aos produtos listados.")
                    return
                confirmar = input("Confirmar exclusão? (s/n): ").strip().lower()
                if confirmar == "s":
                    cursor.execute("DELETE FROM produtos WHERE id = ?", (int(id_escolhido),))
                    conn.commit()
                    print("✅ Produto excluído com sucesso!")
                else:
                    print("Operação cancelada.")
                return

            item = resultados[0]
            print("\nProduto encontrado:")
            print(f"ID: {item[0]} | Nome: {item[1]} | Categoria: {item[2]} | Preço: R$ {item[3]:.2f} | Quantidade: {item[4]}")
            confirmar = input("Confirmar exclusão deste produto? (s/n): ").strip().lower()
            if confirmar == "s":
                cursor.execute("DELETE FROM produtos WHERE id = ?", (item[0],))
                conn.commit()
                print("✅ Produto excluído com sucesso!")
            else:
                print("Operação cancelada.")

    except sqlite3.Error as e:
        print("❌ Erro ao acessar o banco:", e)

