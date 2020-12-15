import sys
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QSpinBox

def on_calc_clicked():

    dinheiro = spinDinheiro.value()
    pessoa = spinPessoa.value()
    pouco = 0
    razoavel = 0
    adequado = 0
    insuficiente = 0
    satisfatorio = 0

    # Verificando o dinheiro (Dividido entre <= 30, 30 e <50, = 50, > 50 e < 70, >=70
    if dinheiro <= 30:
        pouco = 1
        razoavel = 0
        adequado = 0

    elif 30 < dinheiro < 50:
        pouco = (50 - dinheiro)/ (50 - 30)
        razoavel = (dinheiro - 30) / (50 - 30)
        adequado = 0

    elif dinheiro == 50:
        pouco = 0
        razoavel = 1
        adequado = 0

    elif 50 < dinheiro < 70:
        pouco = 0
        razoavel = (70 - dinheiro) / (70 - 50)
        adequado = (dinheiro - 50) / 70 - 50

    elif dinheiro >= 70:
        pouco = 0
        razoavel = 0
        adequado = 1

    print('Pouco: ' + str(pouco) + ' Razoavel: ' + str(razoavel) + ' Adequado: '+str(adequado))
    # Análise das pessoas, sendo: <= 30, >30 e < 70 e >=70
    if pessoa <= 30:
        insuficiente = 1
        satisfatorio = 0

    elif 30 < pessoa < 70:
        insuficiente = (70 - pessoa) / (70 - 30)
        satisfatorio = (pessoa - 30) / (70 - 30)

    elif pessoa >= 70:
        insuficiente = 0
        satisfatorio = 1

    print('Insuficiente: ' + str(insuficiente) + ' Satisfatorio: ' + str(satisfatorio))
    ## Verificação das regras:
    baixo = 0
    medio = 0
    alto = 0

    ## Regra 01: Se d_pouco OU p_insuficiente então alto
    if pouco < insuficiente:
        alto = insuficiente
    else:
        alto = pouco

    ## Regra 02: Se d_pouco E p_satisfatorio então alto
    if pouco < satisfatorio:
        alto = pouco
    else:
        alto= satisfatorio

    ## Regra 03 : Se d_razoável E p_satisfatório então médio
    if razoavel < satisfatorio:
        medio = razoavel
    else:
        medio = satisfatorio

    ## Regra 04 : Se d_adequado E p_satisfatório então baixo
    if adequado < satisfatorio:
        baixo = adequado
    else:
        baixo = satisfatorio

    print('Baixo: '  + str(baixo) + ' Médio: '+ str(medio) + ' Alto ' + str(alto))
    ## Verificando o resultado das regras
    cog = 0
    div = 0


    if baixo > 0:
        cog = cog + ((10 + 20 + 30)* baixo)
        div = div + (3* baixo)


    if medio > 0:
        cog = cog + ((40 + 50 + 60) * medio)
        div = div + (3 * medio)


    if alto > 0:
        cog = cog + ((70 + 80 + 90) * alto)
        div = div + (3 * alto)

    cog = cog / div

    if cog <= 35:
        labelResp.setText('Baixo de ' + str(cog) + '%')

    elif 35 < cog < 65:
        labelResp.setText('Medio de ' + str(cog) + '%')

    elif cog >= 65:
        labelResp.setText('Alto de ' + str(cog) + '%')

    labelResp.setVisible(True)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi("UIDesign.ui")

    labelDinheiro = window.findChild(QLabel, 'labelDinheiro')
    labelPessoa = window.findChild(QLabel, 'labelPessoa')
    labelRisco = window.findChild(QLabel, 'labelRisco')
    labelResp = window.findChild(QLabel, 'labelResp')
    labelResp.setVisible(False)

    spinDinheiro = window.findChild(QSpinBox, 'spinDinheiro')
    spinPessoa = window.findChild(QSpinBox, 'spinPessoa')


    btnCalcular = window.findChild(QPushButton, 'btnCalcular')
    btnCalcular.clicked.connect(on_calc_clicked)

    window.show()

    app.exec_()