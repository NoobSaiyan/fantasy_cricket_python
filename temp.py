# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 503)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.heading = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.heading.setMinimumSize(QtCore.QSize(100, 50))
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.team_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.team_combo_box.setMinimumSize(QtCore.QSize(0, 0))
        self.team_combo_box.setObjectName("team_combo_box")
        self.horizontalLayout_3.addWidget(self.team_combo_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.match_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.match_combo_box.setObjectName("match_combo_box")
        self.horizontalLayout_3.addWidget(self.match_combo_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.player_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.player_list.setObjectName("player_list")
        self.verticalLayout_3.addWidget(self.player_list)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.points_list = QtWidgets.QListView(self.verticalLayoutWidget)
        self.points_list.setObjectName("points_list")
        self.verticalLayout_4.addWidget(self.points_list)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.calculate_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.calculate_button.setObjectName("calculate_button")
        self.horizontalLayout_2.addWidget(self.calculate_button)
        self.total_point = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.total_point.setAlignment(QtCore.Qt.AlignCenter)
        self.total_point.setObjectName("total_point")
        self.horizontalLayout_2.addWidget(self.total_point)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.heading.setText(_translate("Dialog", "Evaluate Your Team"))
        self.label_5.setText(_translate("Dialog", "Team"))
        self.label_6.setText(_translate("Dialog", "Match"))
        self.label_2.setText(_translate("Dialog", "Players"))
        self.label_3.setText(_translate("Dialog", "Points by Player"))
        self.calculate_button.setText(_translate("Dialog", "Calculate Score"))
        self.total_point.setText(_translate("Dialog", "Total Points"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
