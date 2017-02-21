# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    snooze(3)
    
    #Sign In
    clickButton(waitForObject(":MainWindow.signInBt_QPushButton"))
    mouseClick(waitForObject(":SignInForm.signInName_QLineEdit"), 33, 20, 0, Qt.LeftButton)
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "thuyvy")
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "<Tab>")
    type(waitForObject(":SignInForm.signInPass_QLineEdit"), "Thuyvy12")
    clickButton(waitForObject(":SignInForm.signInBt_QPushButton"))
    snooze(10)
    
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    #test Replay, export, remove from local is unactive
    if test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;") :
        test.compare(str(waitForObjectExists(":RecordedSession.downloadBt_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")
        test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
        clickButton(waitForObject(":RecordedSession.downloadBt_QPushButton"))
        snooze(10)
    else: 
        #if the session is downloaded, active buttons again
        test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
        test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
