# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickButton(waitForObject(":MainWindow.signInBt_QPushButton"))
    mouseClick(waitForObject(":SignInForm.signInName_QLineEdit"), 86, 22, 0, Qt.LeftButton)
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "tpv")
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "<Tab>")
    type(waitForObject(":SignInForm.signInPass_QLineEdit"), "Aaa12345678")
    clickButton(waitForObject(":SignInForm.signInBt_QPushButton"))
    test.compare(str(waitForObjectExists(":MainWindow.userNameLb_QPushButton").text), "tpv")
