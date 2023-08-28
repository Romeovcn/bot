import pyautogui
import time
import keyboard
import threading
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer, QObject, QEvent

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 400, 200)
        
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

        # Créer le QLabel pour afficher le texte
        self.label = QLabel("Ceci est un overlay", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 18px;")
        self.label.setGeometry(0, 0, 400, 200)

    def keyPressEvent(self, event):
        # Changer le texte du QLabel lorsque la touche "0" est pressée
        if event.key() == Qt.Key_0:
            self.label.setText("Nouveau texte après avoir pressé 0")
        elif event.key() == Qt.Key_Escape:
            self.close()

class KeyPressFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Q:
                app.quit()
                return True
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()

    key_filter = KeyPressFilter()
    app.installEventFilter(key_filter)

    sys.exit(app.exec_())