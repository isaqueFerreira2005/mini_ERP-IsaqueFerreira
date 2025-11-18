📘 Mini-ERP de Estoque (com SQLite) 👥 Integrantes do Grupo

Cauã

Abner

Isaque

João Pedro

📌 Sobre o Projeto

Este projeto foi desenvolvido como parte da atividade de programação, com o objetivo de simular um pequeno módulo de estoque inspirado em sistemas ERP. A proposta foi criar um sistema simples, mas funcional, capaz de cadastrar produtos, excluir itens e exibir um relatório com informações do estoque.

Para garantir que os dados fossem salvos de forma permanente, utilizamos um banco de dados SQLite, que já vem integrado ao Python e não precisa de instalação adicional.

🧰 Funcionalidades Implementadas ✔️ Cadastro de produtos

O usuário pode registrar um novo produto fornecendo:

nome

categoria

preço

quantidade inicial

As informações são armazenadas automaticamente no banco SQLite.

✔️ Exclusão de produtos

O sistema permite excluir um produto usando:

ID, ou

nome

Caso haja mais de um produto com o mesmo nome, o sistema mostra a correspondência encontrada antes de excluir.

✔️ Relatório de produtos

O relatório lista todos os produtos cadastrados com:

ID

nome

categoria

preço

quantidade

Além disso, produtos com quantidade menor que 5 recebem um aviso de estoque baixo.

✔️ Banco de dados SQLite

O arquivo estoque.db é criado automaticamente na primeira execução. Todos os dados permanecem salvos mesmo depois de fechar o programa.

▶️ Como Executar o Sistema

Certifique-se de ter o Python 3 instalado.

Baixe ou clone o repositório do projeto.

No terminal, acesse a pasta do projeto.

Execute o comando:

python erp_estoque.py

Quando o programa iniciar, o arquivo estoque.db será criado automaticamente (se ainda não existir).

📂 Estrutura do Projeto / (pasta principal) ├── erp_estoque.py # Código principal do sistema ├── estoque.db # Banco de dados (gerado automaticamente) └── README.md # Documentação do projeto

🔧 Tecnologias Utilizadas

Python 3

SQLite (sqlite3)

A biblioteca sqlite3 já vem instalada por padrão com o Python.

💬 Sugestão de Commits

Para manter o histórico bem organizado no GitHub, estas mensagens podem ser usadas:

Inicialização do projeto Adicionado sistema de cadastro usando SQLite Implementada exclusão por ID e nome Criado relatório com alerta de estoque baixo Adicionado README com documentação completa

📝 Observações

Se quiser apagar todos os dados e começar do zero, basta deletar o arquivo estoque.db.

O sistema foi planejado para funcionar em ambiente de terminal, como solicitado.
