# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    snooze(2)
    #Sign In
    clickButton(waitForObject(":MainWindow.signInBt_QPushButton"))
    mouseClick(waitForObject(":SignInForm.signInName_QLineEdit"), 33, 20, 0, Qt.LeftButton)
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "thuyvy")
    type(waitForObject(":SignInForm.signInName_QLineEdit"), "<Tab>")
    type(waitForObject(":SignInForm.signInPass_QLineEdit"), "Thuyvy12")
    clickButton(waitForObject(":SignInForm.signInBt_QPushButton"))
    snooze(10)
    
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").text), "Page : 1")
    if test.compare(waitForObjectExists(":10_HeaderViewItem").text, "10") : 
        test.compare(waitForObjectExists(":10_HeaderViewItem").type, "HeaderViewItem")
        test.compare(waitForObjectExists(":10_HeaderViewItem").visible, True)
        test.compare(str(waitForObjectExists(":RecordedSession.nextBt_QPushButton").styleSheet), "background-image: url(:/Resources/next.png);")
        #test.passes("co page 2",)
        #go to page 2
        clickButton(waitForObject(":RecordedSession.nextBt_QPushButton"))
        test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").text), "Page : 2")
        test.compare(str(waitForObjectExists(":RecordedSession.preBt_QPushButton").styleSheet), "background-image: url(:/Resources/previous.png);")
        test.compare(str(waitForObjectExists(":RecordedSession.nextBt_QPushButton").styleSheet), "background-image: url(:/Resources/next.png);")
    #export as EDF
        
        #sendEvent("QMouseEvent", waitForObject(":RecordedSession.exportBt_QPushButton"), QEvent.MouseButtonPress, 39, 9, Qt.LeftButton, 1, 0)
        #sendEvent("QMouseEvent", waitForObject(":RecordedSession.exportBt_QPushButton"), QEvent.MouseButtonRelease, 39, 9, Qt.LeftButton, 0, 0)
        clickButton(waitForObject(":RecordedSession.exportBt_QPushButton"))
        
        clickButton(waitForObject(":Export as EDF_QPushButton"))
        
        path = "C:\Users\Tu\Desktop"
        type(waitForObject(":fileNameEdit_QLineEdit"), path)
        clickButton(waitForObject(":QFileDialog.Choose_QPushButton"))
        snooze(5)
        
     #Export as CSV
        clickButton(waitForObject(":RecordedSession.exportBt_QPushButton"))
         
        clickButton(waitForObject(":Export as CSV_QPushButton"))
        type(waitForObject(":fileNameEdit_QLineEdit"), path)
        clickButton(waitForObject(":QFileDialog.Choose_QPushButton"))
        sendEvent("QMoveEvent", waitForObject(":RecordedSession_RecordedSession"), 423, 134, 625, 152)
        snooze(3)   