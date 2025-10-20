import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QRectF, QPointF

class ImageAnnotator(QMainWindow):
    def __init__(self, folder_b, folder_c):
        super().__init__()
        
        # Paths to folders
        self.folder_b = folder_b
        self.folder_c = folder_c
        os.makedirs(self.folder_c, exist_ok=True)
        
        # Load image list
        self.image_list = sorted(os.listdir(folder_b))
        self.current_index = 0
        
        # Initialize GUI
        self.init_ui()
        self.load_image()
    
    def init_ui(self):
        self.setWindowTitle("Raw Image Annotator")
        # self.setGeometry(100, 100, 2000, 2000)  # Fixed window size
        self.setFixedSize(2000, 2000)
        
        # Main layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        # Label for raw image
        self.label_raw = QLabel(self)
        self.label_raw.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_raw)
        
        # Buttons
        self.buttons_layout = QHBoxLayout()
        
        self.btn_save = QPushButton("Save Annotated Image", self)
        self.btn_save.clicked.connect(self.save_annotated_image)
        
        self.btn_next = QPushButton("Next Image", self)
        self.btn_next.clicked.connect(self.next_image)

        self.btn_previous = QPushButton("Previous Image", self)
        self.btn_previous.clicked.connect(self.previous_image)
        
        self.buttons_layout.addWidget(self.btn_save)
        self.buttons_layout.addWidget(self.btn_next)
        self.buttons_layout.addWidget(self.btn_previous)
        
        self.main_layout.addLayout(self.buttons_layout)
        
        # Annotation variables
        self.drawing = False
        self.start_point = None
        self.rectangles = []
        
        # Enable mouse events on raw image
        self.label_raw.mousePressEvent = self.mouse_press
        self.label_raw.mouseMoveEvent = self.mouse_move
        self.label_raw.mouseReleaseEvent = self.mouse_release
        
        # Pixmap to display the image with annotations
        self.raw_pixmap = None
    
    def load_image(self):
        raw_path = os.path.join(self.folder_b, self.image_list[self.current_index])
        
        # Ensure QLabel fills the available space
        self.label_raw.setFixedSize(self.width(), self.height() - 100)
        
        # Scale the pixmap to fit the QLabel dimensions
        self.raw_pixmap = QPixmap(raw_path).scaled(
            self.label_raw.width(), self.label_raw.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.label_raw.setPixmap(self.raw_pixmap)
        self.rectangles.clear()  # Clear annotations for the new image
    
    def mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = self.map_to_image(event.pos())
        elif event.button() == Qt.RightButton:
            # Remove the last drawn rectangle (Ctrl+Z functionality)
            if self.rectangles:
                self.rectangles.pop()
                self.update_annotations()
    
    def mouse_move(self, event):
        if self.drawing:
            self.update_annotations(self.map_to_image(event.pos()))
    
    def mouse_release(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            end_point = self.map_to_image(event.pos())
            self.rectangles.append(QRectF(self.start_point, end_point))
            self.update_annotations()
    
    def map_to_image(self, widget_pos):
        """
        Maps widget coordinates to the original image coordinates.
        """
        # Get the QLabel dimensions
        label_width = self.label_raw.width()
        label_height = self.label_raw.height()

        # Get the displayed pixmap size
        pixmap_width = self.raw_pixmap.width()
        pixmap_height = self.raw_pixmap.height()

        # Calculate offsets (padding) to center the image in QLabel
        offset_x = (label_width - pixmap_width) / 2
        offset_y = (label_height - pixmap_height) / 2

        # Adjust the widget position to account for the offset
        adjusted_x = widget_pos.x() - offset_x
        adjusted_y = widget_pos.y() - offset_y

        # Ensure the adjusted coordinates are within the image boundaries
        adjusted_x = max(0, min(adjusted_x, pixmap_width))
        adjusted_y = max(0, min(adjusted_y, pixmap_height))

        # Scale coordinates to match the original image
        scale_x = self.raw_pixmap.size().width() / pixmap_width
        scale_y = self.raw_pixmap.size().height() / pixmap_height

        image_x = adjusted_x * scale_x
        image_y = adjusted_y * scale_y

        return QPointF(image_x, image_y)
    
    def update_annotations(self, current_point=None):
        # Draw the image with bounding boxes
        annotated_pixmap = self.raw_pixmap.copy()
        painter = QPainter(annotated_pixmap)
        pen = QPen(Qt.red, 2)
        painter.setPen(pen)
        
        # Draw existing rectangles
        for rect in self.rectangles:
            painter.drawRect(rect)
        
        # Draw the current rectangle being created
        if self.drawing and current_point:
            painter.drawRect(QRectF(self.start_point, current_point))
        
        painter.end()
        self.label_raw.setPixmap(annotated_pixmap)
    
    def save_annotated_image(self):
        # Save the raw image with bounding boxes
        raw_path = self.image_list[self.current_index]
        save_path = os.path.join(self.folder_c, raw_path)
        annotated_pixmap = self.raw_pixmap.copy()
        painter = QPainter(annotated_pixmap)
        pen = QPen(Qt.red, 2)
        painter.setPen(pen)
        for rect in self.rectangles:
            painter.drawRect(rect)
        painter.end()
        annotated_pixmap.save(save_path)
        self.statusBar().showMessage(f"Annotated image saved to {save_path}", 5000)
    
    def next_image(self):
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.load_image()
        else:
            self.statusBar().showMessage("No more images to display.", 5000)

    def previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_image()
        else:
            self.statusBar().showMessage("There is no previous image to display.", 5000)

# Main execution
if __name__ == "__main__":
    folder_b = "./data/Raw"
    folder_c = "./data/Saved_withoutAI"
    
    app = QApplication(sys.argv)
    window = ImageAnnotator(folder_b, folder_c)
    window.show()
    sys.exit(app.exec_())
