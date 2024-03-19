from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QGraphicsView
from PySide6.QtGui import QPixmap, QIcon
import os
import resource_rc
from styles.styles import styles_table_files, styles_btn_disabled, styles_btn_enabled
from views.validation_window_ui import ValidationWindow
import chess
from chess_game.chessboard import Chessboard
from chess_game.piece import Piece

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
        self.set_chess_game()


    def closeEvent(self, event):
        self.main_window.show()
        event.accept()

    def set_chess_game(self):
        starting_fen = "rnbqkbnr/pp1pp1pp/8/2p2p2/3P4/2N5/PPP1PPPP/R1BQKBNR"
        self.board = chess.Board(starting_fen)
        self.scene = Chessboard(self.board)
        self.chess_graphic_view.setScene(self.scene)

        #self.viewer = QGraphicsView(self.scene)
        #self.setCentralWidget(self.viewer)
        self.scene.render()



