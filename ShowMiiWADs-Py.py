# "ShowMiiWADs-Py.py" licensed under the MIT license
# Copyright 2025 NinjaCheetah and Contributors

# Nuitka options. These determine compilation settings based on the current OS.
# nuitka-project-if: {OS} == "Darwin":
#    nuitka-project: --standalone
#    nuitka-project: --macos-create-app-bundle
#    nuitka-project: --macos-app-icon={MAIN_DIRECTORY}/resources/icon.png
# nuitka-project-if: {OS} == "Windows":
#    nuitka-project: --onefile
#    nuitka-project: --windows-icon-from-ico={MAIN_DIRECTORY}/resources/icon.png
#    nuitka-project: --windows-console-mode=disable
# nuitka-project-if: {OS} in ("Linux", "FreeBSD", "OpenBSD"):
#    nuitka-project: --onefile

# These are standard options that are needed on all platforms.
# nuitka-project: --plugin-enable=pyside6
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/resources=resources

import sys

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QListView, QLabel, QTableWidgetItem, \
    QProgressBar
from PySide6.QtCore import Qt, QRunnable, Slot, QThreadPool, Signal, QObject, QLibraryInfo, QTranslator, QLocale

from qt.py.ui_MainWindow import Ui_MainWindow
from modules.lz77 import *
from modules.config import *
from modules.coredata import *


