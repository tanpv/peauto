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
   
    if str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet)== "background: rgb(179, 179, 179); font: bold 12px ; color:white;":
        test.compare(str(waitForObjectExists(":RecordedSession.downloadBt_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")
        #test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
        test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").text), "Replay Session")
        test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").text), "Export")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").text), "Remove from Local")
        test.compare(str(waitForObjectExists(":RecordedSession.downloadBt_QPushButton").text), "Download from Cloud")
        clickButton(waitForObject(":RecordedSession.downloadBt_QPushButton"))
        snooze(10)
        #stop download
        test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
        test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "background: rgb(179, 179, 179); font: bold 12px ; color:white;")
      
    #if (test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")):
    else:
        test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
        test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
        test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").text), "Replay Session")
        test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").text), "Export")
        test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").text), "Remove from Local")
        test.compare(str(waitForObjectExists(":RecordedSession.downloadBt_QPushButton").text), "Download from Cloud")
