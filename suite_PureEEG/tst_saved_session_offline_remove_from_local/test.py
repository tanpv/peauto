# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickButton(waitForObject(":MainWindow.offlineModebt_QPushButton"))
    mouseClick(waitForObject(":signInOfflineMode.signInName_QLineEdit"), 113, 9, 0, Qt.LeftButton)
    type(waitForObject(":signInOfflineMode.signInName_QLineEdit"), "thuyvy")
    clickButton(waitForObject(":signInOfflineMode.signInOffBt_QPushButton"))
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    test.compare(waitForObjectExists(":SubjectID_HeaderViewItem").text, "SubjectID")
    test.compare(waitForObjectExists(":RecordID_HeaderViewItem").text, "RecordID")
    test.compare(waitForObjectExists(":Start Time_HeaderViewItem").text, "Start Time")
    test.compare(waitForObjectExists(":Duration (s)_HeaderViewItem").text, "Duration (s)")
    test.compare(waitForObjectExists(":Local_HeaderViewItem").text, "Local")
    test.compare(waitForObjectExists(":Cloud_HeaderViewItem").text, "Cloud")
    test.compare(waitForObjectExists(":listFileInfoTb.0_0_QModelIndex").row, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.0_0_QModelIndex").text, "autotest-1-13.02.17-14.58.16")
    test.compare(waitForObjectExists(":listFileInfoTb.0_0_QModelIndex").column, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").row, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").text, "")
    test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").column, 1)
    test.compare(waitForObjectExists(":listFileInfoTb.0_2_QModelIndex").row, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.0_2_QModelIndex").column, 2)
    test.compare(waitForObjectExists(":listFileInfoTb.0_2_QModelIndex").text, "")
    test.compare(waitForObjectExists(":listFileInfoTb.0_3_QModelIndex").column, 3)
    test.compare(waitForObjectExists(":listFileInfoTb.0_3_QModelIndex").row, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.0_3_QModelIndex").text, "")
    test.compare(waitForObjectExists(":listFileInfoTb.1_0_QModelIndex").row, 1)
    test.compare(waitForObjectExists(":listFileInfoTb.1_0_QModelIndex").column, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.1_0_QModelIndex").text, "autotest-1-13.02.17-15.05.39")
    clickButton(waitForObject(":RecordedSession.removeDownloadbt_QPushButton"))
    sendEvent("QCloseEvent", waitForObject(":_QMessageBox"))
    test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").text), "Replay Session")
    test.compare(str(waitForObjectExists(":RecordedSession.playSessionBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
    test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").text), "Page : 1")
    test.compare(str(waitForObjectExists(":RecordedSession.pageLb_QLabel").styleSheet), "font: bold 12px ;\n")
    test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
    test.compare(str(waitForObjectExists(":RecordedSession.exportBt_QPushButton").text), "Export")
    test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").text), "Remove from Local")
    test.compare(str(waitForObjectExists(":RecordedSession.removeDownloadbt_QPushButton").styleSheet), "font: bold 12px ; color:white; background:black; ")
    test.compare(waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").columnCount, 6)
    test.compare(waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").rowCount, 4)
    sendEvent("QMouseEvent", waitForObject(":RecordedSession.removeDownloadbt_QPushButton"), QEvent.MouseButtonPress, 63, 16, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":RecordedSession.removeDownloadbt_QPushButton"), QEvent.MouseButtonRelease, 63, 16, Qt.LeftButton, 0, 0)
    test.compare(str(waitForObjectExists(":qt_msgbox_label_QLabel").text), "Are you sure you want to delete the session? It cannot be undone.")
    test.compare(str(waitForObjectExists(":Yes_QPushButton").text), "&Yes")
    test.compare(str(waitForObjectExists(":No_QPushButton").text), "&No")
    clickButton(waitForObject(":Yes_QPushButton"))
    test.compare(waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").columnCount, 6)
    test.compare(waitForObjectExists(":RecordedSession.listFileInfoTb_QTableWidget").rowCount, 3)
