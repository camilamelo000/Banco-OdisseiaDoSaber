import sqlite3
import os

# Remove o arquivo Livraria.db se ele existir
os.remove("Livraria.db") if os.path.exists("Livraria.db") else None

# Conecta ao banco de dados
conexao = sqlite3.connect("Livraria.db")
cursor = conexao.cursor()

# Criação da tabela Usuario
sql_usuario = '''
CREATE TABLE IF NOT EXISTS Usuario(
IdUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
NomeUsuario TEXT NOT NULL,
Email TEXT NOT NULL,
Senha TEXT NOT NULL
);
'''
cursor.execute(sql_usuario)

# Criação da tabela Livro
sql_livro = '''
CREATE TABLE IF NOT EXISTS Livro(
IdLivro INTEGER PRIMARY KEY AUTOINCREMENT,
Titulo TEXT NOT NULL,
Autor TEXT NOT NULL,
Categoria TEXT NOT NULL,
Descricao TEXT NOT NULL,
Preco DECIMAL(7,2),
StatusLivro TEXT
);
'''
cursor.execute(sql_livro)

# Criação da tabela Comentario
sql_comentario = '''
CREATE TABLE IF NOT EXISTS Comentario(
IdComentario INTEGER PRIMARY KEY AUTOINCREMENT,
IdUsuario INTEGER,
IdLivro INTEGER,
Estrelas INTEGER,
Comentarios TEXT NOT NULL,
FOREIGN KEY(IdUsuario) REFERENCES Usuario(IdUsuario),
FOREIGN KEY(IdLivro) REFERENCES Livro(IdLivro)
);
'''
cursor.execute(sql_comentario)

# Criação da tabela Pedido
sql_pedido = '''
CREATE TABLE IF NOT EXISTS Pedido(
IdPedido INTEGER PRIMARY KEY AUTOINCREMENT,
IdUsuario INTEGER,
ValorPedido DECIMAL(7,2),
StatusPedido TEXT,
FOREIGN KEY(IdUsuario) REFERENCES Usuario(IdUsuario)
);
'''
cursor.execute(sql_pedido)

# Criação da tabela Carrinho
sql_carrinho = '''
CREATE TABLE IF NOT EXISTS Carrinho(
IdCarrinho INTEGER PRIMARY KEY AUTOINCREMENT,
IdPedido INTEGER,
IdLivro INTEGER,
Quantidade INTEGER,
Preco DECIMAL(7,2), 
PrecoTotal DECIMAL(7,2),
FOREIGN KEY(IdPedido) REFERENCES Pedido(IdPedido),
FOREIGN KEY(IdLivro) REFERENCES Livro(IdLivro)
);
'''
cursor.execute(sql_carrinho)

# Trigger de atualização do preço total no carrinho
triger_pedido = '''
CREATE TRIGGER AtualizaPrecoTotal
AFTER UPDATE OF Quantidade, Preco 
ON Carrinho FOR EACH ROW
BEGIN
  UPDATE Carrinho
  SET PrecoTotal = Quantidade * Preco
  WHERE IdCarrinho = NEW.IdCarrinho;
END;
'''
cursor.execute(triger_pedido)

# Confirma as alterações e fecha a conexão
conexao.commit()
conexao.close()


categoria = [
    ("Matemática Básica para Aplicações de Engenharia", "Kuldip S. Rattan", "Exatas", "Matemática Básica para Aplicações de Engenharia foi elaborado com o objetivo de atender aos estudantes de graduação que precisam realizar uma imersão para desenvolver e aprimorar seus conhecimentos de matemática.Esta disciplina é vista segundo a perspectiva das aplicações práticas das Engenharias, abordando tópicos básicos como pré-cálculo, trigonometria, equações diferenciais, lineares e quadráticas, vetores bidimensionais, números complexos, senoides, sistemas de equações e matrizes, derivadas e integrais. Os autores também incluíram conteúdos da física referentes às disciplinas de dinâmica, estática e resistência de materiais, entre outros, extremamente úteis aos futuros engenheiros.", 135.00, "Semi-Novo"),
    ("Matemática Básica para Aplicações de Engenharia", "Kuldip S. Rattan", "Exatas", "Matemática Básica para Aplicações de Engenharia foi elaborado com o objetivo de atender aos estudantes de graduação que precisam realizar uma imersão para desenvolver e aprimorar seus conhecimentos de matemática.Esta disciplina é vista segundo a perspectiva das aplicações práticas das Engenharias, abordando tópicos básicos como pré-cálculo, trigonometria, equações diferenciais, lineares e quadráticas, vetores bidimensionais, números complexos, senoides, sistemas de equações e matrizes, derivadas e integrais. Os autores também incluíram conteúdos da física referentes às disciplinas de dinâmica, estática e resistência de materiais, entre outros, extremamente úteis aos futuros engenheiros.", 135.00, "Semi-Novo" )

]


cursor.execute("insert into ")
