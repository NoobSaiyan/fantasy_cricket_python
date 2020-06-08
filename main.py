# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FantasyCricket(object):
    def setupUi(self, FantasyCricket):
        FantasyCricket.setObjectName("FantasyCricket")
        FantasyCricket.resize(1083, 799)
        font = QtGui.QFont()
        font.setPointSize(10)
        FantasyCricket.setFont(font)
        self.centralwidget = QtWidgets.QWidget(FantasyCricket)
        self.centralwidget.setObjectName("centralwidget")
        self.top = QtWidgets.QWidget(self.centralwidget)
        self.top.setGeometry(QtCore.QRect(50, 30, 979, 89))
        self.top.setAutoFillBackground(False)
        self.top.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.top.setObjectName("top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Batsmen = QtWidgets.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Batsmen.setFont(font)
        self.Batsmen.setObjectName("Batsmen")
        self.horizontalLayout_2.addWidget(self.Batsmen)
        self.Batsmen_value = QtWidgets.QLineEdit(self.top)
        self.Batsmen_value.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Batsmen_value.setFont(font)
        self.Batsmen_value.setAccessibleDescription("")
        self.Batsmen_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Batsmen_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Batsmen_value.setReadOnly(False)
        self.Batsmen_value.setObjectName("Batsmen_value")
        self.horizontalLayout_2.addWidget(self.Batsmen_value)
        self.Bowler = QtWidgets.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bowler.setFont(font)
        self.Bowler.setObjectName("Bowler")
        self.horizontalLayout_2.addWidget(self.Bowler)
        self.Bowler_value = QtWidgets.QLineEdit(self.top)
        self.Bowler_value.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bowler_value.setFont(font)
        self.Bowler_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Bowler_value.setObjectName("Bowler_value")
        self.horizontalLayout_2.addWidget(self.Bowler_value)
        self.All_Rounder = QtWidgets.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.All_Rounder.setFont(font)
        self.All_Rounder.setObjectName("All_Rounder")
        self.horizontalLayout_2.addWidget(self.All_Rounder)
        self.All_Rounder_value = QtWidgets.QLineEdit(self.top)
        self.All_Rounder_value.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.All_Rounder_value.setFont(font)
        self.All_Rounder_value.setAlignment(QtCore.Qt.AlignCenter)
        self.All_Rounder_value.setObjectName("All_Rounder_value")
        self.horizontalLayout_2.addWidget(self.All_Rounder_value)
        self.Wicket_Keeper = QtWidgets.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Wicket_Keeper.setFont(font)
        self.Wicket_Keeper.setObjectName("Wicket_Keeper")
        self.horizontalLayout_2.addWidget(self.Wicket_Keeper)
        self.Wicket_Keeper_value = QtWidgets.QLineEdit(self.top)
        self.Wicket_Keeper_value.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Wicket_Keeper_value.setFont(font)
        self.Wicket_Keeper_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Wicket_Keeper_value.setObjectName("Wicket_Keeper_value")
        self.horizontalLayout_2.addWidget(self.Wicket_Keeper_value)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 120, 981, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bottom_2 = QtWidgets.QWidget(self.centralwidget)
        self.bottom_2.setGeometry(QtCore.QRect(49, 149, 981, 581))
        self.bottom_2.setAutoFillBackground(True)
        self.bottom_2.setStyleSheet("")
        self.bottom_2.setObjectName("bottom_2")
        self.bottom = QtWidgets.QHBoxLayout(self.bottom_2)
        self.bottom.setContentsMargins(0, 0, 0, 0)
        self.bottom.setObjectName("bottom")
        self.left = QtWidgets.QWidget(self.bottom_2)
        self.left.setAutoFillBackground(False)
        self.left.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.left.setObjectName("left")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem2)
        self.widget = QtWidgets.QWidget(self.left)
        self.widget.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.Points_Left = QtWidgets.QLabel(self.widget)
        self.Points_Left.setObjectName("Points_Left")
        self.horizontalLayout_5.addWidget(self.Points_Left)
        self.Points_Left_value = QtWidgets.QLineEdit(self.widget)
        self.Points_Left_value.setEnabled(False)
        self.Points_Left_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Points_Left_value.setObjectName("Points_Left_value")
        self.horizontalLayout_5.addWidget(self.Points_Left_value)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_7.addWidget(self.widget)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem5)
        self.Plyer_Category = QtWidgets.QLabel(self.left)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Plyer_Category.setFont(font)
        self.Plyer_Category.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.Plyer_Category.setAlignment(QtCore.Qt.AlignCenter)
        self.Plyer_Category.setObjectName("Plyer_Category")
        self.verticalLayout_7.addWidget(self.Plyer_Category)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem6)
        self.radioHandler = QtWidgets.QWidget(self.left)
        self.radioHandler.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.radioHandler.setObjectName("radioHandler")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.radioHandler)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.BAT_radio = QtWidgets.QRadioButton(self.radioHandler)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BAT_radio.setFont(font)
        self.BAT_radio.setObjectName("BAT_radio")
        self.horizontalLayout_4.addWidget(self.BAT_radio)
        self.BWL_radio = QtWidgets.QRadioButton(self.radioHandler)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BWL_radio.setFont(font)
        self.BWL_radio.setObjectName("BWL_radio")
        self.horizontalLayout_4.addWidget(self.BWL_radio)
        self.AR_radio = QtWidgets.QRadioButton(self.radioHandler)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AR_radio.setFont(font)
        self.AR_radio.setObjectName("AR_radio")
        self.horizontalLayout_4.addWidget(self.AR_radio)
        self.WK_radio = QtWidgets.QRadioButton(self.radioHandler)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WK_radio.setFont(font)
        self.WK_radio.setObjectName("WK_radio")
        self.horizontalLayout_4.addWidget(self.WK_radio)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_7.addWidget(self.radioHandler)
        self.Player_Catergory_value = QtWidgets.QListWidget(self.left)
        self.Player_Catergory_value.setObjectName("Player_Catergory_value")
        self.verticalLayout_7.addWidget(self.Player_Catergory_value)
        self.bottom.addWidget(self.left)
        spacerItem9 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.bottom.addItem(spacerItem9)
        self.right_2 = QtWidgets.QWidget(self.bottom_2)
        self.right_2.setAutoFillBackground(False)
        self.right_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.right_2.setObjectName("right_2")
        self.right = QtWidgets.QVBoxLayout(self.right_2)
        self.right.setObjectName("right")
        spacerItem10 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.right.addItem(spacerItem10)
        self.widget1 = QtWidgets.QWidget(self.right_2)
        self.widget1.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.Points_Used = QtWidgets.QLabel(self.widget1)
        self.Points_Used.setObjectName("Points_Used")
        self.horizontalLayout_6.addWidget(self.Points_Used)
        self.Points_Used_value = QtWidgets.QLineEdit(self.widget1)
        self.Points_Used_value.setEnabled(False)
        self.Points_Used_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Points_Used_value.setObjectName("Points_Used_value")
        self.horizontalLayout_6.addWidget(self.Points_Used_value)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.right.addWidget(self.widget1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.right.addItem(spacerItem13)
        self.Player_Selected = QtWidgets.QLabel(self.right_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Player_Selected.setFont(font)
        self.Player_Selected.setAutoFillBackground(False)
        self.Player_Selected.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.Player_Selected.setAlignment(QtCore.Qt.AlignCenter)
        self.Player_Selected.setObjectName("Player_Selected")
        self.right.addWidget(self.Player_Selected)
        spacerItem14 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.right.addItem(spacerItem14)
        self.Team_Name = QtWidgets.QLabel(self.right_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Team_Name.setFont(font)
        self.Team_Name.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.Team_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Team_Name.setObjectName("Team_Name")
        self.right.addWidget(self.Team_Name)
        self.Player_Selected_value = QtWidgets.QListWidget(self.right_2)
        self.Player_Selected_value.setObjectName("Player_Selected_value")
        self.right.addWidget(self.Player_Selected_value)
        self.bottom.addWidget(self.right_2)
        FantasyCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FantasyCricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        FantasyCricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FantasyCricket)
        self.statusbar.setObjectName("statusbar")
        FantasyCricket.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(FantasyCricket)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(FantasyCricket)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSave_Team = QtWidgets.QAction(FantasyCricket)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Score = QtWidgets.QAction(FantasyCricket)
        self.actionEvaluate_Score.setObjectName("actionEvaluate_Score")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_Score)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(FantasyCricket)
        QtCore.QMetaObject.connectSlotsByName(FantasyCricket)


         # connect handle functions
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu_handle)
        for rb in [self.BAT_radio, self.BWL_radio, self.AR_radio, self.WK_radio]:
            rb.toggled.connect(self.radio_button_handler)
        
        self.default_variables()
        self.update_ui()

        # list double clicked actions
        self.Player_Catergory_value.itemDoubleClicked.connect(self.remove_from_available_players)
        self.Player_Selected_value.itemDoubleClicked.connect(self.remove_from_chosen_players)


    def retranslateUi(self, FantasyCricket):
        _translate = QtCore.QCoreApplication.translate
        FantasyCricket.setWindowTitle(_translate("FantasyCricket", "Fantasy Cricket"))
        self.Batsmen.setText(_translate("FantasyCricket", "Batsmen"))
        self.Bowler.setText(_translate("FantasyCricket", "Bowler"))
        self.All_Rounder.setText(_translate("FantasyCricket", "All-Rounder"))
        self.Wicket_Keeper.setText(_translate("FantasyCricket", "Wicket-Keeper"))
        self.Points_Left.setText(_translate("FantasyCricket", "Points Left:"))
        self.Plyer_Category.setText(_translate("FantasyCricket", "Player Category"))
        self.BAT_radio.setText(_translate("FantasyCricket", "BAT"))
        self.BWL_radio.setText(_translate("FantasyCricket", "BWL"))
        self.AR_radio.setText(_translate("FantasyCricket", "AR"))
        self.WK_radio.setText(_translate("FantasyCricket", "WK"))
        self.Points_Used.setText(_translate("FantasyCricket", "Points Used:"))
        self.Player_Selected.setText(_translate("FantasyCricket", "Player Selected"))
        self.Team_Name.setText(_translate("FantasyCricket", "Team_Name"))
        self.menuManage_Teams.setTitle(_translate("FantasyCricket", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("FantasyCricket", "New Team"))
        self.actionOPEN_Team.setText(_translate("FantasyCricket", "Open Team"))
        self.actionSave_Team.setText(_translate("FantasyCricket", "Save Team"))
        self.actionEvaluate_Score.setText(_translate("FantasyCricket", "Evaluate Team"))

    #------------------------------#
    #setting default values of the variables
    #------------------------------#
    def default_variables(self):
        self.batsmen = 0
        self.bowler = 0
        self.all_rounder= 0
        self.wicket_keeper = 0
        self.points_left = 1000
        self.points_used = 0
        self.team_name = 'NO_TEAM_SELECTED'
        self.radio_buttons_enabled = False

        total_players = {}
        cricket_db_cursor.execute('SELECT player, value, ctg FROM stats;')
        for record in cricket_db_cursor.fetchall():
            total_players.update(
                {
                    record[0]: {
                        "name": record[0],
                        "value": record[1],
                        "ctg": record[2]
                    }
                }
            )

        self.total_players = total_players.copy()

        # clearing both lists
        self.Player_Catergory_value.clear()
        self.Player_Selected_value.clear()

    #------------------------------#
    #updating UI of the app
    #------------------------------#
    def update_ui(self):
        # update ui according to current variables
        self.Batsmen_value.setText(str(self.batsmen))
        self.Bowler_value.setText(str(self.bowler))
        self.All_Rounder_value.setText(str(self.all_rounder))
        self.Wicket_Keeper_value.setText(str(self.wicket_keeper))
        self.Points_Left_value.setText(str(self.points_left))
        self.Points_Used_value.setText(str(self.points_used))
        self.Team_Name.setText(self.team_name)

        radio_buttons = [self.BAT_radio, self.BWL_radio, self.AR_radio, self.WK_radio]
        if(self.radio_buttons_enabled):
            for rb in radio_buttons:
                rb.setEnabled(True)
        else:
            for rb in radio_buttons:
                rb.setEnabled(False)
                rb.setChecked(False)
    #------------------------------#
    #radio button handler
    #------------------------------#
    def radio_button_handler(self):
        for rb in [self.BAT_radio, self.BWL_radio, self.AR_radio, self.WK_radio]:
            if(rb.isChecked()):
                self.populate_players_list(rb.text())
    #------------------------------#
    #populating the list with the available players
    #------------------------------#
    def populate_players_list(self, category = 'ALL'):
        self.Player_Catergory_value.clear()
        players = []
        for index in range(self.Player_Selected_value.count()):
            players.append(self.Player_Selected_value.item(index).text())
        for player in self.total_players.values():
            #if player already in chosen list dont add it to available players
            if player['name'] in players:
                continue
            # category in radio button is BOW but in db its BWL
            if(category == 'BOW'):
                category = 'BWL'
            if category == 'ALL':
                self.Player_Catergory_value.addItem(player['name'])
            elif category == player['ctg']:
                self.Player_Catergory_value.addItem(player['name'])
    #------------------------------#
    #removing from the not selected player list
    #------------------------------#
    def remove_from_available_players(self, item):
        self.add_player_to_team(item.text())
        self.Player_Catergory_value.takeItem(self.Player_Catergory_value.row(item))
        self.Player_Selected_value.addItem(item.text()) 
    #------------------------------#
    #removing form the chosen players list
    #------------------------------#
    def remove_from_chosen_players(self, item):
        self.Player_Selected_value.takeItem(self.Player_Selected_value.row(item))
        self.Player_Catergory_value.addItem(item.text())
        self.remove_player_from_team(item.text())
        # update list according to category seletect in radio button
        self.radio_button_handler()
    #------------------------------#
    #adding player to the selected player list
    #------------------------------#
    def add_player_to_team(self, name):        
        player = self.total_players[name]

        if player['ctg'] == 'BAT':
            self.batsmen += 1
        elif player['ctg'] == 'BWL':
            self.bowler += 1
        elif player['ctg'] == 'AR':
            self.all_rounder +=1
        elif player['ctg'] == 'WK':
            self.wicket_keeper += 1
        self.points_left -= player['value']
        self.points_used += player['value']       
        self.update_ui()
    #------------------------------#
    #removing players form the selected player list
    #------------------------------#
    def remove_player_from_team(self, name):
        player = self.total_players[name]

        if player['ctg'] == 'BAT':
            self.batsmen -= 1
        elif player['ctg'] == 'BWL':
            self.bowler -= 1
        elif player['ctg'] == 'AR':
            self.all_rounder -=1
        elif player['ctg'] == 'WK':
            self.wicket_keeper -= 1

        self.points_left += player['value']
        self.points_used -= player['value']
        self.update_ui()


    #------------------------------#
    #handling menu options
    #------------------------------#
    #menu handle main funciton
    #------------------------------#
    def menu_handle(self,action):
        option_used = action.text()
        # creating new team
        if(option_used) == 'New Team':
            self.create_team()
        #opening existing team
        elif option_used == 'Open Team':
            try:
                self.open_team()
                print('I: team opend succesfully')
            except Exception as error:
                print(f'ERROR: {error}')
        #saving the new team
        elif option_used == 'Save Team':
            try:
                self.save_team()
                print('MESSAGE: team saved successfully')
                self.message(heading = 'Success', desc = 'Team Saved Successfully')
            except ValueError as error:
                print(f'ERROR: {error}')
                self.message(heading = 'Error', desc = str(error), icon='critical')
            except Exception as error:
                print(f'ERROR: {error}')
                self.message(heading = 'Error', desc = str(error), icon='critical')
        #Evaluation of team 
        elif option_used == 'Evaluate Team':
            try:
                self.evaluate_team()
            except Exception as error:
                print(f'ERROR: {error}')
                self.message(heading = 'Error', desc = str(error), icon='critical')   
    #------------------------------#
    #creating new team
    #------------------------------#
    def create_team(self):
        value, confirmed = QtWidgets.QInputDialog.getText(FantasyCricket, 'Fantasy Cricket', 'Enter Team Name')
        if confirmed:
            self.default_variables()
            self.team_name = value
            self.populate_players_list()
            self.radio_buttons_enabled = True
            self.update_ui()
    #------------------------------#
    #saving the team we created
    #------------------------------#
    def save_team(self):
        team_players = self.batsmen + self.bowler + self.all_rounder + self.wicket_keeper     
        #validations
        if team_players > 11:
            raise ValueError('You can only have 11 players in team')
        if team_players < 11:
            raise ValueError('You must have atleast 11 players in team')
        if self.points_left < 0:
            raise ValueError('You don\'t have enough points available')        
        if self.wicket_keeper > 1:
            raise ValueError('You can only have one Wicket Keeper in team')        
        if self.batsmen > 5:
            raise ValueError('You cat\'t have more than 5 Batsmen in team')
        if self.bowler > 5:
            raise ValueError('You can\'t have more than 5 Bowlers in team')
        if self.all_rounder > 3:
            raise ValueError('You can\'t have more than 3 all rounders in team')
        team_name = self.team_name
        team_players_string = ''
        team_value = 0
        for i in range(self.Player_Selected_value.count()):
            player_name = self.Player_Selected_value.item(i).text()
            team_players_string += player_name if i == 0 else f':{player_name}'
            team_value += self.total_players[player_name]['value']
        try:
            sql = f"""INSERT INTO teams (name, players, value) 
                VALUES ("{team_name}", "{team_players_string}", {team_value})
                ON CONFLICT(name) 
                DO UPDATE SET players = "{team_players_string}", value = {team_value} WHERE name = "{team_name}";"""
            cricket_db_cursor.execute(sql)
            cricket_db.commit()
        except Exception as error:
            cricket_db.rollback()
            raise error
        return True
    #------------------------------#
    #opening team from database
    #------------------------------#
    def open_team(self):        
        # getting teams
        teams = {}
        cricket_db_cursor.execute('SELECT name, players, value FROM teams')
        for record in cricket_db_cursor.fetchall():
            teams.update({
                record[0]: {
                    "name": record[0],
                    "players": record[1].split(':'),
                    "value": record[2]
                }
            })                                     
        if len(teams):
            opened_team, confirmed = QtWidgets.QInputDialog.getItem(FantasyCricket, "Fantasy Cricket", "Choose a team", teams.keys(), 0, False)
        else:
            raise ValueError('No saved teams found')
        if not confirmed:
            raise ValueError('No team selected')
        #loading defaults and updating ui
        self.default_variables()
        self.update_ui()
        #updating variable values to the opened team
        self.team_name = opened_team
        self.points_left -= teams[opened_team]['value']
        self.points_used = teams[opened_team]['value']
        for player_name in teams[self.team_name]['players']:
            if self.total_players[player_name]['ctg'] == 'BAT':
                self.batsmen += 1
            elif self.total_players[player_name]['ctg'] == 'BWL':
                self.bowler += 1
            elif self.total_players[player_name]['ctg'] == 'AR':
                self.all_rounder +=1
            elif self.total_players[player_name]['ctg'] == 'WK':
                self.wicket_keeper += 1
            
            self.Player_Selected_value.addItem(player_name)
        # refreshing ui
        self.populate_players_list()
        self.radio_buttons_enabled = True
        self.update_ui()

    #------------------------------#
    #function to open evaluation dailog
    #------------------------------#
    def evaluate_team(self):
        # check if atleast one team is present in database
        try:
            cricket_db_cursor.execute('SELECT name, players, value FROM teams')
        except Exception as error:
            raise error

        if len(cricket_db_cursor.fetchall()):
            # open evaluate dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            result = Dialog.exec()
        else:
            raise ValueError('No saved teams found')
    #------------------------------#
    #popup message 
    #------------------------------#
    def message(self, heading = 'Error', desc = 'Unknown Error Occured', icon = None):
        QMessageBox = QtWidgets.QMessageBox
        if not icon: icon = QMessageBox.Information
        if icon == 'critical': icon = QMessageBox.Critical
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(heading)
        msg.setInformativeText(desc + '\t\t\t')
        msg.setWindowTitle('Fantasy Cricket')
        msg.exec_()    

if __name__ == "__main__":
    import sys
    import sqlite3
    from evaluateTeam import Ui_Dialog

    # db connection
    cricket_db = sqlite3.connect('cricket.db')
    cricket_db_cursor = cricket_db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    FantasyCricket = QtWidgets.QMainWindow()
    ui = Ui_FantasyCricket()
    ui.setupUi(FantasyCricket)
    FantasyCricket.show()
    sys.exit(app.exec_())
