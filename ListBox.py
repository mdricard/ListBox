import sys
from PyQt5.QtCore import QMargins, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QListWidget, QPushButton, \
    QHBoxLayout
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()

        my_list = QListWidget()
        my_list.addItems(["One", "Two", "Three", "Four", "Five list items"])
        # In QListWidget there are two separate signals for the item, and the string
        my_list.currentItemChanged.connect(self.index_changed)
        my_list.currentTextChanged.connect(self.text_changed)

        self.lbl_mouse_coords = QLabel("Mouse Coords")
        vertical_layout.addWidget(self.lbl_mouse_coords)
        vertical_layout.addWidget(QLabel("my label 2"))
        vertical_layout.addWidget(QPushButton("Button One"))
        vertical_layout.addWidget(my_list)

        horizontal_layout.addLayout(vertical_layout)
        img_label = QLabel("Hello")
        img_label.setPixmap(QPixmap("d:/heart.png"))
        horizontal_layout.addWidget(img_label)

        widget = QWidget()
        widget.setLayout(horizontal_layout)
        self.setCentralWidget(widget)

    def index_changed(self, i):     # Not an index, i is a QListItem
        print("QListItem selected is :" + i.text())
        self.lbl_mouse_coords.setText(i.text())

    def text_changed(self, s):      # s is a string
        print("s is: " + s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
