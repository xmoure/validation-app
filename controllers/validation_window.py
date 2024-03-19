from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QLabel, QAbstractItemView, QDialog, QVBoxLayout, QHeaderView, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon
import os
import resource_rc
from styles.styles import styles_table_files, styles_btn_disabled, styles_btn_enabled
from views.validation_window_ui import ValidationWindow

class ValidationWindowForm(QWidget, ValidationWindow):
    def __init__(self, parent = None, folder_path = None, destination_folder_path = None) -> None:
        super().__init__(parent)
        self.main_window = parent
        self.folder_path =  folder_path
        self.destination_folder_path = destination_folder_path
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.main_window.hide()
        self.cancel_validation_btn.clicked.connect(self.close)

    def closeEvent(self, event):
        self.main_window.show()
        event.accept()



