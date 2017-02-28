# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickTab(waitForObject(":MainWindow.tabWidget_QTabWidget_3"), "Gyro")
    test.compare(waitForObjectExists(":qt_tabwidget_tabbar.Gyro_TabItem").enabled, True)
    test.compare(waitForObjectExists(":qt_tabwidget_tabbar.Gyro_TabItem").text, "Gyro")
