# Realizando as importações  necessárias
from PyQt5.QtWidgets import  QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog

# Herdando a classe QDialog
# Criando um novo tipo de diálogo chamado form
class Form(QDialog):

    # Construtor de classe
    def __init__(self, parent=None):
        # Chamando o construtor da classe QDialog
        super(Form, self).__init__(parent)

        # Criando os widgets
        self.edit = QLineEdit("Escreva seu nome aqui!")
        self.button = QPushButton("Mostrar os cuprimentos")

        # Criando o layout e adicionando os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Configurando o layout do diálogo
        self.setLayout(layout)

        # Conectando o sinal ao slot
        self.button.clicked.connect(self.greetings)

    # Slot: Cumprimentos ao usuário
    def greetings(self):
        print("Hello %s" % self.edit.text())

if __name__ == "__main__":
    # Criando a janela da aplicação
    app = QApplication([])

    # Criando e apresentando o Form
    form = Form()
    form.show()

    # Executando a janela
    app.exec_()