# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyGame.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 583)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 811, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 795, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.t1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t1.setFont(font)
        self.t1.setEnabled(False)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.t2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t2.setFont(font)
        self.t2.setEnabled(False)
        self.t2.setObjectName("t2")
        self.horizontalLayout.addWidget(self.t2)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.t3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t3.setFont(font)
        self.t3.setEnabled(False)
        self.t3.setObjectName("t3")
        self.horizontalLayout.addWidget(self.t3)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.t4 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t4.setFont(font)
        self.t4.setEnabled(False)
        self.t4.setObjectName("t4")
        self.horizontalLayout.addWidget(self.t4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 120, 271, 411))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.PtsUsd = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PtsUsd.setFont(font)
        self.PtsUsd.setObjectName("PtsUsd")
        self.horizontalLayout_3.addWidget(self.PtsUsd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.Tname = QtWidgets.QLabel(self.groupBox_3)
        self.Tname.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.Tname.setFont(font)
        self.Tname.setAlignment(QtCore.Qt.AlignCenter)
        self.Tname.setObjectName("Tname")
        self.gridLayout.addWidget(self.Tname, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.list2 = QtWidgets.QListWidget(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list2.setFont(font)
        self.list2.setObjectName("list2")
        self.list2.itemDoubleClicked.connect(self.removelist2)
        self.verticalLayout.addWidget(self.list2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 120, 271, 411))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.PtsAvl = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PtsAvl.setFont(font)
        self.PtsAvl.setObjectName("PtsAvl")
        self.horizontalLayout_4.addWidget(self.PtsAvl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget2)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb1 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_2.addWidget(self.rb1)
        spacerItem4 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.rb2 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_2.addWidget(self.rb2)
        spacerItem5 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.rb3 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rb3.setFont(font)
        self.rb3.setAutoFillBackground(False)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_2.addWidget(self.rb3)
        spacerItem6 = QtWidgets.QSpacerItem(13, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.rb4 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rb4.setFont(font)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_2.addWidget(self.rb4)
        self.rb1.toggled.connect(self.ctg)
        self.rb2.toggled.connect(self.ctg)
        self.rb3.toggled.connect(self.ctg)
        self.rb4.toggled.connect(self.ctg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.list1 = QtWidgets.QListWidget(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list1.setFont(font)
        self.list1.setAutoScroll(True)
        self.list1.setObjectName("list1")
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.verticalLayout_2.addWidget(self.list1)
        self.layoutWidget.raise_()
        self.groupBox.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.customContextMenuRequested.connect(self.context_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Internshala Premier League"))
        self.groupBox.setTitle(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsmen"))
        self.t1.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Bowlers"))
        self.t2.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Allrounders"))
        self.t3.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper"))
        self.t4.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Points Used :"))
        self.PtsUsd.setText(_translate("MainWindow", "####"))
        self.Tname.setText(_translate("MainWindow", " Team_name"))
        self.label.setText(_translate("MainWindow", "Points Available :"))
        self.PtsAvl.setText(_translate("MainWindow", "####"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOWL"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def menufunction(self, action):
        txt=(action.text())
        if txt=="NEW Team":
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.Tname.setText("Team_name")
            self.showstatus()
            text, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Internshala Premier League', 'Enter name of team:')
            if ok:
                self.Tname.setText(str(text))
        if txt=="SAVE Team":
            selected=""
            count=self.list2.count()
            for i in range(count):
                selected=selected+self.list2.item(i).text()
                if i<count-1:
                    selected=selected+","
            self.save_Team(self.Tname.text(),selected,self.used)
        if txt=="OPEN Team":
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.Tname.setText("Team_name")
            self.showstatus()
            self.open_Team()
        if txt=="EVALUATE Team":
            from EvaluateScore import Mini_Ui
            Dialog = QtWidgets.QDialog()
            ui = Mini_Ui()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

    def save_Team(self,nm,string,val):
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Required 11 Players")
            return
        sql="INSERT INTO teams (name, players, value) VALUES ('"+nm+"','"+string+"','"+str(val)+"');"
        try:
            cur=conn.execute(sql)
            conn.commit()
            self.showdlg("Team Saved Successfully")
        except:
            self.showdlg("Operation Error")
            conn.rollback()

    def open_Team(self):
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])
        team, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Internshala Premier League",
                                                  "Choose a team", teams, 0, False)
        if ok and team:
            self.Tname.setText(team)
        sql1="select players, value from teams where name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.list2.addItems(selected)
        self.used=row[1]
        self.avl=1000-row[1]
        count=self.list2.count()
        for i in range(count):
            player=self.list2.item(i).text()
            sql="select ctg from stats where player='"+player+"'"
            cur=conn.execute(sql)
            row=cur.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1
        self.showstatus()
        
    def context_menu(MainWindow):
        MainWindow.menu = QtWidgets.QMenu()
        
    def ctg(self):
        ctgr=''
        if self.rb1.isChecked()==True:ctgr='BAT'
        if self.rb2.isChecked()==True:ctgr='BWL'
        if self.rb3.isChecked()==True:ctgr='AR'
        if self.rb4.isChecked()==True:ctgr='WK'
        self.fillList(ctgr)

    def fillList(self,ctgr):
        if self.Tname.text()=='Team_name':
            self.showdlg("Enter name of team")
            return
        self.list1.clear()
        cursor = conn.execute("SELECT player from stats WHERE ctg='"+ctgr+"'")
        for row in cursor:
            selected=[]
            for i in range(self.list2.count()):
                selected.append(self.list2.item(i).text())
            if row[0] not in selected:self.list1.addItem(row[0])
                
    def criteria(self,ctgr,item):
        msg=''
        if ctgr=="BAT" and self.bat>=4:msg="Batsmen not more than 4"
        if ctgr=="BWL" and self.bwl>=4:msg="Bowlers not more than 4"
        if ctgr=="AR" and self.ar>=2:msg="Allrounders not more than 2"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
        if self.avl<=0:msg = 'You have exhausted your points'
        if msg!='':
            self.showdlg(msg)
            return False
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BWL":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1
        cursor = conn.execute("SELECT player,value from stats WHERE player='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl-int(row[1])
        self.used=self.used+int(row[1])
        return True
    
    def showstatus(self):
        self.t1.setText(str(self.bat))
        self.t2.setText(str(self.bwl))
        self.t3.setText(str(self.ar))
        self.t4.setText(str(self.wk))
        self.PtsAvl.setText(str(self.avl))
        self.PtsUsd.setText(str(self.used))

    def removelist1(self, item):
        ctgr=''
        if self.rb1.isChecked()==True:ctgr='BAT'
        if self.rb2.isChecked()==True:ctgr='BWL'
        if self.rb3.isChecked()==True:ctgr='AR'
        if self.rb4.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr, item)
        if ret==True:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.showstatus()

    def showdlg(self, msg):
        Dialog = QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Internshala Premier League")
        ret=Dialog.exec()

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        cursor = conn.execute("SELECT player,value,ctg from stats WHERE player='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.rb1.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.rb2.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.rb3.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.rb4.isChecked()==True:self.list1.addItem(item.text())
        self.showstatus()    
            
if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('league.db')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    conn.close()
