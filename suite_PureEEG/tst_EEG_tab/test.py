# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    snooze(3)
    if (test.compare(str(waitForObjectExists(":MainWindow.EPOCModeButton_QPushButton").styleSheet), "\nborder:1px solid black;\nborder-radius:5px;\nfont: 16px;\ncolor:white;\nbackground:black;") and test.compare(str(waitForObjectExists(":MainWindow.InsightModeButton_QPushButton").styleSheet), "border:1px solid white;\nfont: 16px;")):
      
        #check Epoc/Epoc+  headset 
        # Check Option
        test.compare(str(waitForObjectExists(":EEG.AllChannels_QCheckBox").styleSheet), "font:bold;color:white;")
        test.compare(str(waitForObjectExists(":EEG.AllChannels_QCheckBox").text), "All Channels")
        clickButton(waitForObject(":EEG.AllChannels_QCheckBox"))
        
       #check F7
        clickButton(waitForObject(":EEG.F7_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.F7_QCheckBox").text), "F7")
        test.compare(str(waitForObjectExists(":EEG.F7_QCheckBox").styleSheet), "font:bold;color: red")
        test.compare(waitForObjectExists(":EEG.F7_QCheckBox").checked, True)
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check F3
        clickButton(waitForObject(":EEG.F7_QCheckBox"))
        clickButton(waitForObject(":EEG.F3_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.F3_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.F3_QCheckBox").text), "F3")
        test.compare(str(waitForObjectExists(":EEG.F3_QCheckBox").styleSheet), "font:bold;\ncolor: \"Cyan\";")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check FC5
        clickButton(waitForObject(":EEG.F3_QCheckBox"))
        clickButton(waitForObject(":EEG.FC5_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.FC5_QCheckBox").styleSheet), "font:bold;color: \"Yellow\"")
        test.compare(waitForObjectExists(":EEG.FC5_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.FC5_QCheckBox").text), "FC5")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check T7
        clickButton(waitForObject(":EEG.FC5_QCheckBox"))
        clickButton(waitForObject(":EEG.T7_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.T7_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.T7_QCheckBox").styleSheet), "font:bold;color: rgb(153, 76, 0);")
        test.compare(str(waitForObjectExists(":EEG.T7_QCheckBox").text), "T7")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
    
        #check P7
        clickButton(waitForObject(":EEG.T7_QCheckBox"))
        clickButton(waitForObject(":EEG.P7_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.P7_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.P7_QCheckBox").styleSheet), "font:bold;color: rgb(0, 255, 0);")
        test.compare(str(waitForObjectExists(":EEG.P7_QCheckBox").text), "P7")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check O1
        clickButton(waitForObject(":EEG.P7_QCheckBox"))
        clickButton(waitForObject(":EEG.O1_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.O1_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.O1_QCheckBox").text), "O1")
        test.compare(str(waitForObjectExists(":EEG.O1_QCheckBox").styleSheet), "font:bold;color: \"Gray\";")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
    
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check O2
        clickButton(waitForObject(":EEG.O1_QCheckBox"))
        clickButton(waitForObject(":EEG.O2_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.O2_QCheckBox").styleSheet), "font:bold;color: \"DarkBlue\";")
        test.compare(str(waitForObjectExists(":EEG.O2_QCheckBox").text), "O2")
        test.compare(waitForObjectExists(":EEG.O2_QCheckBox").checked, True)
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check P8
        clickButton(waitForObject(":EEG.O2_QCheckBox"))
        clickButton(waitForObject(":EEG.P8_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.P8_QCheckBox").styleSheet), "font:bold;\ncolor: rgb(93, 255, 180);")
        test.compare(str(waitForObjectExists(":EEG.P8_QCheckBox").text), "P8")
        test.compare(waitForObjectExists(":EEG.P8_QCheckBox").checked, True)
    
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check T8
        clickButton(waitForObject(":EEG.P8_QCheckBox"))
        clickButton(waitForObject(":EEG.T8_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.T8_QCheckBox").styleSheet), "font:bold;color: rgb(243, 0, 243);")
        test.compare(waitForObjectExists(":EEG.T8_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.T8_QCheckBox").text), "T8")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check FC6
        clickButton(waitForObject(":EEG.T8_QCheckBox"))
        clickButton(waitForObject(":EEG.FC6_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.FC6_QCheckBox").styleSheet), "font:bold;color: rgb(255, 170, 255);")
        test.compare(waitForObjectExists(":EEG.FC6_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.FC6_QCheckBox").text), "FC6")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
    
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check F4
        clickButton(waitForObject(":EEG.FC6_QCheckBox"))
        clickButton(waitForObject(":EEG.F4_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.F4_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.F4_QCheckBox").styleSheet), "font:bold;color: rgb(85, 170, 255);")
        test.compare(str(waitForObjectExists(":EEG.F4_QCheckBox").text), "F4")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check F8
        clickButton(waitForObject(":EEG.F4_QCheckBox"))
        clickButton(waitForObject(":EEG.F8_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.F8_QCheckBox").styleSheet), "font:bold;color: rgb(61, 123, 185);")
        test.compare(str(waitForObjectExists(":EEG.F8_QCheckBox").text), "F8")
        test.compare(waitForObjectExists(":EEG.F8_QCheckBox").checked, True)
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check AF4
        clickButton(waitForObject(":EEG.F8_QCheckBox"))
        clickButton(waitForObject(":EEG.AF4_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.AF4_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.AF4_QCheckBox").styleSheet), "font:bold;color: rgb(44, 134, 65);")
        test.compare(str(waitForObjectExists(":EEG.AF4_QCheckBox").text), "AF4")
    
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
   
    else:    
        
        #check Insight headset
       #check AF4
        test.compare(waitForObjectExists(":qt_tabwidget_tabbar.EEG_TabItem").enabled, True)
        test.compare(waitForObjectExists(":qt_tabwidget_tabbar.EEG_TabItem").text, "EEG")
        test.compare(str(waitForObjectExists(":EEG.label_21_QLabel").text), "OPTIONS")
        test.compare(str(waitForObjectExists(":EEG.label_21_QLabel").styleSheet), "color:white;\nfont:bold 13px;\nbackground:#5d6066;")
        test.compare(str(waitForObjectExists(":EEG.label_QLabel").text), "Channel Spacing")
        #Check up or down channel Spacing
        spinUp(waitForObject(":EEG.ChannelSpacing_QSpinBox"))
        spinUp(waitForObject(":EEG.ChannelSpacing_QSpinBox"))
        spinDown(waitForObject(":EEG.ChannelSpacing_QSpinBox"))
        spinDown(waitForObject(":EEG.ChannelSpacing_QSpinBox"))
        test.compare(str(waitForObjectExists(":EEG.ChannelSpacing_QSpinBox").text), "400")
        test.compare(str(waitForObjectExists(":EEG.ChannelSpacing_QSpinBox").styleSheet), "QSpinBox{\nborder:1px solid #bebfc4;\nbackground: #616266;\ncolor:white;\n}\nQSpinBox::up-button,QSpinBox::down-button{\n\nborder: none;\nborder-right:1px solid #bebfc4;\nbackground: #d3d6db;\n\n\n}\nQSpinBox::up-arrow\n{\nimage:url(:/Resources/up.png);\n}\nQSpinBox::down-arrow\n{\nimage:url(:/Resources/down.png);\n}\n")
        test.compare(waitForObjectExists(":EEG.ChannelSpacing_QSpinBox").enabled, True)
        test.compare(str(waitForObjectExists(":EEG.label_2_QLabel").text), "uV")
        # Max Amplitude
        test.compare(str(waitForObjectExists(":EEG.label_4_QLabel").text), "Max Amplitude")
        test.compare(str(waitForObjectExists(":EEG.qt_spinbox_lineedit_QLineEdit").text), "0")
        test.compare(str(waitForObjectExists(":EEG.MaxAmplitude_QSpinBox").text), "0")
        test.compare(waitForObjectExists(":EEG.MaxAmplitude_QSpinBox").value, 0)
        test.compare(waitForObjectExists(":EEG.MaxAmplitude_QSpinBox").singleStep, 1)
        test.compare(str(waitForObjectExists(":EEG.label_3_QLabel").text), "uV")
        # Min Amplitude
        test.compare(str(waitForObjectExists(":EEG.label_6_QLabel").text), "Min Amplitude")
        test.compare(str(waitForObjectExists(":EEG.qt_spinbox_lineedit_QLineEdit_2").text), "0")
        test.compare(waitForObjectExists(":EEG.MinAmplitude_QSpinBox").singleStep, 1)
        test.compare(str(waitForObjectExists(":EEG.label_5_QLabel").text), "uV")
        #Check EEG channel
        test.compare(str(waitForObjectExists(":EEG.AllChannels_QCheckBox").text), "All")
        clickButton(waitForObject(":EEG.AllChannels_QCheckBox"))
        #check if channel is showed, can adjust up or down Max Amplitude
        clickButton(waitForObject(":EEG.AF3_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.AF3_QCheckBox").styleSheet), "color: \"Blue\"")
        test.compare(waitForObjectExists(":EEG.AF3_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.AF3_QCheckBox").text), "AF3")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        snooze(3)
        #check HighPassFilter
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #Check AF4 
        clickButton(waitForObject(":EEG.AF3_QCheckBox"))
        clickButton(waitForObject(":EEG.AF4_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.AF4_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.AF4_QCheckBox").styleSheet), "\ncolor: rgb(153, 76, 0);")
        test.compare(str(waitForObjectExists(":EEG.AF4_QCheckBox").text), "AF4")
    
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check T7
        clickButton(waitForObject(":EEG.AF4_QCheckBox"))
        clickButton(waitForObject(":EEG.T7_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.T7_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.T7_QCheckBox").styleSheet), "\ncolor: \"Red\";")
        test.compare(str(waitForObjectExists(":EEG.T7_QCheckBox").text), "T7")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check T8
        clickButton(waitForObject(":EEG.T7_QCheckBox"))
        clickButton(waitForObject(":EEG.T8_QCheckBox"))
        test.compare(str(waitForObjectExists(":EEG.T8_QCheckBox").styleSheet), "color: \"Yellow\"")
        test.compare(waitForObjectExists(":EEG.T8_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.T8_QCheckBox").text), "T8")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
        
        #check O1
        clickButton(waitForObject(":EEG.T8_QCheckBox"))
        clickButton(waitForObject(":EEG.O1_QCheckBox"))
        test.compare(waitForObjectExists(":EEG.O1_QCheckBox").checked, True)
        test.compare(str(waitForObjectExists(":EEG.O1_QCheckBox").text), "Pz")
        test.compare(str(waitForObjectExists(":EEG.O1_QCheckBox").styleSheet), "color: \"Cyan\"")
        
        spinUp(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MaxAmplitude_QSpinBox"))
        spinUp(waitForObject(":EEG.MinAmplitude_QSpinBox"))
        spinDown(waitForObject(":EEG.MinAmplitude_QSpinBox"))
    
        snooze(3)
        clickButton(waitForObject(":EEG.HighPassFilter_QCheckBox"))
        clickButton(waitForObject(":EEG.AutoScale_QPushButton"))
