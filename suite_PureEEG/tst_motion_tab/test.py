# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickTab(waitForObject(":MainWindow.tabWidget_QTabWidget"), "Motion")
    # check button
    test.compare(str(waitForObjectExists(":MotionChart.AllChannels_QCheckBox").text), "All Channels")
    test.compare(str(waitForObjectExists(":MotionChart.AllChannels_QCheckBox").objectName), "AllChannels")
    clickButton(waitForObject(":MotionChart.AllChannels_QCheckBox"))
    setWindowState(waitForObject(":MainWindow_MainUI"), WindowState.Minimize)
    setWindowState(waitForObject(":MainWindow_MainUI"), WindowState.Normal)
   
    # check GyroScopeX
    test.compare(str(waitForObjectExists(":MotionChart.GyroscopeZ_QCheckBox").text), "GyroScopeX")
    test.compare(str(waitForObjectExists(":MotionChart.GyroscopeZ_QCheckBox").styleSheet), "color: \"Blue\"")
    #test.compare(str(waitForObjectExists(":MotionChart.GyroscopeZ_QCheckBox").objectName), "GyrosSopeX")
    clickButton(waitForObject(":MotionChart.GyroscopeZ_QCheckBox"))
    
    # Check GyroScopeY
    test.compare(str(waitForObjectExists(":MotionChart.GyroScopeX_QCheckBox").text), "GyroScopeY")
    test.compare(str(waitForObjectExists(":MotionChart.GyroScopeX_QCheckBox").styleSheet), "color: \"Red\"")
   # test.compare(str(waitForObjectExists(":MotionChart.GyroscopeX_QCheckBox").objectName), "GyrosSopeY")
    mouseClick(waitForObject(":MotionChart.widget_QWidget"), 309, 12, 0, Qt.LeftButton)
    clickButton(waitForObject(":MotionChart.GyroScopeX_QCheckBox"))
    
    # Check GyroScopeZ
    test.compare(str(waitForObjectExists(":MotionChart.GyroScopeY_QCheckBox").text), "GyroScopeZ")
    test.compare(str(waitForObjectExists(":MotionChart.GyroScopeY_QCheckBox").styleSheet), "color: \"Cyan\";")
    #test.compare(str(waitForObjectExists(":MotionChart.GyroscopeY_QCheckBox").objectName), "GyrosScopeZ")
    clickButton(waitForObject(":MotionChart.GyroScopeY_QCheckBox"))
   
    # Check ACCX
    test.compare(str(waitForObjectExists(":MotionChart.ACCX_QCheckBox").styleSheet), "color: \"Yellow\";")
    test.compare(str(waitForObjectExists(":MotionChart.ACCX_QCheckBox").text), "ACCX")
   # test.compare(str(waitForObjectExists(":MotionChart.ACCX_QCheckBox").objectName), "ACCX")
    clickButton(waitForObject(":MotionChart.ACCX_QCheckBox"))
   
    # Check ACCY
    test.compare(str(waitForObjectExists(":MotionChart.ACCY_QCheckBox").text), "ACCY")
    test.compare(str(waitForObjectExists(":MotionChart.ACCY_QCheckBox").styleSheet), "color: rgb(153, 76, 0);")
   # test.compare(str(waitForObjectExists(":MotionChart.ACCY_QCheckBox").objectName), "ACCY")
    clickButton(waitForObject(":MotionChart.ACCY_QCheckBox"))
    
    # Check ACCZ
    test.compare(str(waitForObjectExists(":MotionChart.ACCZ_QCheckBox").text), "ACCZ")
    test.compare(str(waitForObjectExists(":MotionChart.ACCZ_QCheckBox").styleSheet), "color:  rgb(0, 255, 0);")
  #  test.compare(str(waitForObjectExists(":MotionChart.ACCZ_QCheckBox").objectName), "ACCZ")
    clickButton(waitForObject(":MotionChart.ACCZ_QCheckBox"))
   
    # Check MAGX
    test.compare(str(waitForObjectExists(":MotionChart.MAGY_QCheckBox").text), "MAGX")
    test.compare(str(waitForObjectExists(":MotionChart.MAGY_QCheckBox").styleSheet), "color: \"Gray\";")
    #test.compare(str(waitForObjectExists(":MotionChart.MAGY_QCheckBox").objectName), "MAGX")
    clickButton(waitForObject(":MotionChart.MAGY_QCheckBox"))
   
    # Check MAGY
    test.compare(str(waitForObjectExists(":MotionChart.MAGZ_QCheckBox").text), "MAGY")
    test.compare(str(waitForObjectExists(":MotionChart.MAGZ_QCheckBox").styleSheet), "color: \"DarkBlue\";")
    #test.compare(str(waitForObjectExists(":MotionChart.MAGZ_QCheckBox").objectName), "MAGY")
    clickButton(waitForObject(":MotionChart.MAGZ_QCheckBox"))
    
    # Check MAGZ
    test.compare(str(waitForObjectExists(":MotionChart.MAGX_QCheckBox").text), "MAGZ")
    test.compare(str(waitForObjectExists(":MotionChart.MAGX_QCheckBox").styleSheet), "color: rgb(93, 255, 180);")
    #test.compare(str(waitForObjectExists(":MotionChart.MAGX_QCheckBox").objectName), "MAGZ")
    clickButton(waitForObject(":MotionChart.MAGX_QCheckBox"))
    # Check Graph
