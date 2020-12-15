import sys, random
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLineEdit, QLabel


def disable_visibility():
    son1_label_1.setVisible(False)
    son1_label_2.setVisible(False)
    son1_label_3.setVisible(False)
    son2_label_1.setVisible(False)
    son2_label_2.setVisible(False)
    son2_label_3.setVisible(False)

def on_cross_pushbutton_clicked():
    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover()
        print(offsprings)
        son1_label_1.setVisible(True)
        son1_label_2.setVisible(True)
        son1_label_3.setVisible(True)
        son2_label_1.setVisible(True)
        son2_label_2.setVisible(True)
        son2_label_3.setVisible(True)

    else:
        offsprings = pmx_crossover()
        son1_label_1.setVisible(True)
        son1_label_2.setVisible(True)
        son1_label_3.setVisible(True)
        son2_label_1.setVisible(True)
        son2_label_2.setVisible(True)
        son2_label_3.setVisible(True)

    son1_label_1.setText(offsprings[0])
    son1_label_2.setText(offsprings[1])
    son1_label_3.setText(offsprings[2])
    son2_label_1.setText(offsprings[3])
    son2_label_2.setText(offsprings[4])
    son2_label_3.setText(offsprings[5])


def on_method_combobox_current_text_changed():
    if method_combo_box.currentText() == "PMX":
        disable_visibility()
        father_line_edit.setInputMask('9999999999')
        father_line_edit.setText('1234567890')
        mother_line_edit.setInputMask('9999999999')
        mother_line_edit.setText('5417268390')
    else:
        disable_visibility()
        father_line_edit.setInputMask('BBBBBBBBBB')
        father_line_edit.setText('0000000000')
        mother_line_edit.setInputMask('BBBBBBBBBB')
        mother_line_edit.setText('1111111111')

def pmx_crossover():
    father = list(father_line_edit.text())
    mother = list(mother_line_edit.text())

    print('Father ',father)
    print('Mother ',mother)
    ## Alterando o filho 1
    son1 = mother.copy()
    son1[3] = father[3]
    son1[4] = father[4]
    son1[5] = father[5]
    son1[6] = father[6]

    print(son1)
    son1 = change_pmx(son1)
    print(son1)

    print('')
    ## Alterando o filho 2
    print('Father ', father)
    print('Mother ', mother)
    son2 = father.copy()
    son2[3] = mother[3]
    son2[4] = mother[4]
    son2[5] = mother[5]
    son2[6] = mother[6]

    print(son2)
    son2 = change_pmx(son2)
    print(son2)

    son1 = "".join(son1)
    son2 = "".join(son2)
    print(son1, son2)
    return son1[0:3], son1[3:7], son1[7:10], son2[0:3], son2[3:7], son2[7:10]

def change_pmx(value_to_change):
    listNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Verificando repetição
    for i in value_to_change:
        listNumbers[int(i)] = listNumbers[int(i)] + 1

    toPut = []
    toReplace = []
    for j in range(10):
        if listNumbers[j] < 1:
            toPut.append(j)
        elif int(listNumbers[j]) > 1:
            for k in range(listNumbers[j]):
                toReplace.append(j)

    #print(toPut, toReplace)

    for i in range(len(toReplace)):
        cont = 0
        for j in range(10):
            if toReplace[i] == int(value_to_change[j]):
                if cont == 0:
                    cont = cont + 1
                elif cont == 1:
                    value_to_change[j] = str(toPut[0])
                    toPut.pop(0)
                    if toReplace[i + 1] == toReplace[i]:
                        cont = 1
                    else:
                        cont = 0

    return value_to_change

def simple_cut_crossover():
    father = list(father_line_edit.text())
    mother = list(mother_line_edit.text())

    numRandom = random.randint(0, 9)
    if numRandom == 0:
        print('mutei')
        # MUTACAO - MUTA O 1o do pai e o 2o da mãe
        toMutateFather = father[4]
        toMutateMother = mother[5]
        if toMutateFather == '0':
            toMutateFather = '1'
        else:
            toMutateFather = '0'

        if toMutateMother == '1':
            toMutateMother = '0'
        else:
            toMutateMother = '1'

        father[4] = toMutateFather
        mother[5] = toMutateMother

    father = "".join(father)
    mother = "".join(mother)
    print(father, mother)
    return father[0:3], mother[3:7], father[7:10], mother[0:3], father[3:7], mother[7:10]


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    # Loading widgets elements from ui file
    window = uic.loadUi("crossover_operation.ui")
    window.show()

    # Getting widgets elements
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    son1_label_1 = window.findChild(QLabel, 'son1Label1')
    son1_label_2 = window.findChild(QLabel, 'son1Label2')
    son1_label_3 = window.findChild(QLabel, 'son1Label3')
    son2_label_1 = window.findChild(QLabel, 'son2Label1')
    son2_label_2 = window.findChild(QLabel, 'son2Label2')
    son2_label_3 = window.findChild(QLabel, 'son2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')

    # Connecting
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)

    sys.exit(app.exec_())
