from datetime import datetime
import sys
from banco_vegas import *
from cadastro_vendas import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSalvar.clicked.connect(self.salvar)
        self.btnNovo.clicked.connect(self.nova_venda)
        self.btnIncluirProduto.clicked.connect(self.incluir_produto)

    def salvar(self):
        data = datetime.now().strftime('%d/%m')
        nome = str(self.inputNome.text().title())
        bairro = str(self.inputBairro.text().title())
        produto = str(self.cbProdutos.currentText())
        hamburguer = str(self.cbHamburguer.currentText())
        quantidade = str(self.inputQuantidade.text())
        valor = str(self.inputValor.text().replace(',', '.'))
        tipo_venda = str(self.cbTipoDaVenda.currentText())
        taxa_entrega = str(self.inputTaxaDeEntrega.text().replace(',', '.'))
        forma_pagamento = str(self.cbFormaDePagamento.currentText())

        venda = VendaDB(caminho)
        venda.inserir(data, nome, bairro, produto, hamburguer, quantidade, valor, tipo_venda, taxa_entrega,
                      forma_pagamento)
        self.msg.setText(str('<span style="color: #008000; font-size: 18px;">Venda registrada com sucesso.'))

    def nova_venda(self):
        self.inputNome.setText(str(''))
        self.inputBairro.setText(str(''))
        self.cbProdutos.setCurrentText(str(''))
        self.cbHamburguer.setCurrentText(str(''))
        self.inputQuantidade.setText(str(''))
        self.cbTipoDaVenda.setCurrentText(str(''))
        self.inputValor.setText(str(''))
        self.cbFormaDePagamento.setCurrentText(str(''))
        self.inputTaxaDeEntrega.setText(str(''))
        self.msg.setText(str(''))

    def incluir_produto(self):
        self.cbProdutos.setCurrentText(str(''))
        self.cbHamburguer.setCurrentText(str(''))
        self.inputQuantidade.setText(str(''))
        self.inputValor.setText(str(''))
        self.inputTaxaDeEntrega.setText(str(''))
        self.msg.setText(str(''))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
