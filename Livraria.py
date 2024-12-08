import sqlite3
import os

os.remove("Livraria.db") if os.path.exists("Livraria.db") else None
conexao = sqlite3.connect("Livraria.db")
cursor = conexao.cursor()

sql_usuario = '''
CREATE TABLE IF NOT EXISTS Usuario(
IdUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
NomeUsuario TEXT NOT NULL,
Email TEXT NOT NULL,
Senha TEXT NOT NULL,
);
'''
cursor.execute(sql_usuario)

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

sql_comentario = '''
CREATE TABLE IF NOT EXISTS Comentario(
IdComentario INTEGER PRIMARY KEY AUTOINCREMENT,
IdUsuario INTEGER FOREIGN KEY,
IdLivro INTEGER FOREIGN KEY,
Estrelas INTEGER,
Comentarios TEXT NOT NULL,
FOREIGN KEY(IdUsuario) REFERENCES Usuario(IdUsuario),
FORET KEY(IdLivro) REFERENCES Livro(IdLivro)
'''
cursor.execute(sql_comentario)

sql_pedido = '''
CREATE TABLE IF NOT EXISTS Pedido(
IdPedido INTEGER PRIMARY KEY AUTOINCREMENT,
IdUsuario INTEGER FOREIGN KEY,
ValorPedido DECIMAL(7,2),
StatusPedido TEXT,
FOREIGN KEY(IdUsuario) REFERENCES Usuario(IdUsuario)
);
'''
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
cursor.execute(sql_pedido)
cursor.execute(triger_pedido)

sql_carrinho = '''
CREATE TABLE IF NOT EXISTS Carrinho(
IdCarrinho INTEGER PRIMARY KEY AUTOINCREMENT,
IdPedido INTEGER FOREIGN KEY,
IdLivro INTEGER FOREIGN KEY,
Quantidade INTEGER,
Preco DECIMAL(7,2), 
PrecoTotal DECIMAL(7,2)
);
'''
cursor.execute(sql_carrinho)
