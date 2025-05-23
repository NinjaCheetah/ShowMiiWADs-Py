# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1045, 545)
        self.file_open_folder = QAction(MainWindow)
        self.file_open_folder.setObjectName(u"file_open_folder")
        self.file_exit = QAction(MainWindow)
        self.file_exit.setObjectName(u"file_exit")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_placeholder_none = QAction(MainWindow)
        self.action_placeholder_none.setObjectName(u"action_placeholder_none")
        self.action_placeholder_none.setEnabled(False)
        self.file_export = QAction(MainWindow)
        self.file_export.setObjectName(u"file_export")
        self.file_refresh = QAction(MainWindow)
        self.file_refresh.setObjectName(u"file_refresh")
        self.tools_lz77_compress = QAction(MainWindow)
        self.tools_lz77_compress.setObjectName(u"tools_lz77_compress")
        self.tools_lz77_decompress = QAction(MainWindow)
        self.tools_lz77_decompress.setObjectName(u"tools_lz77_decompress")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.wad_table = QTableWidget(self.centralwidget)
        if (self.wad_table.columnCount() < 10):
            self.wad_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.wad_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.wad_table.setObjectName(u"wad_table")
        self.wad_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.wad_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.wad_table.setShowGrid(False)
        self.wad_table.setCornerButtonEnabled(False)
        self.wad_table.horizontalHeader().setHighlightSections(False)

        self.main_layout.addWidget(self.wad_table)


        self.verticalLayout_2.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1045, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.file_recent_folders = QMenu(self.menuFile)
        self.file_recent_folders.setObjectName(u"file_recent_folders")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.file_open_folder)
        self.menuFile.addAction(self.file_export)
        self.menuFile.addAction(self.file_refresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.file_recent_folders.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.file_exit)
        self.file_recent_folders.addAction(self.action_placeholder_none)
        self.menuTools.addAction(self.tools_lz77_compress)
        self.menuTools.addAction(self.tools_lz77_decompress)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ShowMiiWADs-Py", None))
        self.file_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#if QT_CONFIG(shortcut)
        self.file_open_folder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.file_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.action_placeholder_none.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.file_export.setText(QCoreApplication.translate("MainWindow", u"Export to File", None))
#if QT_CONFIG(shortcut)
        self.file_export.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.file_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh Folder", None))
#if QT_CONFIG(shortcut)
        self.file_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.tools_lz77_compress.setText(QCoreApplication.translate("MainWindow", u"LZ77 Compress", None))
        self.tools_lz77_decompress.setText(QCoreApplication.translate("MainWindow", u"LZ77 Decompress", None))
        ___qtablewidgetitem = self.wad_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem1 = self.wad_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.wad_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Channel Name", None));
        ___qtablewidgetitem3 = self.wad_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Title ID", None));
        ___qtablewidgetitem4 = self.wad_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Version", None));
        ___qtablewidgetitem5 = self.wad_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Blocks", None));
        ___qtablewidgetitem6 = self.wad_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Filesize", None));
        ___qtablewidgetitem7 = self.wad_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"IOS", None));
        ___qtablewidgetitem8 = self.wad_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Region", None));
        ___qtablewidgetitem9 = self.wad_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Contents", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.file_recent_folders.setTitle(QCoreApplication.translate("MainWindow", u"Recent Folders", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

