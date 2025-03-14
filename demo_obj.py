import sys
import numpy as np
import trimesh
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QLabel, QOpenGLWidget
from PyQt5.QtCore import Qt

class OpenGLFaceWidget(QOpenGLWidget):
    def __init__(self, model, parent=None):
        super(OpenGLFaceWidget, self).__init__(parent)
        self.model = model

    def paintGL(self):
        # 使用 trimesh 渲染 3D 模型
        self.model.render()

    def initializeGL(self):
        # 初始化OpenGL设置
        pass

    def resizeGL(self, w, h):
        # 处理窗口大小调整
        pass

    def update_face(self, model):
        self.model = model
        self.update()

class FaceModelApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("3D Face Model Adjustment")

        # 初始化面部模型
        self.model = self.load_3d_face_model('examples/results/JZG.obj')

        # 创建滑动条和标签
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.nose_slider = self.create_slider("Nose")
        self.eyes_slider = self.create_slider("Eyes")
        self.mouth_slider = self.create_slider("Mouth")

        layout.addWidget(self.nose_slider)
        layout.addWidget(self.eyes_slider)
        layout.addWidget(self.mouth_slider)

        # 3D模型显示区域
        self.opengl_widget = OpenGLFaceWidget(self.model)
        layout.addWidget(self.opengl_widget)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # 连接滑动条的值变化信号到槽函数
        self.nose_slider.valueChanged.connect(self.update_nose)
        self.eyes_slider.valueChanged.connect(self.update_eyes)
        self.mouth_slider.valueChanged.connect(self.update_mouth)

    def create_slider(self, name):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(-10)
        slider.setMaximum(10)
        return slider

    def load_3d_face_model(self, file_path):
        # 加载 OBJ 文件为 3D 模型
        mesh = trimesh.load(file_path)
        return FaceModel(mesh)

    def update_nose(self, value):
        self.model.adjust_nose(value)
        self.opengl_widget.update_face(self.model)

    def update_eyes(self, value):
        self.model.adjust_eyes(value)
        self.opengl_widget.update_face(self.model)

    def update_mouth(self, value):
        self.model.adjust_mouth(value)
        self.opengl_widget.update_face(self.model)

class FaceModel:
    def __init__(self, mesh):
        self.mesh = mesh

    def adjust_nose(self, value):
        # 在此处调整鼻子的顶点坐标，值通过滑动条传入
        self.mesh.vertices[5000:5500, 2] += value * 0.01

    def adjust_eyes(self, value):
        # 在此处调整眼睛区域的顶点坐标
        self.mesh.vertices[3000:3500, 1] += value * 0.01

    def adjust_mouth(self, value):
        # 在此处调整嘴巴区域的顶点坐标
        self.mesh.vertices[7000:7500, 0] += value * 0.01

    def render(self):
        # 使用 trimesh 渲染当前的 3D 模型
        scene = trimesh.Scene(self.mesh)
        scene.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceModelApp()
    window.show()
    sys.exit(app.exec_())