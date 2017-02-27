# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    #login offline
    clickButton(waitForObject(":MainWindow.offlineModebt_QPushButton"))
    mouseClick(waitForObject(":signInOfflineMode.signInName_QLineEdit"), 113, 9, 0, Qt.LeftButton)
    type(waitForObject(":signInOfflineMode.signInName_QLineEdit"), "thuyvy")
    clickButton(waitForObject(":signInOfflineMode.signInOffBt_QPushButton"))
    snooze(5)
    #check save session offline
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    #check name of column
    test.compare(waitForObjectExists(":SubjectID_HeaderViewItem").text, "SubjectID")
    test.compare(waitForObjectExists(":RecordID_HeaderViewItem").text, "RecordID")
    test.compare(waitForObjectExists(":Start Time_HeaderViewItem").text, "Start Time")
    test.compare(waitForObjectExists(":Duration (s)_HeaderViewItem").text, "Duration (s)")
    test.compare(waitForObjectExists(":Local_HeaderViewItem").text, "Local")
    test.compare(waitForObjectExists(":Cloud_HeaderViewItem").text, "Cloud")
    
    #check button
    test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").text), "Replay Session")
    test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
    test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").text), "Page : 1")
    test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").styleSheet), "font: bold 12px ;\n")
    test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
    test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").text), "Export")
    test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").text), "Remove from Local")
    test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
    
    #remove from local
    row_start = waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").rowCount
    if row_start>0:
        clickButton(waitForObject(":RecordedSession.removeDownloadbt_QPushButton"))
        test.compare(str(waitForObjectExists(":qt_msgbox_label_QLabel").text), "Are you sure you want to delete the session? It cannot be undone.")
        test.compare(str(waitForObjectExists(":Yes_QPushButton").text), "&Yes")
        test.compare(str(waitForObjectExists(":No_QPushButton").text), "&No")
        clickButton(waitForObject(":Yes_QPushButton"))
        sendEvent("QCloseEvent", waitForObject(":RecordedSession_RecordedSession"))
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    test.compare(waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").columnCount, 6)
    test.compare(waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").rowCount, row_start-1)
