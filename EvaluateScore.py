# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateScore.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Mini_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Internshala Premier League")
        Dialog.resize(480, 434)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 481, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 40, 451, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.combo1 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo1.setFont(font)
        self.combo1.setObjectName("combo1")
        import sqlite3
        conn = sqlite3.connect('league.db')
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.combo1.addItem(str(row[0]))
        conn.close()
        self.horizontalLayout.addWidget(self.combo1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.combo2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo2.setFont(font)
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("")
        #self.combo2.addItem("")
        #self.combo2.addItem("")
        #self.combo2.addItem("")
        #self.combo2.addItem("")
        self.horizontalLayout.addWidget(self.combo2)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 80, 441, 311))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.list3 = QtWidgets.QListWidget(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list3.setFont(font)
        self.list3.setObjectName("list3")
        self.verticalLayout.addWidget(self.list3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.list4 = QtWidgets.QListWidget(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list4.setFont(font)
        self.list4.setObjectName("list4")
        self.verticalLayout_2.addWidget(self.list4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 400, 401, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b1 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.evaluate)
        self.horizontalLayout_3.addWidget(self.b1)
        spacerItem1 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.score = QtWidgets.QLabel(self.layoutWidget2)
        self.score.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.horizontalLayout_3.addWidget(self.score)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def evaluate(self):
        team=self.combo1.currentText()
        self.list4.clear()
        self.list3.clear()
        import sqlite3
        conn = sqlite3.connect('league.db')
        sql1="select players, value from teams where name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.list3.addItems(selected)
        teamttl=0
        self.list4.clear()
        match=self.combo2.currentText()
        for i in range(self.list3.count()):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.list3.item(i).text()
            cursor=conn.execute("select * from "+match+" where player='"+nm+"'")
            row=cursor.fetchone()
            batscore=int(row[1]/2)
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row[1]>0:
                sr=row[1]/row[2]
                if sr>=80 and sr<100: batscore+=2
                if sr>=100:batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore+10
            if row[7]>0:
                er=6*row[7]/row[5]
                if er<=2: bowlscore=bowlscore+10
                if er>2 and er<=3.5: bowlscore=bowlscore+7
                if er>3.5 and er<=4.5: bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10
            ttl=batscore+bowlscore+fieldscore
            self.list4.addItem(str(ttl))
            teamttl=teamttl+ttl
        self.score.setText(str(teamttl))    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Team"))
        self.label_4.setText(_translate("Dialog", "Select Team"))
        self.label_3.setText(_translate("Dialog", "Select Match"))
        self.combo2.setItemText(0, _translate("Dialog", "Match1"))
        self.combo2.setItemText(1, _translate("Dialog", "Match2"))
        self.combo2.setItemText(2, _translate("Dialog", "Match3"))
        self.combo2.setItemText(3, _translate("Dialog", "Match4"))
        self.combo2.setItemText(4, _translate("Dialog", "Match5"))
        self.label_2.setText(_translate("Dialog", "Players"))
        self.label_5.setText(_translate("Dialog", "Points"))
        self.b1.setText(_translate("Dialog", "Calculate Score"))
        self.score.setText(_translate("Dialog", "00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Mini_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
