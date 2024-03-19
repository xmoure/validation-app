import os
import resource_rc
import csv
import chess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QPixmap
from views.validation_window_ui import ValidationWindow
from chess_game.chessboard import Chessboard

class ValidationWindowForm(QWidget, ValidationWindow):
    def __init__(self, parent = None, folder_path = None, destination_folder_path = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('FEN Validation')
        self.generated_fen_text_edit.setEnabled(False)
        self.image_paths = []
        self.fen_strings = []
        self.current_index = 0
        self.main_window = parent
        self.folder_path =  folder_path
        self.destination_folder_path = destination_folder_path
        self.setWindowFlag(Qt.Window)
        self.main_window.hide()
        self.cancel_validation_btn.clicked.connect(self.close)
        self.read_csv_and_display_first_element()
        self.save_validation_btn.clicked.connect(self.validate_and_show_next)

    def read_csv_and_display_first_element(self):
        try:
            csv_file_path = self.find_csv_filename(self.folder_path)
            with open(csv_file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    self.image_paths.append(row['file'])
                    self.fen_strings.append(row['fen'])
                # After loading, display the first image and FEN if available
                if self.image_paths and self.fen_strings:
                    self.set_image(self.image_paths[0])
                    self.set_chess_game(self.fen_strings[0])
                    self.update_image_count_label()
                    self.update_fen_label(self.fen_strings[0])
        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Error", e)

    def find_csv_filename(self,directory):
        csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
        if len(csv_files) == 1:
            return os.path.join(directory, csv_files[0])
        elif len(csv_files) > 1:
            raise Exception("More than one CSV file found in the directory.")
        else:
            raise Exception("No CSV files found in the directory.")

    def closeEvent(self, event):
        self.main_window.show()
        event.accept()

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(550, 600, Qt.KeepAspectRatio)
        self.chess_img_label.setPixmap(pixmap)
        image_name = os.path.basename(image_path)
        self.imge_label.setText(f"Image {image_name}")

    def set_chess_game(self, starting_fen):
        self.board = chess.Board(starting_fen)
        self.scene = Chessboard(self.board)
        self.chess_graphic_view.setScene(self.scene)
        self.scene.fenUpdated.connect(self.update_fen_label)
        self.scene.render()

    def update_fen_label(self, fen):
        self.generated_fen_text_edit.setText(fen)

    def update_image_count_label(self):
        current_position = self.current_index + 1
        total_images = len(self.image_paths)
        self.count_images_label.setText(f"Image {current_position} out of {total_images}")

    def show_next_item(self):
        if self.current_index + 1 < len(self.image_paths):
            self.current_index += 1
            self.set_image(self.image_paths[self.current_index])
            self.set_chess_game(self.fen_strings[self.current_index])
            self.update_fen_label(self.fen_strings[self.current_index])
            self.update_image_count_label()
        else:
            QMessageBox.information(self, "Validation finished", "You have finished validating all the images")

    def validate_and_show_next(self):
        # STILL MISSING TO STORE THE VALIDATED FEN
        self.show_next_item()



