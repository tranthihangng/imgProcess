import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFileDialog, QFrame, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPoint

class ImageLabel(QLabel):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setPixmap(pixmap)
        self.original_pixmap = pixmap
        self.setScaledContents(True)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.is_moving = False
        self.offset = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_moving = True
            self.offset = event.pos()
        elif event.button() == Qt.RightButton:
            self.showContextMenu(event.pos())

    def mouseMoveEvent(self, event):
        if self.is_moving:
            new_pos = self.mapToParent(event.pos() - self.offset)
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        self.is_moving = False

    def wheelEvent(self, event):
        # Phóng to hoặc thu nhỏ ảnh
        delta = event.angleDelta().y() / 120
        scale_factor = 1 + delta * 0.1
        new_size = self.size() * scale_factor
        if 50 < new_size.width() < 1000 and 50 < new_size.height() < 1000:
            self.resize(new_size)
            self.setPixmap(self.original_pixmap.scaled(self.size(), Qt.KeepAspectRatio))

    def showContextMenu(self, pos):
        context_menu = QMenu(self)
        bring_to_front = context_menu.addAction("Đưa lên trước")
        send_to_back = context_menu.addAction("Đưa ra sau")
        action = context_menu.exec_(self.mapToGlobal(pos))

        if action == bring_to_front:
            self.raise_()
        elif action == send_to_back:
            self.lower()

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Photo Editor')
        self.setGeometry(100, 100, 600, 600)

        # Khung chứa ảnh
        self.frame = QFrame(self)
        self.frame.setGeometry(50, 50, 500, 500)
        self.frame.setStyleSheet("background-color: lightgray;")

        # Layout chính
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Chọn và tải ảnh lên
        self.load_images()

    def load_images(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Load Images", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if files:
            for file in files:
                pixmap = QPixmap(file)
                scaled_pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label = ImageLabel(scaled_pixmap, self.frame)
                image_label.show()
                image_label.setCursor(Qt.OpenHandCursor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())
