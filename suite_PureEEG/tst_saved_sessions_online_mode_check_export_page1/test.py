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
        
    #Export
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").text), "Page : 1")
    if test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ") : 
        clickButton(waitForObject(":RecordedSession.exportBt_QPushButton"))
        test.compare(str(waitForObjectExists(":Export as EDF_QPushButton").text), "Export as EDF")
        test.compare(str(waitForObjectExists(":Export as CSV_QPushButton").text), "Export as CSV")
    
        #export as EDF
        clickButton(waitForObject(":Export as EDF_QPushButton"))
        waitForObjectItem(":splitter.sidebar_QSidebar", "My Computer")
        clickItem(":splitter.sidebar_QSidebar", "My Computer", 61, 17, 0, Qt.LeftButton)
        waitForObjectItem(":splitter.sidebar_QSidebar", "Tu")
        clickItem(":splitter.sidebar_QSidebar", "Tu", 38, 12, 0, Qt.LeftButton)
        waitForObjectItem(":splitter.sidebar_QSidebar", "Tu")
        clickItem(":splitter.sidebar_QSidebar", "Tu", 39, 16, 0, Qt.LeftButton)
        waitForObjectItem(":stackedWidget.treeView_QTreeView", "Desktop")
        clickItem(":stackedWidget.treeView_QTreeView", "Desktop", 55, 6, 0, Qt.LeftButton)
        clickButton(waitForObject(":QFileDialog.Choose_QPushButton"))
        clickButton(waitForObject(":RecordedSession.exportBt_QPushButton"))
        
        #Export as CSV
        clickButton(waitForObject(":Export as CSV_QPushButton"))
        waitForObjectItem(":splitter.sidebar_QSidebar", "Tu")
        clickItem(":splitter.sidebar_QSidebar", "Tu", 41, 16, 0, Qt.LeftButton)
        waitForObjectItem(":stackedWidget.treeView_QTreeView", "Desktop")
        clickItem(":stackedWidget.treeView_QTreeView", "Desktop", 54, 7, 0, Qt.LeftButton)
        clickButton(waitForObject(":QFileDialog.Choose_QPushButton"))
        sendEvent("QMoveEvent", waitForObject(":RecordedSession_RecordedSession"), 423, 134, 625, 152)
        snooze(3)
   