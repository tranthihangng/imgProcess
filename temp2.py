import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFileDialog, QFrame, QMenu, QPushButton
from PyQt5.QtGui import QPixmap, QPainter
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

        # Nút lưu ảnh
        self.save_button = QPushButton('Save Image', self)
        self.save_button.clicked.connect(self.save_image)
        layout.addWidget(self.save_button)

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

    def save_image(self):
        # Tìm ảnh ở lớp đầu tiên
        image_labels = self.frame.findChildren(ImageLabel)
        if not image_labels:
            return

        # Lấy ảnh ở lớp đầu tiên
        first_image_label = image_labels[0]

        # Lấy kích thước của ảnh từ lớp đầu tiên
        first_image_size = first_image_label.original_pixmap.size()

        # Tạo một QPixmap với kích thước của ảnh từ lớp đầu tiên
        pixmap = QPixmap(first_image_size)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        for child in image_labels:
            # Vẽ ảnh lên pixmap với kích thước của ảnh đầu tiên
            painter.drawPixmap(child.geometry().topLeft(), child.pixmap())

        painter.end()

        # Lưu ảnh ghép lại
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)",
                                                   options=options)
        if file_name:
            pixmap.save(file_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())
