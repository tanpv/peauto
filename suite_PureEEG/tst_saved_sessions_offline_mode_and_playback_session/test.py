# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickButton(waitForObject(":MainWindow.offlineModebt_QPushButton"))
    mouseClick(waitForObject(":signInOfflineMode.signInName_QLineEdit"), 77, 19, 0, Qt.LeftButton)
    type(waitForObject(":signInOfflineMode.signInName_QLineEdit"), "thuyvy")
    clickButton(waitForObject(":signInOfflineMode.signInOffBt_QPushButton"))
            
    # Save recording
    clickButton(waitForObject(":MainWindow.SaveData_QPushButton"))
    mouseClick(waitForObject(":RecordConfigClass.subjectidLe_QLineEdit"), 106, 19, 0, Qt.LeftButton)
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
    
    test.compare(waitForObjectExists(":RecordID_HeaderViewItem").text, "RecordID")
    
    
    
    test.compare(waitForObjectExists(":Start Time_HeaderViewItem").text, "Start Time")
    
   
    
    test.compare(waitForObjectExists(":Duration (s)_HeaderViewItem").text, "Duration (s)")
   
    test.compare(waitForObjectExists(":Local_HeaderViewItem").text, "Local")
    test.compare(waitForObjectExists(":listFileInfoTb_QCheckBox").checked, True)
    
    test.compare(waitForObjectExists(":Cloud_HeaderViewItem").text, "Cloud")
    
   
    # continue with test play back    
    clickButton(waitForObject(":RecordedSession.playSessionBt_QPushButton"))
    # after click replay, add verify for playback controller
       
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.pushButton_QPushButton").text), "Open File")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.pushButton_QPushButton").styleSheet), "font: bold 12px ;\ncolor:white;\nbackground:black;")
    
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_QLabel").text), "File path :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.label_2_QLabel").text), "Subject ID :")
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.subjectIDLine_QLineEdit").text), SubjectID)
    test.compare(str(waitForObjectExists(":PlaybackControllerClass.subjectIDLine_QLineEdit").displayText), SubjectID)
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

