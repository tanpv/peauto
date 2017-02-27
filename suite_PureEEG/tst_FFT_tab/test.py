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
    
    clickTab(waitForObject(":MainWindow.ModeEpocFrame_QTabWidget"), "FFT")
    
    # Check channel
    test.compare(str(waitForObjectExists(":FFT.label_7_QLabel").text), "Channel")
    mouseClick(waitForObject(":FFT.Channel_QComboBox"), 79, 12, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "AF3"), 5, 6, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "AF3")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "F7"), 11, 1, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "F7")
    snooze(1)
    
    sendEvent("QMouseEvent", waitForObject(":FFT.Channel_QComboBox"), QEvent.MouseButtonRelease, 49, -16, Qt.LeftButton, 0, 0)
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "F3"), 9, 3, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "F3")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "FC5"), 16, 5, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "FC5")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "T7"), 11, 3, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "T7")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "P7"), 15, 5, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "P7")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "O1"), 14, 3, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "O1")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "O2"), 10, 1, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "O2")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "P8"), 10, 1, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "P8")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "T8"), 11, 4, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "T8")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "FC6"), 23, 5, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "FC6")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "F4"), 12, 6, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "F4")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "F8"), 19, 5, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "F8")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Channel_QComboBox", "AF4"), 22, 5, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Channel_QComboBox").currentText), "AF4")
    snooze(1)
    
    # check amax,
    test.compare(str(waitForObjectExists(":FFT.label_8_QLabel").text), "amax")
    test.compare(str(waitForObjectExists(":FFT.amax_QSpinBox").text), "80")
    test.compare(waitForObjectExists(":FFT.amax_QSpinBox_2").singleStep, 1)
    
    spinUp(waitForObject(":FFT.amax_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.amax_QSpinBox").text), "81")
    snooze(1)
    
    spinDown(waitForObject(":FFT.amax_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.amax_QSpinBox").text), "80")
    snooze(1)
    
    #check amin
    test.compare(str(waitForObjectExists(":FFT.label_9_QLabel").text), "amin")
    test.compare(str(waitForObjectExists(":FFT.amin_QSpinBox").text), "-65")
    test.compare(waitForObjectExists(":FFT.amin_QSpinBox_2").singleStep, 1)
    
    spinUp(waitForObject(":FFT.amin_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.amin_QSpinBox").text), "-64")
    snooze(1)
    
    spinDown(waitForObject(":FFT.amin_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.amin_QSpinBox").text), "-65")
    snooze(1)
    
    #check fmax 
    test.compare(str(waitForObjectExists(":FFT.label_11_QLabel").text), "fmax")
    test.compare(str(waitForObjectExists(":FFT.fmax_QSpinBox").text), "64")
    test.compare(waitForObjectExists(":FFT.fmax_QSpinBox_2").singleStep, 1)
    
    spinDown(waitForObject(":FFT.fmax_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.fmax_QSpinBox").text), "63")
    snooze(1)
    
    spinUp(waitForObject(":FFT.fmax_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.fmax_QSpinBox").text), "64")
    snooze(1)
    
    #check fmin
    test.compare(str(waitForObjectExists(":FFT.label_10_QLabel").text), "fmin")
    test.compare(str(waitForObjectExists(":FFT.fmin_QSpinBox").text), "0")
    test.compare(waitForObjectExists(":FFT.fmin_QSpinBox_2").singleStep, 1)
    
    spinUp(waitForObject(":FFT.fmin_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.fmin_QSpinBox").text), "1")
    snooze(1)
    
    spinDown(waitForObject(":FFT.fmin_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.fmin_QSpinBox").text), "0")
    snooze(1)
    
    #check length
    test.compare(str(waitForObjectExists(":FFT.label_12_QLabel").text), "length")
    test.compare(str(waitForObjectExists(":FFT.length_QSpinBox").text), "256")
    test.compare(waitForObjectExists(":FFT.length_QSpinBox_2").singleStep, 1)
    
    spinUp(waitForObject(":FFT.length_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit").displayText), "257")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit").text), "257")
    snooze(1)
    
    spinDown(waitForObject(":FFT.length_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit").displayText), "256")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit").text), "256")
   
    test.compare(str(waitForObjectExists(":FFT.length_QSpinBox").text), "256")
    snooze(1)
       
    #check step
    test.compare(str(waitForObjectExists(":FFT.label_13_QLabel").text), "step")
    test.compare(str(waitForObjectExists(":FFT.step_QSpinBox").text), "23")
    test.compare(waitForObjectExists(":FFT.step_QSpinBox_2").singleStep, 1)
    
    spinUp(waitForObject(":FFT.step_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_2").displayText), "24")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_2").text), "24")
    snooze(1)
    
    spinDown(waitForObject(":FFT.step_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_2").displayText), "23")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_2").text), "23")
    snooze(1)
    
    #check dB
    test.compare(str(waitForObjectExists(":FFT.label_15_QLabel").text), "dB")
 
    test.compare(str(waitForObjectExists(":FFT.dbBox_QComboBox_2").currentText), "10")
    mouseClick(waitForObject(":FFT.dbBox_QComboBox_2"), 51, 15, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":FFT.dbBox_QComboBox_2", "20"), 29, 7, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.dbBox_QComboBox_2").currentText), "20")
    
    #check Windowing
    test.compare(str(waitForObjectExists(":FFT.label_14_QLabel").text), "Windowing")
    mouseClick(waitForObject(":FFT.Windowing_QComboBox"), 96, 12, 0, Qt.LeftButton)
    sendEvent("QMouseEvent", waitForObject(":FFT.Windowing_QComboBox"), QEvent.MouseButtonPress, 115, 245, Qt.LeftButton, 1, 0)
    test.compare(str(waitForObjectExists(":FFT.Windowing_QComboBox").currentText), "HANNING")
    
    sendEvent("QMouseEvent", waitForObject(":FFT.Windowing_QComboBox"), QEvent.MouseButtonPress, 91, 9, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":FFT.Windowing_QComboBox"), QEvent.MouseButtonRelease, 91, -20, Qt.LeftButton, 0, 0)
    mouseClick(waitForObjectItem(":FFT.Windowing_QComboBox", "HAMMING"), 34, 10, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Windowing_QComboBox").currentText), "HAMMING")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Windowing_QComboBox", "HANN"), 26, 1, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Windowing_QComboBox").currentText), "HANN")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Windowing_QComboBox", "BLACKMAN"), 47, 4, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Windowing_QComboBox").currentText), "BLACKMAN")
    snooze(1)
    
    mouseClick(waitForObjectItem(":FFT.Windowing_QComboBox", "RECTANGLE"), 51, 7, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":FFT.Windowing_QComboBox").currentText), "RECTANGLE")
    snooze(1)
    
    #check pmax
    test.compare(str(waitForObjectExists(":FFT.label_16_QLabel").text), "pmax")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_3").displayText), "0.10")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_3").text), "0.10")
    
    spinUp(waitForObject(":FFT.pmax_QDoubleSpinBox"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_3").text), "0.11")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_3").displayText), "0.11")
    snooze(1)
    
    spinDown(waitForObject(":FFT.pmax_QDoubleSpinBox"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_3").displayText), "0.10")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_3").text), "0.10")
    test.compare(waitForObjectExists(":FFT.pmax_QDoubleSpinBox").singleStep, 0.01)
    test.compare(waitForObjectExists(":FFT.pmax_QDoubleSpinBox").value, 0.1)
    snooze(1)
    
    #check pmin
    test.compare(str(waitForObjectExists(":FFT.label_17_QLabel").text), "pmin")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_4").text), "0.00")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_4").displayText), "0.00")
    
    spinUp(waitForObject(":FFT.pmin_QDoubleSpinBox"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_4").text), "0.01")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_4").displayText), "0.01")
    snooze(1)
    
    spinDown(waitForObject(":FFT.pmin_QDoubleSpinBox"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_4").text), "0.00")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_4").displayText), "0.00")
    test.compare(waitForObjectExists(":FFT.pmin_QDoubleSpinBox").singleStep, 0.01)
    test.compare(str(waitForObjectExists(":FFT.pmin_QDoubleSpinBox").text), "0.00")
    snooze(1)
    
    #check Auto Scale
    test.compare(str(waitForObjectExists(":FFT.pushButton_QPushButton").styleSheet), "color:white;\nfont:12px;\nbackground:black;")
    test.compare(str(waitForObjectExists(":FFT.pushButton_QPushButton").text), "Auto Scale")
    
    #check Custom Band
    test.compare(str(waitForObjectExists(":FFT.label_18_QLabel").text), "Custom Band")
    
    #lower
    test.compare(str(waitForObjectExists(":FFT.label_19_QLabel").text), "lower")
    test.compare(waitForObjectExists(":FFT.lower_QSpinBox_2").singleStep, 1)
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_5").displayText), "3")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_5").text), "3")
    
    spinUp(waitForObject(":FFT.lower_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_5").text), "1")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_5").displayText), "1")
    snooze(1)
    
    spinDown(waitForObject(":FFT.lower_QSpinBox_2"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_5").text), "0")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_5").displayText), "0")
    snooze(1)
    
    #upper
    test.compare(str(waitForObjectExists(":FFT.label_20_QLabel").text), "upper")
    test.compare(waitForObjectExists(":FFT.upper_QSpinBox").singleStep, 1)
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_6").displayText), "4")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_6").text), "4")
    
    spinUp(waitForObject(":FFT.upper_QSpinBox"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_6").displayText), "5")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_6").text), "5")
    snooze(1)
    
    spinDown(waitForObject(":FFT.upper_QSpinBox"))
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_6").displayText), "4")
    test.compare(str(waitForObjectExists(":FFT.qt_spinbox_lineedit_QLineEdit_6").text), "4")
    snooze(1)
    
    #check Power
    test.compare(str(waitForObjectExists(":FFT.label_delta_QLabel").styleSheet), "color:white;\nfont: bold 13px;")
    test.compare(str(waitForObjectExists(":FFT.label_delta_QLabel").text), "Delta\n(1-4Hz)")
    
    test.compare(str(waitForObjectExists(":FFT.label_theta_QLabel").styleSheet), "color:white;\nfont: bold 13px;")
    test.compare(str(waitForObjectExists(":FFT.label_theta_QLabel").text), "Theta\n(4-7Hz)")
    
    test.compare(str(waitForObjectExists(":FFT.label_alpha_QLabel").styleSheet), "color:white;\nfont: bold 13px;")
    test.compare(str(waitForObjectExists(":FFT.label_alpha_QLabel").text), "Alpha\n(7-13Hz)")
    
    test.compare(str(waitForObjectExists(":FFT.label_beta_QLabel").text), "Beta\n(13-30Hz)")
    test.compare(str(waitForObjectExists(":FFT.label_beta_QLabel").styleSheet), "color:white;\nfont: bold 13px;")
    
    test.compare(str(waitForObjectExists(":FFT.label_custom_QLabel").styleSheet), "color:white;\nfont: bold 13px;")
    test.compare(str(waitForObjectExists(":FFT.label_custom_QLabel").text), "Custom")
    
    