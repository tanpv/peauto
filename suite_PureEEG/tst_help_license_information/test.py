# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickButton(waitForObject(":MainWindow.menuPushButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.helpMenuButton_QPushButton"))
    waitForObjectItem(":menuGroupBox.helpListWidget_QListWidget", "                   License Information")
    clickItem(":menuGroupBox.helpListWidget_QListWidget", "                   License Information", 78, 16, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":licenseInfoForm.label_QLabel").styleSheet), "font: 11pt \"Sans Serif\";\ncolor: rgb(0, 0, 0);\nfont: bold")
    #check text
    test.compare(str(waitForObjectExists(":licenseInfoForm.label_QLabel").text), "License Information")
    test.compare(str(waitForObjectExists(":licenseInfoForm.information_QLabel").styleSheet), "font: 10pt \"Sans Serif\";\ncolor: rgb(0, 0, 0);")
    #test.compare(str(waitForObjectExists(":licenseInfoForm.information_QLabel").text), " Mode: Online \n User:  \n Headset list: ALL \n Subscription from: 2016-05-13 \n Subscription to: 2017-12-31                            \n Allocated quota: 1967 \n Used quota: 157")
