# "ShowMiiWADs-Py.py" licensed under the MIT license
# Copyright 2025 NinjaCheetah and Contributors

import json
import os
import sys
import webbrowser
from importlib.metadata import version

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QListView, QLabel
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject, QLibraryInfo, QTranslator, QLocale

from qt.py.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.addWidget(QLabel("Files: 0"))
        self.ui.statusbar.addWidget(QLabel("Folders: 0"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Load the config path and then the configuration data, if it exists. If not, then we should initialize it and write
    # it out.
    # config_file = get_config_file()
    # if config_file.exists():
    #     config_data: dict = json.load(open(config_file))
    # else:
    #     config_data: dict = {"auto_update": True}
    #     save_config(config_data)

    # Load Fusion because that's objectively the best base theme, and then load the fancy stylesheet on top to make
    # NUSGet look nice and pretty.
    app.setStyle("fusion")
    # theme_sheet = "style_dark.qss"
    # try:
    #     # Check for an environment variable overriding the theme. This is mostly for theme testing but would also allow
    #     # you to force a theme.
    #     if os.environ["THEME"].lower() == "light":
    #         theme_sheet = "style_light.qss"
    # except KeyError:
    #     if is_dark_theme():
    #         theme_sheet = "style_dark.qss"
    #     else:
    #         theme_sheet = "style_light.qss"
    # stylesheet = open(os.path.join(os.path.dirname(__file__), "resources", theme_sheet)).read()
    # image_path_prefix = pathlib.Path(os.path.join(os.path.dirname(__file__), "resources")).resolve().as_posix()
    # stylesheet = stylesheet.replace("{IMAGE_PREFIX}", image_path_prefix)
    # app.setStyleSheet(stylesheet)

    # Load base Qt translations, and then app-specific translations.
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = os.path.join(os.path.dirname(__file__), "resources", "translations")
    # Unix-likes and Windows handle this differently, apparently. Unix-likes will try `nusget_xx_XX.qm` and then fall
    # back on just `nusget_xx.qm` if the region-specific translation for the language can't be found. On Windows, no
    # such fallback exists, and so this code manually implements that fallback, since for languages like Spanish NUSGet
    # doesn't use region-specific translations.
    # locale = QLocale.system()
    # if not translator.load(QLocale.system(), 'nusget', '_', path):
    #     base_locale = QLocale(locale.language())
    #     translator.load(base_locale, 'nusget', '_', path)
    # app.installTranslator(translator)

    window = MainWindow()
    window.setWindowTitle("ShowMiiWADs-Py")
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources", "icon.png")))
    window.show()

    sys.exit(app.exec())
