# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_cryptograph.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cryptograph(object):
    def setupUi(self, Cryptograph):
        Cryptograph.setObjectName("Cryptograph")
        Cryptograph.setWindowModality(QtCore.Qt.WindowModal)
        Cryptograph.resize(282, 153)
        self.verticalLayoutWidget = QtWidgets.QWidget(Cryptograph)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cryptogprah_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cryptogprah_combobox.setObjectName("cryptogprah_combobox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cryptogprah_combobox)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.key = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.key.setObjectName("key")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.key)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Cryptograph)
        self.buttonBox.accepted.connect(Cryptograph.accept) # type: ignore
        self.buttonBox.rejected.connect(Cryptograph.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Cryptograph)

    def retranslateUi(self, Cryptograph):
        _translate = QtCore.QCoreApplication.translate
        Cryptograph.setWindowTitle(_translate("Cryptograph", "Dialog"))
        self.label.setText(_translate("Cryptograph", "Cryptograph"))
        self.label_2.setText(_translate("Cryptograph", "Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cryptograph = QtWidgets.QDialog()
    ui = Ui_Cryptograph()
    ui.setupUi(Cryptograph)
    Cryptograph.show()
    sys.exit(app.exec_())