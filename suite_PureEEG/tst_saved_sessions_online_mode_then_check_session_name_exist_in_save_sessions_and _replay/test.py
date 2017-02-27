# -*- coding: utf-8 -*-
import time
import os
import sys
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
    # check  online mode properly?
    test.compare(str(waitForObjectExists(":MainWindow.userNameLb_QPushButton").text), "thuyvy")
    test.compare(str(waitForObjectExists(":MainWindow.modeSignin_QPushButton").styleSheet), "\nborder:1px solid black;\nborder-radius:5px;\ncolor:white;\nbackground:black;\nfont: 12px;")
    test.compare(str(waitForObjectExists(":MainWindow.modeSignin_QPushButton").text), "Online")
    
    # Save recording
    clickButton(waitForObject(":MainWindow.SaveData_QPushButton_2"))
    type(waitForObject(":RecordConfigClass.subjectidLe_QLineEdit"), "autotest")
    type(waitForObject(":RecordConfigClass.subjectidLe_QLineEdit"), "<Tab>")
    type(waitForObject(":RecordConfigClass.recordidLe_QLineEdit"), "1")
    
    test.compare(str(waitForObjectExists(":RecordConfigClass.subjectidLe_QLineEdit").displayText), "autotest")
    test.compare(str(waitForObjectExists(":RecordConfigClass.subjectidLe_QLineEdit").text), "autotest")
    SubjectID = str(waitForObjectExists(":RecordConfigClass.subjectidLe_QLineEdit").text)
    
    test.compare(str(waitForObjectExists(":RecordConfigClass.recordidLe_QLineEdit").text), "1")
    RecordID = str(waitForObjectExists(":RecordConfigClass.recordidLe_QLineEdit").text)
    test.compare(str(waitForObjectExists(":RecordConfigClass.recordidLe_QLineEdit").displayText), "1")
    snooze(3)
    
    test.compare(str(waitForObjectExists(":RecordConfigClass.label_2_QLabel").text), "File name :")
    test.compare(str(waitForObjectExists(":RecordConfigClass.label_3_QLabel").text), "Subject ID :")
    test.compare(str(waitForObjectExists(":RecordConfigClass.label_4_QLabel").text), "Record ID :")
    test.compare(str(waitForObjectExists(":RecordConfigClass.label_6_QLabel").text), "Date :")
    test.compare(str(waitForObjectExists(":RecordConfigClass.label_5_QLabel").text), "Time :")
    snooze(2)
    clickButton(waitForObject(":RecordConfigClass.startBt_QPushButton"))
    snooze(30)
    clickButton(waitForObject(":RecordConfigClass.startBt_QPushButton"))
    snooze(5)
        
    # Check save sessions
    clickButton(waitForObject(":MainWindow.savedSessionsBt_QPushButton"))
    test.compare(waitForObjectExists(":SubjectID_HeaderViewItem").text, "SubjectID")
    #test.compare(waitForObjectExists(":listFileInfoTb.0_0_QModelIndex").text, "autotest")
    test.compare(waitForObjectExists(":listFileInfoTb.0_0_QModelIndex").text, SubjectID)
    
    test.compare(waitForObjectExists(":RecordID_HeaderViewItem").text, "RecordID")
    test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").row, 0)
    #test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").text, "1")
    test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").text, RecordID)
    test.compare(waitForObjectExists(":listFileInfoTb.0_1_QModelIndex").column, 1)
    
    test.compare(waitForObjectExists(":Start Time_HeaderViewItem").text, "Start Time")
    test.compare(waitForObjectExists(":listFileInfoTb.0_2_QModelIndex").row, 0)
    test.compare(waitForObjectExists(":listFileInfoTb.0_2_QModelIndex").column, 2)
   
    
    test.compare(waitForObjectExists(":Duration (s)_HeaderViewItem").text, "Duration (s)")
    test.compare(waitForObjectExists(":listFileInfoTb.0_3_QModelIndex").column, 3)
    test.compare(waitForObjectExists(":listFileInfoTb.0_3_QModelIndex").row, 0)
    #test.compare(waitForObjectExists(":listFileInfoTb.0_3_QModelIndex").text, "00:00:30")
    
    test.compare(waitForObjectExists(":Local_HeaderViewItem").text, "Local")
    test.compare(waitForObjectExists(":Cloud_HeaderViewItem").text, "Cloud")
       
    # continue with test play back    
    clickButton(waitForObject(":RecordedSession.playSessionBt_QPushButton"))
    # after click replay, add verify for playback controller
       
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.pushButton_QPushButton").text), "Open File")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.pushButton_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")
    
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_QLabel").text), "File path :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_2_QLabel").text), "Subject ID :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.subjectIDLine_QLineEdit_2").text), SubjectID)
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.subjectIDLine_QLineEdit_2").displayText), SubjectID)
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_3_QLabel").text), "Record ID :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.recordIDLine_QLineEdit").displayText), RecordID)
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.recordIDLine_QLineEdit").text), RecordID)
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_4_QLabel").text), "Date :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_5_QLabel").text), "Start time :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.playButton_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.playButton_QPushButton").text), "Play")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.pauseButton_QPushButton").text), "Pause")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.pauseButton_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.stopButton_QPushButton").text), "Stop")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.stopButton_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")


    clickButton(waitForObject(":PlaybackControllerClass.playButton_QPushButton"))
    snooze(10)
    clickButton(waitForObject(":PlaybackControllerClass.pauseButton_QPushButton"))
    snooze(3)
    clickButton(waitForObject(":PlaybackControllerClass.stopButton_QPushButton"))
