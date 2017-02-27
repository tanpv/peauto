# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickButton(waitForObject(":MainWindow.signInBt_QPushButton"))
    #Login
    mouseClick(waitForObject(":SignInForm.signInName_QLineEdit"), 69, 18, 0, Qt.LeftButton)
    name= "thuyvy"
    type(waitForObject(":SignInForm.signInName_QLineEdit"), name)
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "<Tab>")
    passw= "Thuyvy12"
    type(waitForObject(":SignInForm.signInPass_QLineEdit"), passw)
    clickButton(waitForObject(":SignInForm.signInBt_QPushButton"))
    #wait for 10 seconds
    snooze(10)
    #check EmotivID
    sendEvent("QMoveEvent", waitForObject(":MainWindow_MainUI"), 152, 0, 390, 0)
    test.compare(str(waitForObjectExists(":MainWindow.userNameLb_QPushButton").text), name)
    #check Sign Out show
    test.compare(str(waitForObjectExists(":MainWindow.userNameLb_QPushButton").styleSheet), "border:1px solid white;\nfont: 12px;")
    test.compare(str(waitForObjectExists(":MainWindow.signOutBt_QPushButton").text), "Sign Out")
    test.compare(str(waitForObjectExists(":MainWindow.signOutBt_QPushButton").styleSheet), "border:1px solid white;\nfont: 12px;")
      #check Logtex
    #test.compare(str(waitForObjectExists(":groupBox.LogBox_QTextEdit").styleSheet), "QTextEdit{\nbackground:#4a4e54;color:white;\n\nfont: 12px;\n}\nQScrollBar{\nbackground-color:#4a4d52;\nwidth:5px;\n}\n QScrollBar::handle{\nborder:1px solid #ffffff;\nborder-radius:2px;\n     background: #ffffff;\nmax-width:10px;\n }\n\n")
    #test.compare(str(waitForObjectExists(":groupBox.LogBox_QTextEdit").html), "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12px; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Headset (user) 0 has connected.</p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connecting to Emotiv Cloud...</p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Logged in as thuyvy</p></body></html>")
    #test.compare(str(waitForObjectExists(":groupBox.LogBox_QTextEdit").textInteractionFlags), "Qt::TextSelectableByMouse | Qt::TextSelectableByKeyboard | Qt::TextEditable | Qt::TextEditorInteraction | Qt::TextBrowserInteraction")
    test.compare(str(waitForObjectExists(":groupBox.LogBox_QTextEdit").plainText), "Headset (user) 0 has connected.\nConnecting to Emotiv Cloud...\nLogged in as thuyvy")
