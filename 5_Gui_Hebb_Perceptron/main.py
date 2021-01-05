from PyQt5 import QtCore,QtWidgets, uic
from PyQt5.QtWidgets import QAction, QApplication, QLabel,QPushButton,QRadioButton, QSpinBox,QComboBox


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi('gui.ui')

    #combo = window.findChild(QComboBox)
    window.show()
    app.exec_()
    # Interligando as coisas da ui
