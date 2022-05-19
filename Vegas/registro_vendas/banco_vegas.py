import sqlite3


# class ClienteDB:
#     def __init__(self, arquivo):
#         self.conn = sqlite3.connect(arquivo)
#         self.cursor = self.conn.cursor()
#
#     def inserir(self, nome, bairro):
#         consulta = 'INSERT OR IGNORE INTO clientes (nome, bairro) VALUES (?, ?)'
#         self.cursor.execute(consulta, (nome, bairro))
#         self.conn.commit()
#
#     def editar(self, nome, bairro, id):
#         consulta = 'UPDATE OR IGNORE clientes SET nome=?, bairro=? WHERE id=?'
#         self.cursor.execute(consulta, (nome, bairro, id))
#         self.conn.commit()
#
#     def excluir(self, id):
#         consulta = 'DELETE FROM clientes WHERE id_cliente=?'
#         self.cursor.execute(consulta, (id,))
#         self.conn.commit()
#
#     def buscar(self, valor):
#         consulta = 'SELECT * FROM clientes WHERE nome LIKE ?'
#         self.cursor.execute(consulta, (f'%{valor}%',))
#
#         for linha in self.cursor.fetchall():
#             print(linha)
#
#     def fechar(self):
#         self.cursor.close()
#         self.conn.close()


class VendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, data, nome, bairro, produto, hamburguer, quantidade, valor, tipo_venda, taxa_entrega,
                forma_pagamento):
        consulta = 'INSERT OR IGNORE INTO vendas (data, nome, bairro, produto, hamburguer, quantidade, valor, ' \
                   'tipo_venda, taxa_entrega, forma_pagamento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.cursor.execute(consulta, (data, nome, bairro, produto, hamburguer, quantidade, valor, tipo_venda,
                                       taxa_entrega, forma_pagamento))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM vendas')

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


caminho = r'C:\Users\Ribas\Documents\Vegas\vegas.db'