class WorkerSignals(QObject):
    result = Signal(object)
    progress = Signal(str)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        # All possible errors *should* be caught by the code and will safely return specific error codes. In the
        # unlikely event that an unexpected error happens, it can only possibly be a ValueError, so handle that and
        # return code 1.
        # I have no idea if this above comment is true outside of NUSGet yet^
        try:
            result = self.fn(*self.args, **self.kwargs)
        except ValueError:
            self.signals.result.emit(1)
        else:
            self.signals.result.emit(result)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.ui.file_count_lbl = QLabel("Files: 0")
        self.ui.folder_count_lbl = QLabel("Folders: 0")
        self.ui.status_progressbar = QProgressBar()
        self.ui.status_progressbar.setMaximumWidth(200)
        self.ui.status_lbl = QLabel()
        self.folder_actions = []
        self.ui.statusbar.addWidget(self.ui.file_count_lbl)
        self.ui.statusbar.addWidget(self.ui.folder_count_lbl)
        self.ui.statusbar.addPermanentWidget(self.ui.status_lbl)
        self.ui.statusbar.addPermanentWidget(self.ui.status_progressbar)
        # =========
        # File Menu
        # =========
        self.ui.file_open_folder.triggered.connect(self.add_folder)
        self.ui.file_export.triggered.connect(self.export_wad_info)
        self.ui.file_refresh.triggered.connect(self.load_folder)
        self.ui.file_exit.triggered.connect(self.close)
        # ==========
        # Tools Menu
        # ==========
        self.ui.tools_lz77_compress.triggered.connect(self.tools_lz77_compress)
        self.ui.tools_lz77_decompress.triggered.connect(self.tools_lz77_decompress)
        if "folder_paths" in config_data.keys() and len(config_data["folder_paths"]) > 0:
            self.load_folder()
            self.ui.folder_count_lbl.setText(f"Folders: {len(config_data["folder_paths"])}")
            self.build_recent_folder_list()

    def build_recent_folder_list(self):
        self.ui.file_recent_folders.clear()
        for index, folder in enumerate(config_data["folder_paths"]):
            new_action = QAction(folder)
            new_action.triggered.connect(lambda _, idx=index: self.change_active_folder(idx))
            self.folder_actions.append(new_action)
            self.ui.file_recent_folders.addAction(new_action)

    def add_folder(self):
        selected_dir = QFileDialog.getExistingDirectory(self, app.translate("MainWindow", "Open Directory"),
                                                        "", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if selected_dir == "":
            return
        out_path = pathlib.Path(selected_dir)
        if not out_path.exists() or not out_path.is_dir():
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg_box.setWindowTitle("Invalid WAD Folder")
            msg_box.setText("<b>The specified directory does not exist!</b>")
            msg_box.setInformativeText("Please make sure the directory you want to use exists, and that you have permission to access it.")
            msg_box.exec()
            return
        add_new_folder(config_data, str(out_path.absolute()))
        self.build_recent_folder_list()
        self.load_folder()

    def change_active_folder(self, idx):
        folders = config_data["folder_paths"]
        tgt_folder = folders.pop(idx)
        folders.insert(0, tgt_folder)
        update_setting(config_data, "folder_paths", folders)
        self.build_recent_folder_list()
        self.load_folder()

    def load_folder(self):
        folder_path = pathlib.Path(config_data["folder_paths"][0])
        print(f"loading WADs in path \"{folder_path}\"...")
        for row in range(0, self.ui.wad_table.rowCount()):
            self.ui.wad_table.removeRow(0)
        wad_files = list(folder_path.glob("*.[wW][aA][dD]"))
        if wad_files:
            for wad in wad_files:
                title = libWiiPy.title.Title()
                title.load_wad(open(wad, "rb").read())
                self.ui.wad_table.insertRow(self.ui.wad_table.rowCount())
                row_idx = self.ui.wad_table.rowCount() - 1
                wad_info = process_wad_info(wad.name, title)
                self.ui.wad_table.setItem(row_idx, 0, QTableWidgetItem(wad_info["name"]))
                self.ui.wad_table.setItem(row_idx, 1, QTableWidgetItem(wad_info["type"]))
                self.ui.wad_table.setItem(row_idx, 2, QTableWidgetItem(wad_info["channel_name"]))
                self.ui.wad_table.setItem(row_idx, 3, QTableWidgetItem(wad_info["ascii_tid"]))
                self.ui.wad_table.setItem(row_idx, 4, QTableWidgetItem(wad_info["version"]))
                self.ui.wad_table.setItem(row_idx, 5, QTableWidgetItem(wad_info["size_blocks"]))
                self.ui.wad_table.setItem(row_idx, 6, QTableWidgetItem(wad_info["size_mb"]))
                self.ui.wad_table.setItem(row_idx, 7, QTableWidgetItem(wad_info["ios"]))
                self.ui.wad_table.setItem(row_idx, 8, QTableWidgetItem(wad_info["region"]))
                self.ui.wad_table.setItem(row_idx, 9, QTableWidgetItem(wad_info["contents"]))
        self.ui.file_count_lbl.setText(f"Files: {self.ui.wad_table.rowCount()}")

    def export_wad_info(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Export WAD Info to CSV", "", "CSV Files (*.csv)")
        if file_name == "":
            return
        file_path = pathlib.Path(file_name).with_suffix(".csv")
        out_text = "Filename,Type,Channel Name,ASCII TID,Version,Size Blocks,Size MB,IOS,Region,Contents\n"
        for row in range(0, self.ui.wad_table.rowCount()):
            for i in range(0, 10):
                out_text += f"{self.ui.wad_table.item(row, i).text()},"
            out_text += "\n"
        open(file_path, "w").write(out_text)

    def tools_lz77_compress(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select a File to Compress", "")
        if file_name == "":
            return
        file_path = pathlib.Path(file_name)
        # Outsource to Rust because the Python implementation is uselessly slow. Also outsource that to a thread so the
        # UI doesn't die.
        self.ui.status_lbl.setText(f"Compressing {file_path.name}...")
        self.ui.status_progressbar.setRange(0, 0)
        worker = Worker(compress_lz77, file_path)
        worker.signals.result.connect(self.callback_lz77_compress_done)
        self.threadpool.start(worker)

    def callback_lz77_compress_done(self, file_path):
        self.ui.status_lbl.clear()
        self.ui.status_progressbar.setRange(0, 100)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg_box.setWindowTitle("File Compressed Successfully")
        msg_box.setText("<b>The file has successfully been compressed!</b>")
        msg_box.setInformativeText(f"The compressed file was saved to {file_path.with_suffix('.lz77')}.")
        msg_box.exec()

    def tools_lz77_decompress(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select a File to Decompress", "")
        if file_name == "":
            return
        file_path = pathlib.Path(file_name)
        self.ui.status_lbl.setText(f"Decompressing {file_path.name}...")
        self.ui.status_progressbar.setRange(0, 0)
        worker = Worker(decompress_lz77, file_path)
        worker.signals.result.connect(self.callback_lz77_decompress_done)
        self.threadpool.start(worker)

    def callback_lz77_decompress_done(self, file_path):
        msg_box = QMessageBox()
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        self.ui.status_lbl.clear()
        self.ui.status_progressbar.setRange(0, 100)
        if not file_path:
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("Could Not Decompress File")
            msg_box.setText("<b>The specified file could not be decompressed!</b>")
            msg_box.setInformativeText(f"Please make sure that you have selected an LZ77-compressed file.")
        else:
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("File Decompressed Successfully")
            msg_box.setText("<b>The file has successfully been decompressed!</b>")
            msg_box.setInformativeText(f"The decompressed file was saved to {file_path.with_suffix('.out')}.")
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Load the config path and then the configuration data, if it exists. If not, then we should initialize it and write
    # it out.
    config_file = get_config_file()
    if config_file.exists():
        config_data: dict = json.load(open(config_file))
    else:
        config_data: dict = {}
        save_config(config_data)

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
