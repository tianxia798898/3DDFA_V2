import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 打开 HDF5 文件
file_path = 'examples/inputs/model2019_face12.h5'  # 请替换为你的 H5 文件路径
with h5py.File(file_path, 'r') as f:
    # 获取顶点数据（从 'shape/model/mean' 路径获取）
    vertices = f['shape/model/mean'][:]
    
    # 获取面数据（从 'shape/representer/cells' 路径获取）
    faces = f['shape/representer/cells'][:]

# 检查数据形状
print(f"Vertices shape: {vertices.shape}")  # 输出形状，如 (n, 3)，n为顶点数量
print(f"Faces shape: {faces.shape}")  # 输出形状，通常是 (m, 3)，m为面片数量，每个面由3个顶点组成

# 如果 vertices 不是二维数组，则需要重塑
if len(vertices.shape) == 1:
    print("Reshaping vertices to 2D array...")
    # 假设顶点数是 vertices 的长度，3 是坐标维度
    vertices = vertices.reshape(-1, 3)

# 创建3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 可视化顶点
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=1)

# 假设 faces 是一个顶点索引的数组，每个face是一个顶点索引的列表（通常是3个顶点组成一个三角形面）
# 绘制每个面
faces_triangles = []
for face in faces:
    # 获取面对应的三个顶点坐标
    triangle = vertices[face]
    faces_triangles.append(triangle)

# 绘制面片（将面片的三角形放入 Poly3DCollection 中）
mesh = Poly3DCollection(faces_triangles, facecolors='cyan', linewidths=0.5, edgecolors='r', alpha=.25)
ax.add_collection3d(mesh)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示3D图形
plt.show()