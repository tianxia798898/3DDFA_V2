import open3d as o3d
import numpy as np

# 加载 OBJ 文件
mesh = o3d.io.read_triangle_mesh("examples/results/JZG.obj")
vertices = np.asarray(mesh.vertices)

# 备份原始顶点
original_vertices = vertices.copy()
# 鼻子调整
nose_region = vertices[:, 2] > np.mean(vertices[:, 2])  # 选择鼻子区域
# vertices[nose_region, 2] += 3.0  # 让鼻子更高

# 颧骨调整
cheek_region = (vertices[:, 0] > 0.02) | (vertices[:, 0] < -0.02)  # 选取颧骨
vertices[cheek_region, 0] *= 1.1  # 让颧骨更宽

# 眼睛调整
eye_region = vertices[:, 1] > np.mean(vertices[:, 1])  # 选取眼睛
vertices[eye_region, 1] += 1.0  # 让眼睛上移

# 更新 Mesh
mesh.vertices = o3d.utility.Vector3dVector(vertices)
mesh.compute_vertex_normals()

# 显示调整后的人脸
o3d.visualization.draw_geometries([mesh])

# import tkinter as tk
# from tkinter import filedialog

# # 创建滑块
# root = tk.Tk()
# tk.Scale(root, from_=0.8, to=1.2, resolution=0.01, orient=tk.HORIZONTAL, label="鼻子大小").pack()
# tk.Scale(root, from_=0.8, to=1.2, resolution=0.01, orient=tk.HORIZONTAL, label="颧骨宽度").pack()
# root.mainloop()