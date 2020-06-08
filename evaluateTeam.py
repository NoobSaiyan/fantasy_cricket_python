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
        self.points_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
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


        # connecting to db
        self.connect_to_db()

        # poulating ui and fetching teams, players and matches at start
        self.populate_ui()

        # adding combo box handlers
        self.team_combo_box.activated.connect(self.team_combo_handler)
        # manually calling once to populate data of first team
        self.team_combo_handler(0)

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

    #------------------------------#
    #combo handler 
    #------------------------------#
    def team_combo_handler(self, index):
        team_name = self.team_combo_box.itemText(index)
        team = self.teams[team_name]

        # populating players list widget
        self.player_list.clear()
        for player in team['players']:
            self.player_list.addItem(player)

        # reset points list and counter
        self.points_list.clear()
        self.total_point.setText('Total Points: 0')


    #------------------------------#
    #fetching matches data from the db 
    #------------------------------#
    def fetch_matches(self):
        matches = { "match" : {} }
        self.cricket_db_cursor.execute('SELECT player, scored, faced, fours, sixes, bowled, maiden, given, wkts, catches, stumping, ro FROM match')
        for record in self.cricket_db_cursor.fetchall():
            matches['match'].update({ record[0]: {
                    "player": record[0],
                    "scored": record[1],
                    "faced": record[2],
                    "fours": record[3],
                    "sixes": record[4],
                    "bowled": record[5],
                    "maiden": record[6],
                    "given": record[7],
                    "wkts": record[8],
                    "catches": record[9],
                    "stumping": record[10],
                    "ro": record[11]
                }
            })
        return matches
    

    #------------------------------#
    #fetching teams data from the db 
    #------------------------------#
    def fetch_teams(self):
        teams = {}
        try:
            self.cricket_db_cursor.execute('SELECT name, players, value FROM teams')
        except Exception as error:
            raise error
        
        for record in self.cricket_db_cursor.fetchall():
            teams.update({
                record[0]: {
                    "name": record[0],
                    "players": record[1].split(':'),
                    "value": record[2]
                }
            }) 
        
        return teams

    #------------------------------#
    #fetching players from db 
    #------------------------------#
    def fetch_players(self):
        players = {}
        self.cricket_db_cursor.execute('SELECT player, value, ctg FROM stats')
        for record in self.cricket_db_cursor.fetchall():
            players.update({ record[0]: {
                    "name": record[0],
                    "value": record[1],
                    "ctg": record[2]
                }
            })
        return players


    #------------------------------#
    #populating data to the UI of our evaluating dailog
    #------------------------------#
    def populate_ui(self):
        #adding team to combobox
        self.teams = self.fetch_teams()
        for team in self.teams.keys():
            self.team_combo_box.addItem(team)

        #adding match to combobox
        self.matches = self.fetch_matches()
        for match in self.matches.keys():
            self.match_combo_box.addItem(match)

        #fetching all players
        self.total_players = self.fetch_players()


    #------------------------------#
    #connnecting to data base
    #------------------------------#
    def connect_to_db(self):
        import sqlite3

        self.cricket_db = sqlite3.connect('cricket.db')
        self.cricket_db_cursor = self.cricket_db.cursor()


    #------------------------------#
    #disconnecting from database database
    #------------------------------#
    def disconnect_db(self):
        self.cricket_db.close()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
