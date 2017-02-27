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
    snooze(10)
    #check form License Information
    clickButton(waitForObject(":menuGroupBox.helpMenuButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.helpMenuButton_QPushButton_2"))
    waitForObjectItem(":menuGroupBox.helpListWidget_QListWidget", "                   License Information")
    clickItem(":menuGroupBox.helpListWidget_QListWidget", "                   License Information", 124, 4, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":licenseInfoForm.label_QLabel").styleSheet), "font: 11pt \"Sans Serif\";\ncolor: rgb(0, 0, 0);\nfont: bold")
    #check text
    test.compare(str(waitForObjectExists(":licenseInfoForm.label_QLabel").text), "License Information")
    test.compare(str(waitForObjectExists(":licenseInfoForm.information_QLabel").styleSheet), "font: 10pt \"Sans Serif\";\ncolor: rgb(0, 0, 0);")
    #test.compare(str(waitForObjectExists(":licenseInfoForm.information_QLabel").text), " Mode: Online \n User:  \n Headset list: ALL \n Subscription from: 2016-05-13 \n Subscription to: 2017-12-31                            \n Allocated quota: 1967 \n Used quota: 157")
