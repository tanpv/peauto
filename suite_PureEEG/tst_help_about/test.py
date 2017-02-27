# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickButton(waitForObject(":MainWindow.signInBt_QPushButton"))
    #Login
    mouseClick(waitForObject(":SignInForm.signInName_QLineEdit"), 69, 18, 0, Qt.LeftButton)
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "thuyvy")
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "<Tab>")
    type(waitForObject(":SignInForm.signInPass_QLineEdit"), "Thuyvy12")
    clickButton(waitForObject(":SignInForm.signInBt_QPushButton"))
    snooze(7)
    #check menu Help
    clickButton(waitForObject(":menuGroupBox.helpMenuButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.helpPushButton_QPushButton"))
    waitForObjectItem(":menuGroupBox.helpListWidget_QListWidget", "                   About Xavier Pure\\.EEG")
    clickItem(":menuGroupBox.helpListWidget_QListWidget", "                   About Xavier Pure\\.EEG", 170, 7, 0, Qt.LeftButton)
    #test.compare(str(waitForObjectExists(":aboutClass.emotivLabel_QLabel").text), "<b>Emotiv Xavier Pure.EEG </b> <br> 							Version: 3.4.3. Build: b835800 <br>                            <b>Hardware information:</b><br>User 0: Headset [0x1e00], Dongle [0x6ff], \n <br>Serial [0x000055EE] \n <br></p> <br>                            @2016 Emotiv Inc.<br> 							All rights reserved")
    test.compare(str(waitForObjectExists(":aboutClass.warningLabel_QLabel").text), "WARNING: This computer program is protected by \n copyright law and international treaties.\n Unauthorized reproduction or distribution of this \n program, or any portion of it, may result in severe \n civil and criminal penalties, and will be prosecuted \n under the maximum extent possible under law.")
    test.compare(str(waitForObjectExists(":aboutClass.OkButton_QPushButton").styleSheet), "\nfont: bold 12px ;\ncolor:white;\nbackground:black;")
    test.compare(str(waitForObjectExists(":aboutClass.OkButton_QPushButton").text), "OK")
    clickButton(waitForObject(":aboutClass.OkButton_QPushButton"))