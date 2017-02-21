# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierPure.EEG")
    clickTab(waitForObject(":MainWindow.ModeEpocFrame_QTabWidget"), "Data Packets")
    test.compare(waitForObjectExists(":qt_tabwidget_tabbar.Data Packets_TabItem").enabled, True)
    test.compare(waitForObjectExists(":qt_tabwidget_tabbar.Data Packets_TabItem").text, "Data Packets")
