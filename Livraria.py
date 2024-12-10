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
Senha TEXT NOT NULL
);
'''
cursor.execute(sql_usuario)


sql_livro = '''
CREATE TABLE IF NOT EXISTS Livro(
IdLivro INTEGER PRIMARY KEY AUTOINCREMENT,
Autor TEXT NOT NULL,
Titulo TEXT NOT NULL,
Categoria TEXT NOT NULL,
Preco DECIMAL(7,2)
Descricao TEXT
);
'''
cursor.execute(sql_livro)


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

conexao.commit()
conexao.close()

categoria = [
    ('Autor do livro', 'Titulo do livro', 'Categoria', 00.00, 'Descrição'),
    ('Autor do livro', 'Titulo do livro', 'Categoria', 00.00, 'Descrição'),
    ('Autor do livro', 'Titulo do livro', 'Categoria', 00.00, 'Descrição'),
]

